from ctypes import windll
import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

dll = windll.LoadLibrary('ControlCAN.dll')
Remote_list = ["数据帧","远程帧"]
Extern_list = ["标准帧","扩展帧"]

class can_command():

    def Start(self,DEVICETYPE,DEVICEINDEX,can_Index,bound):
        if OpenDevices(DEVICETYPE,DEVICEINDEX,can_Index):
            if SetReference(DEVICETYPE,DEVICEINDEX,can_Index,0,bound):
                if InitCAN(DEVICETYPE,DEVICEINDEX,can_Index,0,0,0,0,0,0,0):
                    if StartCAN(DEVICETYPE,DEVICEINDEX,can_Index):
                        print(DEVICETYPE,DEVICEINDEX,can_Index)
                        print("start")
                        return 0
                    else:
                        return 4
                else:
                    return 3
            else:
                return 2
        else:
            return 1

    def can_send(self,DEVICETYPE,DEVICEINDEX,can_Index,ID,SendType_flag,Remote_flag,Extern_flag,Data):
        return Transmit(DEVICETYPE,DEVICEINDEX,can_Index,ID,SendType_flag,Remote_flag,Extern_flag,Data,1)

    def Close(self,DEVICETYPE,DEVICEINDEX):
        return CloseCAN(DEVICETYPE,DEVICEINDEX)

    def Reset(self,DEVICETYPE,DEVICEINDEX,can_Index):
        return ResetCAN(DEVICETYPE,DEVICEINDEX,can_Index)

    def Clear(self,EVICETYPE, DEVICEINDEX, CANINDEX):
        return ClearBuffer(EVICETYPE, DEVICEINDEX, CANINDEX)

class Rec(QtCore.QThread):
    trigger  = pyqtSignal(str)
    trigger2 = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Rec, self).__init__(parent)

    def run_(self, DEVICETYPE = 21, DEVICEINDEX = 0, can_Index= 1):
        self.can_Index  = can_Index
        self.DEVICETYPE = DEVICETYPE
        self.DEVICEINDEX= DEVICEINDEX
        self.start()

    def run(self):
        while 1:
            Rec_Data = Receive(self.DEVICETYPE, self.DEVICEINDEX, self.can_Index)
            for i in Rec_Data:
                if type(i) == int:
                    pass
                else:
                    ID_temp = i[0]
                    TimeFlag = i[1]
                    TimeStamp = i[2]
                    RemoteFlag = i[3]
                    ExternFlag = i[4]
                    data_len = i[5]
                    Data = []
                    for j in range(data_len):
                        Data.append(self.dec2str(i[6 + j],2))
                    if ExternFlag == 0:
                        ID = ID_temp << 5
                        ID = self.dec2str(ID,8)
                        str_Extern = Extern_list[0]
                    else:
                        ID = ID_temp << 3
                        ID = self.dec2str(ID, 8)
                        str_Extern = Extern_list[1]
                    if RemoteFlag == 0:
                        str_Remote = Remote_list[0]
                    else:
                        str_Remote = Remote_list[1]
                    TimeStamp = str(TimeStamp)
                    TimeStamp = TimeStamp.center(12)
                    a = '接收'
                    string = a.center(4) + ' ' + \
                             ID + ' ' + \
                             TimeStamp + ' ' + \
                             str_Remote.center(5) + ' ' + \
                             str_Extern.center(5) + ' ' + \
                             " ".join(Data)
                    data_list = []
                    data_list.append(ID)
                    data_list.append(Data)
                    self.trigger.emit(string)
                    self.trigger2.emit(data_list)

    def dec2str(self,Data,num):
        temp = hex(Data)
        str = temp[2:]
        if len(str) < num:
            str = str.zfill(num)
            str = str.upper()
            return str
        else:
            str.upper()
            return str

