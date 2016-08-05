from ctypes import *

_stdcall_libraries = {}
_stdcall_libraries['8112pg.dll'] = WinDLL('8112pg.dll')


W_812_Initial = _stdcall_libraries['8112pg.dll'].W_812_Initial
W_812_Initial.restype = c_int
W_812_Initial.argtypes = [c_int, c_int]
W_812_Switch_Card_No = _stdcall_libraries['8112pg.dll'].W_812_Switch_Card_No
W_812_Switch_Card_No.restype = c_int
W_812_Switch_Card_No.argtypes = [c_int]
W_812_DI = _stdcall_libraries['8112pg.dll'].W_812_DI
W_812_DI.restype = c_int
W_812_DI.argtypes = [c_int, POINTER(c_ubyte)]
W_812_DI_Channel = _stdcall_libraries['8112pg.dll'].W_812_DI_Channel
W_812_DI_Channel.restype = c_int
W_812_DI_Channel.argtypes = [c_int, POINTER(c_uint)]
W_812_DO = _stdcall_libraries['8112pg.dll'].W_812_DO
W_812_DO.restype = c_int
W_812_DO.argtypes = [c_int, c_ubyte]
W_812_DA = _stdcall_libraries['8112pg.dll'].W_812_DA
W_812_DA.restype = c_int
W_812_DA.argtypes = [c_int, c_uint]
W_812_AD_Set_Channel = _stdcall_libraries['8112pg.dll'].W_812_AD_Set_Channel
W_812_AD_Set_Channel.restype = c_int
W_812_AD_Set_Channel.argtypes = [c_int]
W_812_AD_Set_Gain = _stdcall_libraries['8112pg.dll'].W_812_AD_Set_Gain
W_812_AD_Set_Gain.restype = c_int
W_812_AD_Set_Gain.argtypes = [c_int]
W_812_AD_Set_Mode = _stdcall_libraries['8112pg.dll'].W_812_AD_Set_Mode
W_812_AD_Set_Mode.restype = c_int
W_812_AD_Set_Mode.argtypes = [c_int]
W_812_AD_Soft_Trig = _stdcall_libraries['8112pg.dll'].W_812_AD_Soft_Trig
W_812_AD_Soft_Trig.restype = c_int
W_812_AD_Soft_Trig.argtypes = []
W_812_AD_Aquire = _stdcall_libraries['8112pg.dll'].W_812_AD_Aquire
W_812_AD_Aquire.restype = c_int
W_812_AD_Aquire.argtypes = [POINTER(c_int)]
W_812_CLR_IRQ = _stdcall_libraries['8112pg.dll'].W_812_CLR_IRQ
W_812_CLR_IRQ.restype = c_int
W_812_CLR_IRQ.argtypes = []
W_812_AD_DMA_Start = _stdcall_libraries['8112pg.dll'].W_812_AD_DMA_Start
W_812_AD_DMA_Start.restype = c_int
W_812_AD_DMA_Start.argtypes = [c_int, c_int, c_int, c_int, c_int, POINTER(c_ushort), c_uint, c_uint]
W_812_AD_DMA_Status = _stdcall_libraries['8112pg.dll'].W_812_AD_DMA_Status
W_812_AD_DMA_Status.restype = c_int
W_812_AD_DMA_Status.argtypes = [POINTER(c_int), POINTER(c_int)]
W_812_AD_DMA_Stop = _stdcall_libraries['8112pg.dll'].W_812_AD_DMA_Stop
W_812_AD_DMA_Stop.restype = c_int
W_812_AD_DMA_Stop.argtypes = [POINTER(c_int)]
W_812_AD_INT_Start = _stdcall_libraries['8112pg.dll'].W_812_AD_INT_Start
W_812_AD_INT_Start.restype = c_int
W_812_AD_INT_Start.argtypes = [c_int, c_int, c_int, c_int, POINTER(c_ushort), c_uint, c_uint]
W_812_AD_SCANINT_Start = _stdcall_libraries['8112pg.dll'].W_812_AD_SCANINT_Start
W_812_AD_SCANINT_Start.restype = c_int
W_812_AD_SCANINT_Start.argtypes = [c_int, c_int, c_int, c_int, POINTER(c_ushort), c_uint, c_uint]
W_812_AD_INT_Status = _stdcall_libraries['8112pg.dll'].W_812_AD_INT_Status
W_812_AD_INT_Status.restype = c_int
W_812_AD_INT_Status.argtypes = [POINTER(c_int), POINTER(c_int)]
W_812_AD_INT_Stop = _stdcall_libraries['8112pg.dll'].W_812_AD_INT_Stop
W_812_AD_INT_Stop.restype = c_int
W_812_AD_INT_Stop.argtypes = [POINTER(c_int)]
W_812_AD_Timer = _stdcall_libraries['8112pg.dll'].W_812_AD_Timer
W_812_AD_Timer.restype = c_int
W_812_AD_Timer.argtypes = [c_uint, c_uint]
W_812_TIMER_Start = _stdcall_libraries['8112pg.dll'].W_812_TIMER_Start
W_812_TIMER_Start.restype = c_int
W_812_TIMER_Start.argtypes = [c_int, c_uint]
W_812_TIMER_Read = _stdcall_libraries['8112pg.dll'].W_812_TIMER_Read
W_812_TIMER_Read.restype = c_int
W_812_TIMER_Read.argtypes = [POINTER(c_uint)]
W_812_TIMER_Stop = _stdcall_libraries['8112pg.dll'].W_812_TIMER_Stop
W_812_TIMER_Stop.restype = c_int
W_812_TIMER_Stop.argtypes = [POINTER(c_uint)]
W_812_DMA_InitialMemoryAllocated = _stdcall_libraries['8112pg.dll'].W_812_DMA_InitialMemoryAllocated
W_812_DMA_InitialMemoryAllocated.restype = c_int
W_812_DMA_InitialMemoryAllocated.argtypes = [POINTER(c_int)]
boolean = c_ubyte
W_812_AD_DblBufferHalfReady = _stdcall_libraries['8112pg.dll'].W_812_AD_DblBufferHalfReady
W_812_AD_DblBufferHalfReady.restype = c_int
W_812_AD_DblBufferHalfReady.argtypes = [POINTER(boolean)]
USHORT = c_ushort
W_812_AD_DblBufferTransfer = _stdcall_libraries['8112pg.dll'].W_812_AD_DblBufferTransfer
W_812_AD_DblBufferTransfer.restype = c_int
W_812_AD_DblBufferTransfer.argtypes = [POINTER(USHORT)]
W_812_AD_ContDMA_Start = _stdcall_libraries['8112pg.dll'].W_812_AD_ContDMA_Start
W_812_AD_ContDMA_Start.restype = c_int
W_812_AD_ContDMA_Start.argtypes = [c_int, c_int, c_int, c_int, c_int, POINTER(c_ushort), c_uint, c_uint]
Boolean = c_char
W_812_AD_ContINT_Start = _stdcall_libraries['8112pg.dll'].W_812_AD_ContINT_Start
W_812_AD_ContINT_Start.restype = c_int
W_812_AD_ContINT_Start.argtypes = [c_int, Boolean, c_int, c_int, c_int, POINTER(c_ushort), c_uint, c_uint]
__all__ = ['W_812_AD_DMA_Start', 'W_812_AD_INT_Start',
           'W_812_AD_Timer', 'W_812_AD_INT_Stop',
           'W_812_AD_SCANINT_Start', 'boolean', 'W_812_Initial',
           'W_812_TIMER_Read', 'W_812_AD_ContDMA_Start',
           'W_812_TIMER_Stop', 'W_812_AD_Set_Gain',
           'W_812_Switch_Card_No', 'W_812_DI', 'W_812_AD_Aquire',
           'W_812_DI_Channel', 'W_812_AD_Set_Mode',
           'W_812_AD_Set_Channel', 'W_812_AD_ContINT_Start',
           'W_812_DMA_InitialMemoryAllocated', 'W_812_AD_Soft_Trig',
           'W_812_DA', 'W_812_AD_INT_Status', 'W_812_TIMER_Start',
           'W_812_AD_DMA_Status', 'W_812_AD_DblBufferTransfer',
           'W_812_AD_DblBufferHalfReady', 'USHORT', 'W_812_DO',
           'W_812_AD_DMA_Stop', 'Boolean', 'W_812_CLR_IRQ']
