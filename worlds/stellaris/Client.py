import urllib.parse
import logging
import os
import json

import Utils
from CommonClient import ClientCommandProcessor, CommonContext, gui_enabled, server_loop, get_base_parser
import asyncio
from pymem import Pymem, pattern, process
import sys

from NetUtils import add_json_item, add_json_text, add_json_location, JSONTypes
from .Generate import generateMod
from . import DataTest

logger = logging.getLogger("Client")

#########################################################################################
#          _______ _______ _______               _______  ______ _____ _______          #
#          |______    |    |______ |      |      |_____| |_____/   |   |______          #
#          ______|    |    |______ |_____ |_____ |     | |    \_ __|__ ______|          #
#########################################################################################

#[VARIABLES]############################################################################################################
codeInConst      = 7500000000
codeOutConst     = 750000
resConst         = 100000
patternSearch1   = b"\xE0\xAE\x58\x2D\x53\x01"
patternSearch2   = b"\xC0\x72\x00\x5D\x36\x02"
referenceNumber1 = 1456754700000
referenceNumber2 = 2432511800000
baseRes          = 0
emerRes          = 0

commResIn              = []
commResSendPhysics     = []
commResSendSociety     = []
commResSendEngineering = []

pm                 = Pymem()
itemsReceived      = []
itemsReceivedFinal = []
locationChecks     = []


#[METHODS]##############################################################################################################
def decodeItemCode(item):
    """This method takes the Item Codes provided by the server and converts them into a form readable by the game

    SERVER => GAME"""
    code = item - codeInConst + countReceivedItem(item)
    logger.info("Received item " + str(item) + ", converted to internal code " + str(code))
    return int(code)


def encodeItemCode(item):
    """This method takes the Item Codes provided by the game and converts them into a form readable by the server

    GAME => SERVER"""
    code = item + codeOutConst
    logger.info("Received item " + str(item) + ", converted to external code" + str(code))
    return int(code)


def grabResources():
    """This method reads the current Communication Resource Values"""
    global commResIn
    global commResSendPhysics
    global commResSendSociety
    global commResSendEngineering
    commResIn[1]  = pm.read_longlong(commResIn[0])  / resConst
    commResSendPhysics[1]     = pm.read_longlong(commResSendPhysics[0])     / resConst
    commResSendSociety[1]     = pm.read_longlong(commResSendSociety[0])     / resConst
    commResSendEngineering[1] = pm.read_longlong(commResSendEngineering[0]) / resConst


def findBaseRes(patternMatch):
    """This method searches the game's process' memory for a value with binary pattern *patternMatch*"""
    referenceResourceAddress = pattern.pattern_scan_all(pm.process_handle, patternMatch, return_multiple=False)
    try:
        logger.info(
            "Reference resource " + str(patternMatch) + " found at address " + str(hex(referenceResourceAddress)))
    except:
        logger.error("ERROR: Reference Resource could not be found.")
    return referenceResourceAddress


def checkBaseRes(res):
    """This method checks if the provided address can be read"""
    try:
        logger.info("Reference resource value is: " + str(pm.read_longlong(res)))
    except:
        logger.error("ERROR: Reference Resource cannot be read.")


#[CLIENT]###############################################################################################################
async def connectToStellaris():
    """This method connects to Stellaris;
    Finds and checks the reference resources;
    Finds the communication resources via an offset from the reference resources"""
    logger.info("Trying to connect to Stellaris")
    global pm
    global baseRes
    global emerRes
    global commResIn
    global commResSendPhysics
    global commResSendSociety
    global commResSendEngineering

    await asyncio.sleep(1)
    try:
        pm = Pymem("stellaris.exe")
    except:
        logger.error("ERROR: Stellaris couldn't be found. Did you forget to launch the game?")
    else:
        logger.info("Stellaris found: " + str(pm))

        logger.info("Searching for Reference Resource " + str(patternSearch1) + "...")
        await asyncio.sleep(0.1)
        baseRes = findBaseRes(patternSearch1)
        checkBaseRes(baseRes)

        logger.info("Searching for Reference Resource " + str(patternSearch2) + "...")
        await asyncio.sleep(0.1)
        emerRes = findBaseRes(patternSearch2)
        checkBaseRes(emerRes)

        if pm.read_longlong(baseRes + 0x8) != referenceNumber2 or pm.read_longlong(emerRes - 0x8) != referenceNumber1:
            logger.error("ERROR: Wrong reference addresses found.")

        commResIn              = [baseRes - 0x20, 0] ### Items going into Stellaris
        commResSendPhysics     = [baseRes - 0x18,  0] ## Physics Techs going out of Stellaris
        commResSendSociety     = [baseRes - 0x10, 0] ### Society Techs going out of Stellaris
        commResSendEngineering = [baseRes - 0x8, 0] #### Engineering Techs going out of Stellaris
        grabResources()

        return True

def countReceivedItem(item):
    count = 0
    for i in range(len(itemsReceived)):
        if itemsReceived[i] == item:
            count += 1
    return count

