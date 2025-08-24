from ctypes import *
from pwndbg.dbg.dbgeng.wrapper.utils import ComMixin, IID


class IDebugSystemObjects(ComMixin, Structure):
    uuid = "6b86fe2c-2c4f-4f0c-9da2-174311acc327"


class IDebugSystemObjectsVtbl(Structure):
    _fields_ = [
        ("QueryInterface", WINFUNCTYPE(HRESULT, POINTER(IDebugSystemObjects), POINTER(IID), POINTER(c_void_p))),
        ("AddRef", c_void_p),
        ("Release", c_void_p),
        ("GetEventThread", c_void_p),
        ("GetEventProcess", c_void_p),
        ("GetCurrentThreadId", c_void_p),
        ("SetCurrentThreadId", c_void_p),
        ("GetCurrentProcessId", c_void_p),
        ("SetCurrentProcessId", c_void_p),
        ("GetNumberThreads", c_void_p),
        ("GetTotalNumberThreads", c_void_p),
        ("GetThreadIdsByIndex", c_void_p),
        ("GetThreadIdByProcessor", c_void_p),
        ("GetCurrentThreadDataOffset", c_void_p),
        ("GetThreadIdByDataOffset", c_void_p),
        ("GetCurrentThreadTeb", c_void_p),
        ("GetThreadIdByTeb", c_void_p),
        ("GetCurrentThreadSystemId", c_void_p),
        ("GetThreadIdBySystemId", c_void_p),
        ("GetCurrentThreadHandle", c_void_p),
        ("GetThreadIdByHandle", c_void_p),
        ("GetNumberProcesses", c_void_p),
        ("GetProcessIdsByIndex", c_void_p),
        ("GetCurrentProcessDataOffset", c_void_p),
        ("GetProcessIdByDataOffset", c_void_p),
        ("GetCurrentProcessPeb", c_void_p),
        ("GetProcessIdByPeb", c_void_p),
        ("GetCurrentProcessSystemId", c_void_p),
        ("GetProcessIdBySystemId", c_void_p),
        ("GetCurrentProcessHandle", c_void_p),
        ("GetProcessIdByHandle", c_void_p),
        ("GetCurrentProcessExecutableName", c_void_p),
    ]


IDebugSystemObjects._fields_ = [("lpVtbl", POINTER(IDebugSystemObjectsVtbl))]
