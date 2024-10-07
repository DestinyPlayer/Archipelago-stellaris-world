import urllib.parse
import logging
from CommonClient import ClientCommandProcessor, CommonContext, gui_enabled, server_loop, get_base_parser
import asyncio
from pymem import Pymem, pattern, process
import sys

from worlds.dlcquest.test.TestItemShuffle import items
from . import DataTest

logger = logging.getLogger("Client")

########################################################################################
#          _______ _______ _______               _______  ______ _____ _______         #
#          |______    |    |______ |      |      |_____| |_____/   |   |______         #
#          ______|    |    |______ |_____ |_____ |     | |    \_ __|__ ______|         #
########################################################################################

#[COMMON CLIENT]########################################################################

# [CONNECTION TO THE GAME]################################################################
resConst = 100000

patternSearch1 = b"\xE0\xAE\x58\x2D\x53\x01"
patternSearch2 = b"\xC0\x72\x00\x5D\x36\x02"

referenceNumber1 = 1456754700000
referenceNumber2 = 2432511800000

baseRes = 0
emerRes = 0

commResIn = [0, 0]
commResOut = [0, 0]

pm = Pymem()
itemsToReceive = DataTest.testItems

# This function takes item code in form AP-Y-XXX and converts it into the YXXX form readable by the game
def decodeItemCode(item):
    splitItem = item.split("-")
    code = splitItem[1] + splitItem[2]
    logger.info("Received item "+str(item)+", converted to internal code "+str(code))
    return int(code)

def grabResources():
    global commResIn
    global commResOut
    commResIn[1] = pm.read_longlong(commResIn[0]) / resConst
    commResOut[1] = pm.read_longlong(commResOut[0]) / resConst

def findBaseRes(patternMatch):
    referenceResourceAddress = pattern.pattern_scan_all(pm.process_handle, patternMatch, return_multiple=False)
    try:
        logger.info("Reference resource "+str(patternMatch)+" found at address "+str(hex(referenceResourceAddress)))
    except:
        logger.error("ERROR: Reference Resource could not be found. Aborting.")
    return referenceResourceAddress

def checkBaseRes(res):
    try:
        logger.info("Reference resource value is: "+str(pm.read_longlong(res)))
    except:
        logger.error("ERROR: Reference Resource cannot be read. Aborting.")

async def connectToStellaris():
    logger.info("Trying to connect to Stellaris")
    global pm
    global baseRes
    global emerRes
    global commResIn
    global commResOut

    await asyncio.sleep(1)
    try:
        pm = Pymem("stellaris.exe")
    except:
        logger.error("ERROR: Stellaris couldn't be found. Did you forget to launch the game?")
    else:
        logger.info("Stellaris found: "+str(pm))
        logger.info("Searching for Reference Resource " + str(patternSearch1) + "...")
        await asyncio.sleep(0.1)
        baseRes = findBaseRes(patternSearch1)
        checkBaseRes(baseRes)
        logger.info("Searching for Reference Resource " + str(patternSearch2) + "...")
        await asyncio.sleep(0.1)
        emerRes = findBaseRes(patternSearch2)
        checkBaseRes(emerRes)
        if pm.read_longlong(baseRes + 0x8) != referenceNumber2 or pm.read_longlong(
                emerRes - 0x8) != referenceNumber1:
            logger.error("ERROR: Wrong reference addresses found. Aborting.")
        commResIn = [baseRes - 0x10, 0]  # Items going into Stellaris
        commResOut = [baseRes - 0x8, 0]  # Items going out of Stellaris
        grabResources()
        return True


def receiveItem(item, listLen):
    if commResIn[1] == 0:
        curItem = decodeItemCode(item)
        logger.info("   Sending item "+str(item)+" to Stellaris")
        pm.write_longlong(commResIn[0], curItem * resConst)
        logger.info("   "+str(item)+" was sent to Stellaris")
        itemsToReceive.pop(listLen - 1)


async def loopTransmit(getItems):
    while True:
        grabResources()
        length = len(getItems)
        if length != 0:
            for item in getItems:
                receiveItem(item, length)
        await asyncio.sleep(1)

