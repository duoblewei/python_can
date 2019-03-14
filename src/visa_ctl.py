# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hhhhh.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import sys
import os
import time
from visa_command import X_visa
from can_ctl import can_command, Rec

done = 0
voltage = 0
current = 0
D_AGC = 0
A_AGC = 0
power = 0
temperature1 = 0
temperature2 = 0


class connect_can(QtCore.QThread):
    def __init__(self):
        super(connect_can,self).__init__()
        self.can_command = can_command()
        self.DEVICETYPE = 21
        self.DEVICEINDEX = 0
        self.can_Index = 0
        self.ID = 71312448
        self.SendType_flag = 0
        self.Remote_flag = 0
        self.Extern_flag = 1
        self.Data = [1,2,3,4,5,6,7,8]

    def run_(self):
        self.start()

    def run(self):
        while 1:
            try :
                self.can_command.can_send(self.DEVICETYPE, self.DEVICEINDEX, self.can_Index,
                                  self.ID,self.SendType_flag, self.Remote_flag, self.Extern_flag, self.Data)
            except EnvironmentError as e:
                return e
            time.sleep(1)
            if done == 1:
                break
            else:
                pass

class get_data():

    def __init__(self):
        super(get_data, self).__init__()
        self.Rec = Rec()
        self.Rec.trigger2.connect(self.read_data)
        self.D_AGC = 0
        self.A_AGC = 0
        self.lock1 = 0
        self.lock2 = 0
        self.power = 0
        self.voltage = 0
        self.current = 0

    def read_data(self,data_list):
        ID = data_list[0]
        data = data_list[1]
        if ID == '4501':
            if len(data) == 8:
                self.D_AGC = data[0]
                self.A_AGC = data[1]
                self.power = data[2]
                self.voltage = data[3]
                self.current = data[4]
                self.temperature1 = data[5]
                self.temperature2 = data[6]
                state = bin(self.str2dec(data[7]))[22:]
                self.lock1 = state[0]
                self.lock2 = state[2]

    def trans_data(self):
        return (self.D_AGC,self.A_AGC,self.power,self.voltage,self.current,self.lock1,self.lock2)

    def str2dec(self, data_str):
        data = 0
        l = len(data_str)
        for x in range(l):
            if ord(data_str[l - x - 1]) < 65:
                data = data + int(data_str[l - x - 1]) * 16 ** x
            elif 64 < ord(data_str[l - x - 1]) < 71:
                data = data + (ord(data_str[l - x - 1]) - 55) * 16 ** x
            elif 96 < ord(data_str[l - x - 1]) < 103:
                data = data + (ord(data_str[l - x - 1]) - 87) * 16 ** x
        return data

