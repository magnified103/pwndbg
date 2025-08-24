from ctypes import Structure, c_ulong, c_ushort, c_byte
from functools import partial
from uuid import UUID


class IID(Structure):
    _fields_ = [
        ("Data1", c_ulong),
        ("Data2", c_ushort),
        ("Data3", c_ushort),
        ("Data4", c_byte * 8),
    ]


# https://stackoverflow.com/a/76301341
class classproperty:
    def __init__(self, func):
        self.fget = func
    def __get__(self, instance, owner):
        return self.fget(owner)


class ComMixin:
    uuid = None

    def __getattr__(self, name):
        return partial(getattr(self.lpVtbl.contents, name), self)
    
    @property
    def vtable(self):
        return self.lpVtbl.contents

    @classproperty
    def iid(cls):
        raw = UUID(cls.uuid).bytes_le
        return IID.from_buffer_copy(raw)
