from ctypes import *
from pwndbg.dbg.dbgeng.wrapper.utils import ComMixin, IID


class _I64(Structure):
    _fields_ = [
        ('I64', c_ulonglong),
        ('Nat', c_int),
    ]


class _u(Structure):
    _fields_ = [
        ('I8', c_ubyte),
        ('I16', c_ushort),
        ('I32', c_ulong),
        ('I64', _I64),
        ('F32', c_float),
        ('F64', c_double),
        ('F80Bytes', c_ubyte * 10),
        ('F82Bytes', c_ubyte * 11),
        ('F128Bytes', c_ubyte * 16),
        ('VI8', c_ubyte * 16),
        ('VI16', c_ushort * 8),
        ('VI32', c_ulong * 4),
        ('VI64', c_ulonglong * 2),
        ('VF32', c_float * 4),
        ('VF64', c_double * 2),
        ('I64Parts32', __MIDL___MIDL_itf_dbgeng_0001_0083_0158),
        ('F128Parts64', __MIDL___MIDL_itf_dbgeng_0001_0083_0159),
        ('RawBytes', c_ubyte * 24),
    ]


class DEBUG_VALUE(Structure):
    class _U(Union):
        _fields_ = [
            ("I8", c_ubyte),
            ("I16", c_ushort),
            ("I32", c_ulong),

        ]

    _fields_ = [
        ("Type", c_uint32),
        ("Reserved", c_uint32 * 3),
        ("u", _U),
    ]


class IDebugRegisters(ComMixin, Structure):
    uuid = "ce289126-9e84-45a7-937e-67bb18691493"


class IDebugRegistersVtbl(Structure):
    _fields_ = [
        ("QueryInterface", WINFUNCTYPE(HRESULT, POINTER(IDebugRegisters), POINTER(IID), POINTER(c_void_p))),
        ("AddRef", c_void_p),
        ("Release", c_void_p),
    ]


IDebugRegisters._fields_ = [("lpVtbl", POINTER(IDebugRegistersVtbl))]