class InitConfig1(ctypes.Structure):
    _fields_ = [("AccCode", ctypes.c_ulong),
                ("AccMask", ctypes.c_ulong),
                ("Reserved", ctypes.c_ulong),
                ("Filter", ctypes.c_ubyte),
                ("Timing0", ctypes.c_ubyte),
                ("Timing1", ctypes.c_ubyte),
                ("Mode", ctypes.c_ubyte)]

class Frames1(ctypes.Structure):
    _fields_ = [("ID", ctypes.c_uint),
                ("TimeStamp", ctypes.c_uint),
                ("TimeFlag", ctypes.c_ubyte),
                ("SendType", ctypes.c_ubyte),
                ("RemoteFlag", ctypes.c_ubyte),
                ("ExternFlag", ctypes.c_ubyte),
                ("DataLen", ctypes.c_ubyte),
                ("Data", ctypes.c_ubyte * 8),
                ("Reserved", ctypes.c_ubyte * 3)]

class filterRecord1(ctypes.Structure):
    _fields_ = [("ExtFrame", ctypes.c_ulong),
                ("Start", ctypes.c_ulong),
                ("End", ctypes.c_ulong)]

class Errr_Info1(ctypes.Structure):
    _fields_ = [("ErrCode", ctypes.c_ulong),
                ("Passive_ErrData", ctypes.c_ubyte * 3),
                ("ArLost_ErrData", ctypes.c_ubyte)]

def OpenDevices(DEVICETYPE,DEVICEINDEX,CANINDEX):
    return dll.VCI_OpenDevice(DEVICETYPE,DEVICEINDEX,CANINDEX)

def SetReference(DEVICETYPE, DEVICEINDEX, CANINDEX, RefType = 0, baud = 0, Filter = 0, FilterStart = 0, FilterEnd = 0, SendTimeout = 0):
    if baud == 0:
        bauds = (ctypes.c_ulong)(393223)
    else:
        bauds  = (ctypes.c_ulong)(393223)
    if RefType == 0:
        return dll.VCI_SetReference(DEVICETYPE, DEVICEINDEX, CANINDEX, RefType, ctypes.byref(bauds)) #设置波特率
    elif RefType == 1:
        filterRecord = filterRecord1()
        filterRecord.ExtFrame = (ctypes.c_ulong)(Filter)
        filterRecord.Start = (ctypes.c_ulong)(FilterStart)
        filterRecord.End = (ctypes.c_ulong)(FilterEnd)
        return dll.VCI_SetReference(DEVICETYPE, DEVICEINDEX, CANINDEX, RefType, ctypes.byref(filterRecord)) #设置滤波范围
    elif RefType == 2:
        return dll.VCI_SetReference(DEVICETYPE, DEVICEINDEX, CANINDEX, RefType, None) # 0 设置滤波失败 1 设置滤波成功
    elif RefType == 3:
        return dll.VCI_SetReference(DEVICETYPE, DEVICEINDEX, CANINDEX, RefType, SendTimeout) #设置发送超时时间

def InitCAN(DEVICETYPE, DEVICEINDEX, CANINDEX, AccCode,AccMask,Reserved,Filter,Timing0,Timing1,Mode):
    InitConfig = InitConfig1()
    InitConfig.AccCode = (ctypes.c_ulong)(AccCode)
    InitConfig.AccMask = (ctypes.c_ulong)(AccMask)
    InitConfig.Reserved = (ctypes.c_ulong)(Reserved)
    InitConfig.Filter = (ctypes.c_ubyte)(Filter)
    InitConfig.Timing0 = (ctypes.c_ubyte)(Timing0)
    InitConfig.Timing1 = (ctypes.c_ubyte)(Timing1)
    InitConfig.Mode = (ctypes.c_ubyte)(Mode)
    return dll.VCI_InitCAN(DEVICETYPE, DEVICEINDEX, CANINDEX, ctypes.byref(InitConfig))

