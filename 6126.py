from ctypes import *

_stdcall_libraries = {}
_stdcall_libraries['6126.dll'] = WinDLL('6126.dll')
from ctypes.wintypes import HANDLE


W_6126_Initial = _stdcall_libraries['6126.dll'].W_6126_Initial
W_6126_Initial.restype = c_int
W_6126_Initial.argtypes = [c_int, c_int, c_int]
W_6126_Switch_Card_No = _stdcall_libraries['6126.dll'].W_6126_Switch_Card_No
W_6126_Switch_Card_No.restype = c_int
W_6126_Switch_Card_No.argtypes = [c_int]
W_6126_DI = _stdcall_libraries['6126.dll'].W_6126_DI
W_6126_DI.restype = c_int
W_6126_DI.argtypes = [c_int, POINTER(c_ubyte)]
W_6126_DI_Channel = _stdcall_libraries['6126.dll'].W_6126_DI_Channel
W_6126_DI_Channel.restype = c_int
W_6126_DI_Channel.argtypes = [c_int, POINTER(c_uint)]
W_6126_DO = _stdcall_libraries['6126.dll'].W_6126_DO
W_6126_DO.restype = c_int
W_6126_DO.argtypes = [c_int, c_ubyte]
W_6126_DA = _stdcall_libraries['6126.dll'].W_6126_DA
W_6126_DA.restype = c_int
W_6126_DA.argtypes = [c_int, c_uint]
W_6126_INTOP_Start = _stdcall_libraries['6126.dll'].W_6126_INTOP_Start
W_6126_INTOP_Start.restype = c_int
W_6126_INTOP_Start.argtypes = [c_int]
W_6126_INTOP_Status = _stdcall_libraries['6126.dll'].W_6126_INTOP_Status
W_6126_INTOP_Status.restype = c_int
W_6126_INTOP_Status.argtypes = [POINTER(c_int), POINTER(c_int)]
W_6126_INTOP_Stop = _stdcall_libraries['6126.dll'].W_6126_INTOP_Stop
W_6126_INTOP_Stop.restype = c_int
W_6126_INTOP_Stop.argtypes = [POINTER(c_int)]
W_6126_INT_Enable = _stdcall_libraries['6126.dll'].W_6126_INT_Enable
W_6126_INT_Enable.restype = c_int
W_6126_INT_Enable.argtypes = [POINTER(HANDLE)]
W_6126_INT_Disable = _stdcall_libraries['6126.dll'].W_6126_INT_Disable
W_6126_INT_Disable.restype = c_int
W_6126_INT_Disable.argtypes = []
__all__ = ['W_6126_DI_Channel', 'W_6126_INTOP_Start',
           'W_6126_Switch_Card_No', 'W_6126_INTOP_Status',
           'W_6126_INT_Disable', 'W_6126_INTOP_Stop', 'W_6126_DO',
           'W_6126_DI', 'W_6126_Initial', 'W_6126_DA',
           'W_6126_INT_Enable']
