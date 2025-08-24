from pwndbg.dbg.dbgeng.wrapper.client import IDebugClient
from pwndbg.dbg.dbgeng.wrapper.control import IDebugControl
from pwndbg.dbg.dbgeng.wrapper.registers import IDebugRegisters
from pwndbg.dbg.dbgeng.wrapper.systemobjects import IDebugSystemObjects
from pwndbg.dbg.dbgeng.wrapper.utils import IID
from ctypes import *


def DebugCreate() -> IDebugClient:
    DbgEng = WinDLL("dbgeng.dll")
    DbgEng.DebugCreate.argtypes = [POINTER(IID), POINTER(POINTER(IDebugClient))]
    DbgEng.DebugCreate.restype = HRESULT

    ptr = POINTER(IDebugClient)()
    DbgEng.DebugCreate(byref(IDebugClient.iid), byref(ptr))

    return ptr.contents