def receiveItem():
    """This method takes the item's code and sets the Receive Communication Resource to it.
    Waits until the resource is 0 before doing anything."""
    global itemsReceivedFinal
    if commResIn[1] == 0 and len(itemsReceivedFinal) != 0:
        logger.info("Items Received List " + str(itemsReceivedFinal))
        curItem = decodeItemCode(itemsReceivedFinal[0])
        logger.info("   Sending item " + str(curItem) + " to Stellaris")
        pm.write_longlong(commResIn[0], curItem * resConst)
        logger.info("   " + str(curItem) + " was sent to Stellaris")
        itemsReceivedFinal.pop(0)
        logger.info("Items left to send: " + str(len(itemsReceivedFinal)))

def sendItemResource(resource):
    """This method checks a specific resource for if there's a location check to receive from Stellaris"""
    if resource[1] != 0:
        logger.info("Location checks: " + str(locationChecks))
        curItem = encodeItemCode(resource[1])
        pm.write_longlong(resource[0], 0)
        locationChecks.append(curItem)
        logger.info("   Receiving location check " + str(curItem) + " from Stellaris")

def sendItem():
    """This method receives location checks from Stellaris"""
    global locationChecks
    sendItemResource(commResSendPhysics)
    sendItemResource(commResSendSociety)
    sendItemResource(commResSendEngineering)


async def loopTransmit():
    """This is the primary communication loop for transmitting information between the game and the client"""
    while True:
        #print(print(len(itemsReceived),"   ",itemsReceivedNum))
        grabResources()
        receiveItem()
        sendItem()
        await asyncio.sleep(0.1)


def runStellarisClient(*args):
    class StellarisCommandProcessor(ClientCommandProcessor):
        def _cmd_reconnect_stellaris(self):
            """Try to reconnect to Stellaris if the connection failed"""
            stellaris_game_task = asyncio.create_task(connectToStellaris(), name = "StellarisConnection")

    class StellarisContext(CommonContext):
        command_processor = StellarisCommandProcessor
        game              = "Stellaris" # Empty matches any game since 0.3.2
        items_handling    = 0b111 ####### Receive all items for /received
        want_slot_data    = False ####### Can't use game specific slot_data

        def __init__(self, server_address, password):
            super(StellarisContext, self).__init__(server_address, password)

        async def get_username(self):
            if not self.auth:
                self.auth = self.username
                if not self.auth:
                    logger.info('Enter slot name:')
                    self.auth = await self.console_input()

        async def server_auth(self, password_requested: bool = False):
            if password_requested and not self.password:
                await super(StellarisContext, self).server_auth(password_requested)
            await self.get_username()
            await self.send_connect()

        def on_package(self, cmd: str, args: dict):
            #print(cmd,args)
            if cmd == "RoomInfo":
                self.seed_name = args["seed_name"]

            if cmd == "Connected":
                self.game = self.slot_info[self.slot].game

            elif cmd == 'ReceivedItems':
                global itemsReceived
                global itemsReceivedFinal
                for index, item in enumerate(self.items_received, 1):
                    itemsReceived.append(item.item)
                for item in itemsReceived:
                    num = 0
                    for allItems in itemsReceived:
                        if allItems == item:
                            num += 1
                            if num <= 9 and not item + num in itemsReceivedFinal: itemsReceivedFinal.append(item + num)
                        print(item + num)
                itemsReceived.clear()
                print(itemsReceivedFinal)

        async def disconnect(self, allow_autoreconnect: bool = False):
            await super().disconnect(allow_autoreconnect)

    async def finalSendItem(ctx: StellarisContext):
        while True:
            global locationChecks
            if len(locationChecks) != 0:
                await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [int(locationChecks[0])]}])
                logger.info("   Sent item " + str(locationChecks[0]) + " to the server.")
                locationChecks.pop(0)
            await asyncio.sleep(0.1)

    async def main(args):
        ctx = StellarisContext(args.connect, args.password)

        ctx.auth        = args.name
        ctx.server_task = asyncio.create_task(server_loop(ctx), name = "server loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        stellaris_game_task   = asyncio.create_task(connectToStellaris(), name = "StellarisConnection")
        successful_connection = await stellaris_game_task

        if successful_connection:
            logger.info("Connected to Stellaris successfully\n")
            stellaris_loop_task = asyncio.create_task(loopTransmit(), name = "Game loop")
            stellaris_send_task = asyncio.create_task(finalSendItem(ctx))

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description = "Stellaris Archipelago Client.")
    parser.add_argument('--name', default = None, help = "Slot Name to connect as.")
    parser.add_argument("url", nargs = "?",       help = "Archipelago connection url")
    args = parser.parse_args(args)

    # handle if text client is launched using the "archipelago://name:pass@host:port" url from webhost
    if args.url:
        url = urllib.parse.urlparse(args.url)
        if url.scheme == "archipelago":
            args.connect = url.netloc
            if url.username:
                args.name     = urllib.parse.unquote(url.username)
            if url.password:
                args.password = urllib.parse.unquote(url.password)
        else:
            parser.error(f"bad url, found {args.url}, expected url in form of archipelago://archipelago.gg:38281")

    # use colorama to display colored text highlighting on windows
    colorama.init()

    asyncio.run(main(args))

    colorama.deinit()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO) # force log-level to work around log level resetting to WARNING
    runStellarisClient(*sys.argv[1:]) ########## default value for parse_args