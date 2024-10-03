from pymem import Pymem, pattern, process
import time
import EventData

pm = Pymem("stellaris.exe")
stellarisModule = process.base_module(pm.process_handle)

resConst = 100000
receiveWaiter = 0

patternSearch1 = b"\xE0\xAE\x58\x2D\x53\x01"
patternSearch2 = b"\xC0\x72\x00\x5D\x36\x02"

def findBaseRes(patternMatch):
    print("Searching for Reference Resource ",patternMatch,"...")
    #referenceResourceAddress = pattern.pattern_scan_module(pm.process_handle, stellarisModule, patternSearch)
    referenceResourceAddress = pattern.pattern_scan_all(pm.process_handle, patternMatch, return_multiple=False)
    print("Reference resource ",patternMatch," found")
    return referenceResourceAddress

def sendItem(itemNum,res,waitNum):
    if res[1] == 0:
        waitNum = waitNum-1
        pm.write_longlong(res[0], itemNum)
        print(pm.read_longlong(res[0]) / resConst)
    else:
        print("Waiting for event to fire off...")
    print("Items left to send off: ",waitNum)
    time.sleep(1)
    return waitNum

print("Connecting to Stellaris")
baseRes = findBaseRes(patternSearch1)
emerRes = findBaseRes(patternSearch2)

print("   ",hex(baseRes),"   -   ",hex(emerRes))
print("   ",pm.read_longlong(baseRes),"   -   ",pm.read_longlong(emerRes))

time.sleep(1)

#Communication resources
print("Grabbing communication resources")
commResIn = [baseRes-0x10,0] #Items going into Stellaris
commResOut = [baseRes-0x8,0] #Items going out of Stellaris

print("Testing item sending process")
receiveWaiter = len(EventData.items)
while receiveWaiter != 0:
    commResIn[1]  = pm.read_longlong(commResIn[0])/resConst
    commResOut[1] = pm.read_longlong(commResOut[0])/resConst
    receiveWaiter = sendItem(EventData.items[len(EventData.items)-receiveWaiter]*resConst,commResIn,receiveWaiter)