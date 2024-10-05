from pymem import Pymem, pattern, process
import time
import sys
import DataTest

#[VARIABLES]############################################################################
resConst = 100000

patternSearch1 = b"\xE0\xAE\x58\x2D\x53\x01"
patternSearch2 = b"\xC0\x72\x00\x5D\x36\x02"

referenceNumber1 = 1456754700000
referenceNumber2 = 2432511800000

itemsToReceive = DataTest.testItems

#[FUNCTIONS]#############################################################################
#This function finds an address in Process memory based on the provided pattern
def findBaseRes(patternMatch):
    print("Searching for Reference Resource ",patternMatch,"...")
    referenceResourceAddress = pattern.pattern_scan_all(pm.process_handle, patternMatch, return_multiple=False)
    try:
        print("Reference resource ", patternMatch, " found at address ",hex(referenceResourceAddress))
    except:
        sys.exit("ERROR: Reference Resource could not be found. Aborting.")
    return referenceResourceAddress

#This function checks whether the discovered address has an int in it
def checkBaseRes(res):
    try:
        print("Reference resource value is: ",pm.read_longlong(res))
    except:
        sys.exit("ERROR: Reference Resource cannot be read. Aborting.")

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
    sys.exit("ERROR: stellaris.exe not found. Aborting.\nDid you forget to launch the game?")
else:
    print("Stellaris found.")

#[FINDING REFERENCE RESOURCES]###########################################################
print("Connecting to Stellaris")
baseRes = findBaseRes(patternSearch1)
checkBaseRes(baseRes)
emerRes = findBaseRes(patternSearch2)
checkBaseRes(emerRes)

if pm.read_longlong(baseRes+0x8) != referenceNumber2 or pm.read_longlong(emerRes-0x8) != referenceNumber1:
    sys.exit("ERROR: Wrong reference addresses found. Aborting.")

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