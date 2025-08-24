#pragma comment(lib, "dbgeng.lib")

#include <DbgEng.h>
#include <Python.h>




__declspec(dllexport) HRESULT CALLBACK DebugExtensionInitialize(PULONG version, PULONG flags) {
    *version = DEBUG_EXTENSION_VERSION(2025, 05);
    *flags = 0;

    if (Py_IsInitialized() == 0) {
        Py_Initialize();
    }

    return S_OK;
}

__declspec(dllexport) HRESULT CALLBACK pwndbg(PDEBUG_CLIENT4 client, PCSTR args) {
    /*

    */
    if (Py_IsInitialized() == 0) {
        Py_Initialize();
    }
    return S_OK;
}
