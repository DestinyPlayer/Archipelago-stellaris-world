from pymem import Pymem
from pymem import pattern
from pymem import process
import time
import ctypes

pm = Pymem("stellaris.exe")
stellarisModule = process.base_module(pm.process_handle)

patternSearch1 = b"\xE0\xAE\x58\x2D\x53\x01"
patternSearch2 = b"\xC0\x72\x00\x5D\x36\x02"

def findBaseRes(patternMatch):
    #referenceResourceAddress = pattern.pattern_scan_module(pm.process_handle, stellarisModule, patternSearch)
    referenceResourceAddress = pattern.pattern_scan_all(pm.process_handle, patternMatch, return_multiple=False)
    return referenceResourceAddress


resConst = 100000

baseRes = findBaseRes(patternSearch1)
emerRes = findBaseRes(patternSearch2)
for i in range(1):
    print(baseRes)
    print(emerRes)
    print(hex(baseRes),"   -   ",hex(emerRes))
    print(pm.read_longlong(baseRes),"   -   ",pm.read_longlong(emerRes))
    time.sleep(1)

#This is the communication resource!
commRes = baseRes-0x8
for i in range(10):
    pm.write_longlong(commRes,1416*resConst*i)
    print(pm.read_longlong(commRes)/resConst)
    time.sleep(1)