class sens():
    trigger = pyqtSignal(str)
    def __init__(self,FREQ):
        super(sens,self).__init__()
        self.data = get_data()
        (self.lock1, self.lock2) = self.data.trans_data()[5:7]
        self.LEVE = 0
        self.LEVE_c = -115
        self.FREQ = FREQ
        self.visa = X_visa()
        self.cnt = 0
        self.s = s()

    def t_data(self,data,x,y):
        self.trigger.emit(str(data,x,y))

    def sens_t(self,num = 0):
        if num == 0:
            self.s.switch(1,0)
            self.test_run(0)
            self.t_data(self.LEVE,1,2)
            self.s.switch(0,1)
            self.test_run(0)
            self.t_data(self.LEVE,2,2)
            self.s.switch(0,0)
            self.test_run(0)
            self.t_data(self.LEVE,3,2)
        elif num == 1:
            self.s.switch(1, 0)
            self.test_run(1)
            self.t_data(self.LEVE,1,4)
            self.s.switch(0, 1)
            self.test_run(1)
            self.t_data(self.LEVE,2,4)
            self.s.switch(0, 0)
            self.test_run(1)
            self.t_data(self.LEVE,3,4)
        elif num == 3:
            self.s.switch(1, 0)
            self.test_run(0)
            self.t_data(self.LEVE, 1, 2)
            self.test_run(1)
            self.t_data(self.LEVE, 1, 4)
            self.s.switch(0, 1)
            self.test_run(0)
            self.t_data(self.LEVE, 2, 2)
            self.test_run(1)
            self.t_data(self.LEVE, 2, 4)
            self.s.switch(0, 0)
            self.test_run(0)
            self.t_data(self.LEVE, 3, 2)
            self.test_run(1)
            self.t_data(self.LEVE, 3, 4)
        else:
            pass
            return 0

    def test_run(self,num = 0):
        self.visa.w_FREQ(self.FREQ)
        self.visa.output(1)
        if num == 1:
            self.visa.w_MFREQ(1,8)
            self.visa.modulation(1,1)
        while self.LEVE_c < -90:
            self.visa.w_LEVE(self.LEVE_c)
            if self.l1():
                if self.l2():
                    self.LEVE = self.LEVE_c
                    break
                else:
                    self.LEVE_c = self.LEVE_c + 1
            else:
                self.LEVE_c = self.LEVE_c + 1
        if self.LEVE_c < -90:
            return 1
        else:
            return 0

    def l1(self):
        self.cnt = 0
        while 1:
            if self.lock1 == 0:
                self.cnt = self.cnt + 1
            else:
                self.cnt = 0
                break
            if self.cnt == 9:
                break
            else:
                pass
            time.sleep(1)
        if self.cnt == 0:
            return 1
        else:
            return 0

    def l2(self):
        self.cnt = 0
        while 1:
            if self.lock1 == 1:
                self.cnt = self.cnt + 1
            else:
                self.cnt = 0
                break
            if self.cnt == 9:
                break
            else:
                pass
            time.sleep(1)
        if self.cnt == 0:
            return 0
        else:
            return 1

class s():
    def __init__(self):
        super(s, self).__init__()
        self.can_command = can_command()
        self.DEVICETYPE = 21
        self.DEVICEINDEX = 0
        self.can_Index = 1
        self.ID = '22012200'
        self.ID = self.str2dec(self.ID) >> 3
        self.SendType_flag = 0
        self.Remote_flag = 0
        self.Extern_flag = 1
        self.Data1 = ['0A', '03', '03', '03', 'AA', 'AA', 'AA', 'AA']
        self.Data2 = ['0A', '04', '04', '04', 'AA', 'AA', 'AA', 'AA']
        self.Data3 = ['0A', '83', '83', '83', 'AA', 'AA', 'AA', 'AA']
        self.Data4 = ['0A', '84', '84', '84', 'AA', 'AA', 'AA', 'AA']

    def switch(self,x,y):
        if x == 0:
            Data = []
            for i in range(8):
                Data.append(self.str2dec(self.Data2[i]))
            self.can_command.can_send(self.DEVICETYPE, self.DEVICEINDEX, self.can_Index, self.ID,
                                      self.SendType_flag, self.Remote_flag, self.Extern_flag, Data)
        elif x == 1:
            Data = []
            for i in range(8):
                Data.append(self.str2dec(self.Data1[i]))
            self.can_command.can_send(self.DEVICETYPE, self.DEVICEINDEX, self.can_Index, self.ID,
                                      self.SendType_flag, self.Remote_flag, self.Extern_flag, Data)
        if y == 0:
            Data = []
            for i in range(8):
                Data.append(self.str2dec(self.Data4[i]))
            self.can_command.can_send(self.DEVICETYPE, self.DEVICEINDEX, self.can_Index, self.ID,
                                      self.SendType_flag, self.Remote_flag, self.Extern_flag, Data)
        elif y == 1:
            Data = []
            for i in range(8):
                Data.append(self.str2dec(self.Data3[i]))
            self.can_command.can_send(self.DEVICETYPE, self.DEVICEINDEX, self.can_Index, self.ID,
                                      self.SendType_flag, self.Remote_flag, self.Extern_flag, Data)

    def str2dec(self,data_str):
        data = 0
        l = len(data_str)
        for x in range(l):
            if ord(data_str[l - x - 1]) < 65:
                data = data + int(data_str[l - x - 1]) * 16**x
            elif 64< ord(data_str[l - x - 1]) < 71:
                data = data + (ord(data_str[l - x - 1]) - 55) * 16**x
            elif 96< ord(data_str[l - x - 1]) < 103:
                data = data + (ord(data_str[l - x - 1]) - 87) * 16**x
        return data