def StartCAN(DEVICETYPE, DEVICEINDEX, CANINDEX):
    return dll.VCI_StartCAN(DEVICETYPE, DEVICEINDEX, CANINDEX)

def ResetCAN(EVICETYPE, DEVICEINDEX, CANINDEX):
    return dll.VCI_ResetCAN(EVICETYPE, DEVICEINDEX, CANINDEX)

def ClearBuffer(EVICETYPE, DEVICEINDEX, CANINDEX):
    return dll.VCI_ClearBuffer(EVICETYPE, DEVICEINDEX, CANINDEX)

def CloseCAN(DEVICETYPE, DEVICEINDEX):
    return dll.VCI_CloseDevice(DEVICETYPE, DEVICEINDEX)

def Transmit(DEVICETYPE, DEVICEINDEX, CANINDEX, ID, SendType, RemoteFlag, ExternFlag, Data,  SendNums):
    Frames = Frames1()
    Frames.ID = (ctypes.c_uint)(ID)  # 0x4402440
    Frames.TimeStamp = (ctypes.c_uint)(0)
    Frames.TimeFlag = (ctypes.c_ubyte)(0)
    Frames.DataLen = (ctypes.c_ubyte)(8)
    x = (ctypes.c_ubyte * 3)()
    x[0] = 0
    x[1] = 0
    x[2] = 0
    Frames.Reserved = x
    Frames.SendNums = (ctypes.c_ubyte)(SendNums)
    Frames.SendType = (ctypes.c_ubyte)(SendType)
    Frames.RemoteFlag = (ctypes.c_ubyte)(RemoteFlag)  # 0数据帧 1远程帧
    Frames.ExternFlag = (ctypes.c_ubyte)(ExternFlag)  # 0标准帧 1扩展帧
    DataX = (ctypes.c_ubyte * 8)()
    DataX[0] = (Data[0])
    DataX[1] = (Data[1])
    DataX[2] = (Data[2])
    DataX[3] = (Data[3])
    DataX[4] = (Data[4])
    DataX[5] = (Data[5])
    DataX[6] = (Data[6])
    DataX[7] = (Data[7])
    Frames.Data = DataX
    return dll.VCI_Transmit(DEVICETYPE, DEVICEINDEX, CANINDEX, ctypes.byref(Frames), SendNums)

def Receive(DEVICETYPE, DEVICEINDEX, CANINDEX):
    Framinfo = (Frames1 * 50)()
    len = dll.VCI_Receive(DEVICETYPE, DEVICEINDEX, CANINDEX, ctypes.byref(Framinfo), 50, 200)
    Rec_Data = []
    Rec_Data_buf = []
    Errr_Info = Errr_Info1()
    Errr_Data = []
    if len <= 0:
        dll.VCI_ReadErrInfo(DEVICETYPE, DEVICEINDEX, CANINDEX, ctypes.byref(Errr_Info))
        Errr_Data.append(Errr_Info.ErrCode)
        Errr_Data.append(Errr_Info.Passive_ErrData[0])
        Errr_Data.append(Errr_Info.Passive_ErrData[1])
        Errr_Data.append(Errr_Info.Passive_ErrData[2])
        Errr_Data.append(Errr_Info.ArLost_ErrData)
        return Errr_Data
    else:
        for i in range(len):
            Rec_Data_buf.append(Framinfo[i].ID)
            Rec_Data_buf.append(Framinfo[i].TimeFlag)
            Rec_Data_buf.append(Framinfo[i].TimeStamp)
            Rec_Data_buf.append(Framinfo[i].RemoteFlag)
            Rec_Data_buf.append(Framinfo[i].ExternFlag)
            Rec_Data_buf.append(Framinfo[i].DataLen)
            data_len = Framinfo[i].DataLen
            for j in range(data_len):
                Rec_Data_buf.append(Framinfo[i].Data[j])
            Rec_Data.append(Rec_Data_buf)
            print(Framinfo[i].TimeStamp)
        return Rec_Data