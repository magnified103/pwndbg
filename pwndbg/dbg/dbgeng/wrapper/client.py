from ctypes import *
from pwndbg.dbg.dbgeng.wrapper.utils import ComMixin, IID


class IDebugClient(ComMixin, Structure):
    uuid = "27fe5639-8407-4f47-8364-ee118fb08ac8"


class IDebugClientVtbl(Structure):
    _fields_ = [
        ("QueryInterface", WINFUNCTYPE(HRESULT, POINTER(IDebugClient), POINTER(IID), POINTER(c_void_p))),
        ("AddRef", c_void_p),
        ("Release", c_void_p),
        ("AttachKernel", c_void_p),
        ("GetKernelConnectionOptions", c_void_p),
        ("SetKernelConnectionOptions", c_void_p),
        ("StartProcessServer", c_void_p),
        ("ConnectProcessServer", c_void_p),
        ("DisconnectProcessServer", c_void_p),
        ("GetRunningProcessSystemIds", c_void_p),
        ("GetRunningProcessSystemIdByExecutableName", c_void_p),
        ("GetRunningProcessDescription", c_void_p),
        ("AttachProcess", c_void_p),
        ("CreateProcess", c_void_p),
        ("CreateProcessAndAttach", c_void_p),
        ("GetProcessOptions", c_void_p),
        ("AddProcessOptions", c_void_p),
        ("RemoveProcessOptions", c_void_p),
        ("SetProcessOptions", c_void_p),
        ("OpenDumpFile", c_void_p),
        ("WriteDumpFile", c_void_p),
        ("ConnectSession", c_void_p),
        ("StartServer", c_void_p),
        ("OutputServers", c_void_p),
        ("TerminateProcesses", c_void_p),
        ("DetachProcesses", c_void_p),
        ("EndSession", c_void_p),
        ("GetExitCode", c_void_p),
        ("DispatchCallbacks", c_void_p),
        ("ExitDispatch", c_void_p),
        ("CreateClient", c_void_p),
        ("GetInputCallbacks", c_void_p),
        ("SetInputCallbacks", c_void_p),
        ("GetOutputCallbacks", c_void_p),
        ("SetOutputCallbacks", c_void_p),
        ("GetOutputMask", c_void_p),
        ("SetOutputMask", c_void_p),
        ("GetOtherOutputMask", c_void_p),
        ("SetOtherOutputMask", c_void_p),
        ("GetOutputWidth", c_void_p),
        ("SetOutputWidth", c_void_p),
        ("GetOutputLinePrefix", c_void_p),
        ("SetOutputLinePrefix", c_void_p),
        ("GetIdentity", c_void_p),
        ("OutputIdentity", c_void_p),
        ("GetEventCallbacks", c_void_p),
        ("SetEventCallbacks", c_void_p),
        ("FlushCallbacks", c_void_p),
    ]


IDebugClient._fields_ = [("lpVtbl", POINTER(IDebugClientVtbl))]