def runStellarisClient(*args):
    class StellarisCommandProcessor(ClientCommandProcessor):
        def _cmd_reconnect_stellaris(self):
            """Try to reconnect to Stellaris if the connection failed"""
            stellaris_game_task = asyncio.create_task(connectToStellaris(), name="StellarisConnection")

    class StellarisContext(CommonContext):
        command_processor = StellarisCommandProcessor
        # Text Mode to use !hint and such with games that have no text entry
        tags = CommonContext.tags | {"TextOnly"}
        game = "Stellaris"  # empty matches any game since 0.3.2
        items_handling = 0b111  # receive all items for /received
        want_slot_data = False  # Can't use game specific slot_data

        async def server_auth(self, password_requested: bool = False):
            if password_requested and not self.password:
                await super(StellarisContext, self).server_auth(password_requested)
            await self.get_username()
            await self.send_connect()

        def on_package(self, cmd: str, args: dict):
            if cmd == "Connected":
                self.game = self.slot_info[self.slot].game


        async def disconnect(self, allow_autoreconnect: bool = False):
            self.game = ""
            await super().disconnect(allow_autoreconnect)

    async def main(args):
        ctx = StellarisContext(args.connect, args.password)

        ctx.auth = args.name
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        stellaris_game_task = asyncio.create_task(connectToStellaris(), name="StellarisConnection")
        successful_connection = await stellaris_game_task

        if successful_connection:
            logger.info("Connected to Stellaris successfully\n")
            stellaris_loop_task = asyncio.create_task(loopTransmit(itemsToReceive), name="Game loop")

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Stellaris Archipelago Client.")
    parser.add_argument('--name', default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    args = parser.parse_args(args)

    # handle if text client is launched using the "archipelago://name:pass@host:port" url from webhost
    if args.url:
        url = urllib.parse.urlparse(args.url)
        if url.scheme == "archipelago":
            args.connect = url.netloc
            if url.username:
                args.name = urllib.parse.unquote(url.username)
            if url.password:
                args.password = urllib.parse.unquote(url.password)
        else:
            parser.error(f"bad url, found {args.url}, expected url in form of archipelago://archipelago.gg:38281")

    # use colorama to display colored text highlighting on windows
    colorama.init()

    asyncio.run(main(args))

    colorama.deinit()

#INTERRUPT FOR TESTING
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)  # force log-level to work around log level resetting to WARNING
    runStellarisClient(*sys.argv[1:])  # default value for parse_args

#[VARIABLES]############################################################################

connectionAddress = "localhost"
connectionPort = "38281"

connectionFullAddress = "ws://"+connectionAddress+":"+connectionPort
'''
#[GAME FUNCTIONS]########################################################################
#This function finds an address in Process memory based on the provided pattern
def findBaseRes(patternMatch):
    print("Searching for Reference Resource ",patternMatch,"...")
    referenceResourceAddress = pattern.pattern_scan_all(pm.process_handle, patternMatch, return_multiple=False)
    try:
        print("Reference resource ", patternMatch, " found at address ",hex(referenceResourceAddress))
    except:
        logger.info("ERROR: Reference Resource could not be found. Aborting.")
    return referenceResourceAddress

#This function checks whether the discovered address has an int in it
def checkBaseRes(res):
    try:
        print("Reference resource value is: ",pm.read_longlong(res))
    except:
        logger.info("ERROR: Reference Resource cannot be read. Aborting.")

#This function takes item code in form AP-Y-XXX and converts it into the YXXX form readable by the game
def decodeItemCode(item):
    splitItem = item.split("-")
    code = splitItem[1]+splitItem[2]
    print("Received item ",item,", converted to internal code ",code)
    return int(code)

#This function sends the decoded item value to the game and waits until it's been read
def receiveItem(itemNum,res,waitNum):
    if res[1] == 0:
        waitNum = waitNum - 1
        pm.write_longlong(res[0], itemNum)
        print(pm.read_longlong(res[0]) / resConst)
        itemsToReceive.pop(waitNum)
    else:
        print("Waiting for event to fire off...")
    print("Items left to accept: ",waitNum)
    return waitNum

#[CONNECTION TO THE GAME]################################################################
try:
    pm = Pymem("stellaris.exe")
    stellarisModule = process.base_module(pm.process_handle)
except:
    logger.info("ERROR: stellaris.exe not found. Aborting.\nDid you forget to launch the game?")
else:
    print("Stellaris found.")

#[FINDING REFERENCE RESOURCES]###########################################################
print("Connecting to Stellaris")
baseRes = findBaseRes(patternSearch1)
checkBaseRes(baseRes)
emerRes = findBaseRes(patternSearch2)
checkBaseRes(emerRes)

if pm.read_longlong(baseRes+0x8) != referenceNumber2 or pm.read_longlong(emerRes-0x8) != referenceNumber1:
    logger.info("ERROR: Wrong reference addresses found. Aborting.")

#[GRABBING COMMUNICATION RESOURCES]######################################################
print("Grabbing communication resources")
commResIn = [baseRes-0x10,0] #Items going into Stellaris
commResOut = [baseRes-0x8,0] #Items going out of Stellaris

#[ESTABLISHING COMMUNICATION LOOP]#######################################################
print("Testing item sending process")
while True:
    receiveWait = len(itemsToReceive)
    if receiveWait != 0:
        cur = decodeItemCode(itemsToReceive[receiveWait-1])
        commResIn[1]  = pm.read_longlong(commResIn[0])/resConst
        commResOut[1] = pm.read_longlong(commResOut[0])/resConst
        receiveWait = receiveItem(cur*resConst,commResIn,receiveWait)
    time.sleep(1)
'''