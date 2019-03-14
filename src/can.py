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
from can_ctl import can_command, Rec


Mode_list = ["正常发送","自发自收"]
Index_list = [0,1]
Remote_list = ["数据帧","远程帧"]
Extern_list = ["标准帧","扩展帧"]

DEVICETYPE = 21
DEVICEINDEX = 0

class Can_Ui(QtWidgets.QMainWindow):

    def __init__(self,can_Index = 1, bound = 0):
        super(Can_Ui, self).__init__()
        self.bound = bound
        self.can_Index = can_Index
        self.can_command = can_command()
        self.Rec = Rec()
        self.Rec.trigger.connect(self.update_text)
        self.cnt = 0
        self.font_size = 9

    def StartCAN(self):
        globals()["start" + str(self.can_Index)] = 1
        num = self.can_command.Start(DEVICETYPE,DEVICEINDEX,self.can_Index,self.bound)
        if num == 0:
            self.Rec.run_(DEVICETYPE, DEVICEINDEX, self.can_Index)
            return 1
        elif num == 1:
            QtWidgets.QMessageBox.warning(self, "Error", "OpenCan Error", QtWidgets.QMessageBox.Yes)
            return 0
        elif num == 2:
            QtWidgets.QMessageBox.warning(self, "Error", "SetReferenceCan Error", QtWidgets.QMessageBox.Yes)
            return 0
        elif num == 3:
            QtWidgets.QMessageBox.warning(self, "Error", "InitCan Error", QtWidgets.QMessageBox.Yes)
            return 0
        elif num == 4:
            QtWidgets.QMessageBox.warning(self, "Error", "StartCan Error", QtWidgets.QMessageBox.Yes)
            return 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 733)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        MainWindow.setCentralWidget(self.centralwidget)

        self.setDock_1(MainWindow)
        self.setDock_2(MainWindow)
        MainWindow.tabifyDockWidget(self.dockWidget, self.dockWidget_2)
        self.dockWidget.raise_()

        self.Data = []
        self.SaveAdds = None

        self.threads = MyThread()
        self.threads.trigger.connect(self.update_text)
        self.threads.trigger2.connect(self._pushButtonclick_2)
        self.threads.trigger3.connect(self.send_error)

        self.threads2 = MyThread2()
        self.threads2.trigger.connect(self.update_text)
        self.threads2.trigger2.connect(self._pushButtonclick_4)
        self.threads2.trigger3.connect(self.send_error)

        # self.threads3 = self.Rec
        # self.threads3.trigger.connect(self.update_text)

        # self.Open = self.createAction(MainWindow,"&Open", self.OpenDevices, "Open")
        # self.SetReference = self.createAction(MainWindow,"&SetRef", self.SetReference, "SetReference")
        # self.InitCAN = self.createAction(MainWindow,"&Init", self.InitCAN, "Init")
        self.StartCAN = self.createAction(MainWindow,"&启动", self.StartCAN, "启动")
        self.ResetCAN = self.createAction(MainWindow,"&重启", self.ResetCAN, "重启")
        self.CloseCAN1 = self.createAction(MainWindow,"&关闭", self.CloseCAN1, "关闭")
        self.SaveData = self.createAction(MainWindow,"&保存", self.fileSave, "保存")
        self.clear = self.createAction(MainWindow,"&清空", self.clear_text, "清空")
        self.Font_add = self.createAction(MainWindow,"&字体+", self.Font_add, "字体+")
        self.Font_sub = self.createAction(MainWindow,"&-", self.Font_sub, "-")
        ftoolb = MainWindow.addToolBar("tool")
        self.addActions(ftoolb,(self.StartCAN, self.ResetCAN, self.CloseCAN1, self.SaveData,self.clear,self.Font_add,self.Font_sub))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setDock_1(self, objectname):
        self.dockWidget = QtWidgets.QDockWidget("基本操作", objectname)
        self.dockWidget.setObjectName("dockWidget_2")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(0, 100))
        self.dockWidgetContents.setObjectName("dockWidgetContents_2")

        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_7 = QtWidgets.QLabel(self.dockWidgetContents)

        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.dockWidgetContents)

        self.comboBox = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox_2 = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox_3 = QtWidgets.QComboBox(self.dockWidgetContents)

        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_2 = QtWidgets.QPushButton(self.dockWidgetContents)

        # self.label_8 = QtWidgets.QLabel(self.dockWidgetContents)
        # self.pixelSizeSpinBox = QtWidgets.QSpinBox(self.dockWidgetContents)
        # self.pixelSizeSpinBox.setMinimum(5)
        # self.pixelSizeSpinBox.setMaximum(20)
        # self.pixelSizeSpinBox.setValue(9)

        self.setSite(10, 10, 60, 20, self.label, "发送方式")
        self.setSite(28, 40, 50, 20, self.label_2, "帧类型")
        self.setSite(180, 40, 50, 20, self.label_3, "帧ID")
        self.setSite(310, 40, 50, 20, self.label_4, "数据")
        self.setSite(28, 70, 60, 20, self.label_5, "帧格式")
        self.setSite(180, 70, 70, 20, self.label_6, "发送次数")
        self.setSite(370, 70, 70, 20, self.label_7, "发送间隔")
        self.setSite(220, 40, 70, 20, self.lineEdit, "FFFFFFFF")
        self.setSite(350, 40, 200, 20, self.lineEdit_2, "01 02 03 04 05 06 07 08")
        self.setSite(250, 70, 110, 20, self.lineEdit_3, "1")
        self.setSite(440, 70, 110, 20, self.lineEdit_4, "0")
        self.setSite(80, 10, 90, 20, self.comboBox, Mode_list)
        self.setSite(80, 40, 90, 20, self.comboBox_2, Extern_list)
        self.setSite(80, 70, 90, 20, self.comboBox_3, Remote_list)
        self.setSite(570, 39, 75, 22, self.pushButton, "发送")
        self.setSite(570, 69, 75, 22, self.pushButton_2, "停止")

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.pushButton.clicked.connect(self._pushButtonclick)
        self.pushButton_2.clicked.connect(self._pushButtonclick_2)
        self.pushButton_2.setEnabled(False)
        objectname.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)

    def setDock_2(self, objectname):
        self.dockWidget_2 = QtWidgets.QDockWidget("高级操作", objectname)
        self.dockWidget_2.setObjectName("dockWidget_3")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_3")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_1.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 530, 120))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 530, 200))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 600))
        self.scrollArea.setMaximumSize(QtCore.QSize(530, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_1.addWidget(self.scrollArea)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label_8 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_9 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.comboBox_4 = QtWidgets.QComboBox(self.dockWidgetContents_2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.dockWidgetContents_2)

        self.setCheckBox(4, 10)

        self.setSite(550, 10, 60, 20, self.label_8, "发送方式")
        self.setSite(550, 40, 60, 20, self.label_9, "发送次数")
        self.setSite(550, 70, 60, 20, self.label_10, "发送间隔")
        self.setSite(630, 10, 90, 20, self.comboBox_4, Mode_list)
        self.setSite(630, 40, 90, 20, self.lineEdit_5, "1")
        self.setSite(630, 70, 90, 20, self.lineEdit_6, "0")
        self.setSite(740, 9, 70, 22, self.pushButton_3, "发送")
        self.setSite(740, 39, 70, 22, self.pushButton_4, "停止")
        self.setSite(740, 69, 70, 22, self.pushButton_5, "导入")

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.filename = None
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.clicked.connect(self._pushButtonclick_3)
        self.pushButton_4.clicked.connect(self._pushButtonclick_4)
        self.pushButton_5.clicked.connect(self.fileOpen)
        objectname.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_2)

    def setSite(self,x,y,l,h,object,text = None, num = 10):
        object.setGeometry(QtCore.QRect(x,y,l,h))
        if type(text) == str:
            object.setText(text)
        elif type(text) == list:
            object.addItems(text)
            if num == 10:
                pass
            else:
                object.setCurrentIndex(num)

    def setCheckBox(self, x, y, file_name = "command.txt"):
        self.checkBox_list   = []
        self.comboBox_5_list = []
        self.comboBox_6_list = []
        self.lineEdit_7_list = []
        self.lineEdit_8_list = []
        f = open(file_name)
        lines = f.readlines()
        self.command_cnt = 0
        for line in lines:
            if len(line) < 32:
                continue
            else:
                self.command_cnt += 1
                b = line.upper()
                a = b.strip('\n')
                self.lineEdit_7_list.append(a[0:8])
                self.lineEdit_8_list.append(a[13:36])
                self.comboBox_5_list.append(a[9])
                self.comboBox_6_list.append(a[11])
                self.checkBox_list.append(0)
        for i in range(self.command_cnt):
            globals()['checkBox_5'+str(i)+str(self.can_Index)] = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            globals()['comboBox_5'+str(i)+str(self.can_Index)] = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            globals()['comboBox_6'+str(i)+str(self.can_Index)] = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            globals()['lineEdit_7'+str(i)+str(self.can_Index)] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            globals()['lineEdit_8'+str(i)+str(self.can_Index)] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            checkBox_5 = globals()['checkBox_5'+str(i)+str(self.can_Index)]
            comboBox_5 = globals()['comboBox_5'+str(i)+str(self.can_Index)]
            comboBox_6 = globals()['comboBox_6'+str(i)+str(self.can_Index)]
            lineEdit_7 = globals()['lineEdit_7'+str(i)+str(self.can_Index)]
            lineEdit_8 = globals()['lineEdit_8'+str(i)+str(self.can_Index)]
            self.setSite(x, y + 20 * i, 40, 20,  checkBox_5, str(i))
            self.setSite(x + 40, y + 20 * i, 80, 20, comboBox_5, Remote_list,int(self.comboBox_5_list[i]))
            self.setSite(x + 120, y + 20 * i, 80, 20, comboBox_6, Extern_list,int(self.comboBox_6_list[i]))
            self.setSite(x + 200, y + 20 * i, 80, 20, lineEdit_7, self.lineEdit_7_list[i])
            self.setSite(x + 280, y + 20 * i, 200, 20, lineEdit_8, self.lineEdit_8_list[i])

    def currentDate(self):
        for i in range(self.command_cnt):
            checkBox_5 = globals()['checkBox_5'+str(i)+str(self.can_Index)]
            comboBox_5 = globals()['comboBox_5'+str(i)+str(self.can_Index)]
            comboBox_6 = globals()['comboBox_6'+str(i)+str(self.can_Index)]
            lineEdit_7 = globals()['lineEdit_7'+str(i)+str(self.can_Index)]
            lineEdit_8 = globals()['lineEdit_8'+str(i)+str(self.can_Index)]
            if checkBox_5.isChecked():
                self.checkBox_list[i] = 1
            else:
                self.checkBox_list[i] = 0
            self.comboBox_5_list[i] = comboBox_5.currentIndex()
            self.comboBox_6_list[i] = comboBox_6.currentIndex()
            self.lineEdit_7_list[i] = lineEdit_7.text()
            self.lineEdit_8_list[i] = lineEdit_8.text()

    def setcurrentDate(self):
        for i in range(self.command_cnt):
            lineEdit_7 = globals()['lineEdit_7'+str(i)+str(self.can_Index)]
            lineEdit_8 = globals()['lineEdit_8'+str(i)+str(self.can_Index)]
            lineEdit_7.setText(self.lineEdit_7_list[i])
            lineEdit_8.setText(self.lineEdit_8_list[i])

    def fileOpen(self):
        if not self.okToContinue():
            return
        dir = (os.path.dirname(self.filename)
               if self.filename is not None else ".")
        fname = str(QtWidgets.QFileDialog.getOpenFileName(self,
                "Python Editor - Choose File", dir,
                "command files (*.txt)")[0])
        if fname:
            self.filename = fname
            print(self.filename)
            self.onRestart(self.filename)

    def okToContinue(self):
        reply = QtWidgets.QMessageBox.question(self,
                        "Python Editor - Unsaved Changes",
                        "保存当前指令表?",
                                               QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|
                                               QtWidgets.QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Cancel:
            return False
        elif reply == QtWidgets.QMessageBox.Yes:
            return True
        return True

    def onRestart(self,fname):
        self.scrollArea.close()
        self.scrollArea.deleteLater()
        del self.scrollArea

        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 530, 120))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 530, 200))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 600))
        self.scrollArea.setMaximumSize(QtCore.QSize(530, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_1.addWidget(self.scrollArea)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.setCheckBox(4, 10,fname)

    def fileSave(self):
        if self.SaveAdds is None:
            return self.fileSaveAs()
        fh = None
        print(self.SaveAdds)
        try:
            fh = QtCore.QFile(self.SaveAdds)
            if not fh.open(QtCore.QIODevice.WriteOnly):
                raise IOError(str(fh.errorString()))
            stream = QtCore.QTextStream(fh)
            stream.setCodec("UTF-8")
            stream << ''.join(self.Data)
        except EnvironmentError as e:
            QtWidgets.QMessageBox.warning(self, "Python Editor -- Save Error",
                    "Failed to save {0}: {1}".format(self.SaveAdds, e))
            return False
        finally:
            if fh is not None:
                fh.close()
        return True

    def fileSaveAs(self):
        filename = self.SaveAdds if self.SaveAdds is not None else "."
        filename,filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                "Python Editor -- Save File As", filename,
                "Python files (*.txt)")
        if filename:
            self.SaveAdds = filename
            self.setWindowTitle("Python Editor - {0}".format(
                QtCore.QFileInfo(self.SaveAdds).fileName()))
            return self.fileSave()
        return False

    def _pushButtonclick(self):
        SendType_flag = self.comboBox.currentIndex()
        Extern_flag = self.comboBox_2.currentIndex()
        Remote_flag = self.comboBox_3.currentIndex()
        a = int(self.lineEdit_3.text())
        time_cont = int(self.lineEdit_4.text())/1000
        Data = []
        Data.append(self.str2dec(self.lineEdit_2.text()[0:2]))
        Data.append(self.str2dec(self.lineEdit_2.text()[3:5]))
        Data.append(self.str2dec(self.lineEdit_2.text()[6:8]))
        Data.append(self.str2dec(self.lineEdit_2.text()[9:11]))
        Data.append(self.str2dec(self.lineEdit_2.text()[12:14]))
        Data.append(self.str2dec(self.lineEdit_2.text()[15:17]))
        Data.append(self.str2dec(self.lineEdit_2.text()[18:20]))
        Data.append(self.str2dec(self.lineEdit_2.text()[21:23]))
        x1 = 'None'
        x2 = '发送'
        if Extern_flag == 0:
            ID = self.str2dec(self.lineEdit.text()[4:9]) >> 5
            ID1 = ID << 5
            str_Extern = Extern_list[0]
        elif Extern_flag == 1:
            ID = self.str2dec(self.lineEdit.text()) >> 3
            ID1 = ID << 3
            str_Extern = Extern_list[1]
        else:
            ID1 = None
            ID = None
            str_Extern = None
        if Remote_flag == 0:
            str_Remote = Remote_list[0]
        elif Remote_flag == 1:
            str_Remote = Remote_list[1]
        else:
            str_Remote = None
        ID2 = self.dec2str(ID1, 8)
        ID2 = ID2.upper()
        self.lineEdit.setText(ID2)
        str_data = self.lineEdit_2.text()
        str_data = str_data.upper()
        self.lineEdit_2.setText(str_data)
        message = x2.center(4) + ' ' + ID2 + ' ' + x1.center(12) + ' ' + str_Remote.center(5) + ' ' + str_Extern.center(5) + ' ' + str_data
        if a == 1:
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
        else:
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
        self.threads.run_(DEVICETYPE,DEVICEINDEX,self.can_Index,message,a, time_cont,ID,
                          SendType_flag, Remote_flag, Extern_flag, Data)

    def send_error(self):
        QtWidgets.QMessageBox.warning(self, "Error", "Send Error", QtWidgets.QMessageBox.Yes)
        self.threads.terminate()

    def _pushButtonclick_2(self):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.threads.terminate()

    def _pushButtonclick_3(self):
        self.currentDate()
        message   = []
        ID_list   = []
        Data_list = []
        Remote_flag = []
        Extern_flag   = []
        a = int(self.lineEdit_5.text())
        time_cont = int(self.lineEdit_6.text())/1000
        SendType_flag = self.comboBox_4.currentIndex()
        ID_cont = len(self.checkBox_list)
        for i in range(ID_cont):
            if self.checkBox_list[i] == 1:
                Remote_flag.append(self.comboBox_5_list[i])
                Extern_flag.append(self.comboBox_6_list[i])
                if self.comboBox_6_list[i] == 0:
                    ID = self.str2dec(self.lineEdit_7_list[i][4:9]) >> 5
                    ID1 = ID << 5
                    str_Extern = Extern_list[0]
                elif self.comboBox_6_list[i] == 1:
                    ID = self.str2dec(self.lineEdit_7_list[i]) >> 3
                    ID1 = ID << 3
                    str_Extern = Extern_list[0]
                else:
                    ID = None
                    ID1 = None
                    str_Extern = None
                if self.comboBox_5_list[i] == 0:
                    str_Remote = Remote_list[0]
                elif self.comboBox_5_list[i] == 1:
                    str_Remote = Remote_list[1]
                else:
                    str_Remote = None
                x1 = 'None'
                x2 = '发送'
                ID2 = self.dec2str(ID1, 8)
                ID2 = ID2.upper()
                self.lineEdit.setText(ID2)
                str_data = self.lineEdit_8_list[i]
                str_data = str_data.upper()
                self.lineEdit_2.setText(str_data)
                self.lineEdit_7_list[i] = ID2
                self.lineEdit_8_list[i] = str_data
                self.setcurrentDate()
                message.append(x2.center(4) + ' ' + ID2 + ' ' + x1.center(12) + ' ' + str_Remote.center(5) + ' ' + str_Extern.center(5) + ' ' + str_data)
                ID_list.append(ID)
                Data = []
                Data.append(self.str2dec(self.lineEdit_8_list[i][0:2]))
                Data.append(self.str2dec(self.lineEdit_8_list[i][3:5]))
                Data.append(self.str2dec(self.lineEdit_8_list[i][6:8]))
                Data.append(self.str2dec(self.lineEdit_8_list[i][9:11]))
                Data.append(self.str2dec(self.lineEdit_8_list[i][12:14]))
                Data.append(self.str2dec(self.lineEdit_8_list[i][15:17]))
                Data.append(self.str2dec(self.lineEdit_8_list[i][18:20]))
                Data.append(self.str2dec(self.lineEdit_8_list[i][21:23]))
                Data_list.append(Data)
        if len(message) == 0:
            print('请选择指令')
        else:
            self.threads2.run_(DEVICETYPE,DEVICEINDEX,self.can_Index,message,a, time_cont,ID_list,
                               SendType_flag, Remote_flag, Extern_flag, Data_list)
        if a ==1:
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(False)
        else:
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(True)

    def _pushButtonclick_4(self):
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(False)
        self.threads2.terminate()

    def Font_add(self):
        if self.font_size <= 15:
            self.font_size = self.font_size + 1
        else:
            self.font_size = self.font_size
        font = QtGui.QFont()
        font.setPointSize(self.font_size)
        self.textBrowser.setFont(font)

    def Font_sub(self):
        if self.font_size >= 5:
            self.font_size = self.font_size - 1
        else:
            self.font_size = self.font_size
        font = QtGui.QFont()
        font.setPointSize(self.font_size)
        self.textBrowser.setFont(font)

    def clear_text(self):
        self.cnt = 0
        self.textBrowser.clear()
        self.Data = []
        self.textBrowser.repaint()  # 实时更新显示

    def update_text(self, message):
        self.cnt = self.cnt + 1
        count = str(self.cnt)
        x = count.zfill(6)
        message1 = x + ' ' + message
        self.textBrowser.append(message1)
        self.textBrowser.repaint()    #实时更新显示
        data = message + '\n'
        print(data)
        self.Data.append(data)

    def createAction(self, objectname, text, slot=None, tip=None):
        action = QtWidgets.QAction(text, objectname)
        action.setStatusTip(tip)
        action.triggered.connect(slot)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def CloseCAN(self):
        self.can_command.Close(DEVICETYPE,DEVICEINDEX)
        # self.can_command.Close(DEVICETYPE,DEVICEINDEX)

    def CloseCAN1(self):
        self.can_command.Close(DEVICETYPE,DEVICEINDEX)
        self.can_command.Close(DEVICETYPE,DEVICEINDEX)
        globals()["start" + str(self.can_Index)] = 0
        can_Index = 1 - self.can_Index
        try:
            a = globals()["start" + str(can_Index)]
        except Exception as err:
            a = 0
        if a == 1:
            self.can_command.Start(DEVICETYPE, DEVICEINDEX, can_Index, self.bound)
        else:
            pass
        # self.can_command.ClearBuffer(DEVICETYPE, DEVICEINDEX, self.can_Index)

    def ResetCAN(self):
        self.can_command.Reset(DEVICETYPE,DEVICEINDEX,self.can_Index)

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

class MyThread(QtCore.QThread):
    trigger = pyqtSignal(str)
    trigger2 = pyqtSignal()
    trigger3 = pyqtSignal()

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)
        self.can_command = can_command()

    def run_(self,DEVICETYPE,DEVICEINDEX,can_Index, message=None,a = 1, time_cont = 0.0,ID = 0,
             SendType_flag = 0, Remote_flag = 0, Extern_flag = 0, Data = []):
        self.DEVICETYPE1    = DEVICETYPE
        self.DEVICEINDEX1   = DEVICEINDEX
        self.can_Index1     = can_Index
        self.message1       = message
        self.a1             = a
        self. time_cont1    = time_cont
        self.ID1            = ID
        self.SendType_flag1 = SendType_flag
        self.Remote_flag1   = Remote_flag
        self.Extern_flag1   = Extern_flag
        self.Data1          =  Data
        self.start()

    def run(self):
        if self.a1 == 1:
            if self.can_command.can_send(self.DEVICETYPE1,self.DEVICEINDEX1,self.can_Index1,self.ID1,
                                         self.SendType_flag1, self.Remote_flag1, self.Extern_flag1, self.Data1):
                self.trigger.emit(self.message1)
                self.trigger2.emit()
            else:
                self.trigger3.emit()
        else:
            for i in range(self.a1):
                if self.can_command.can_send(self.DEVICETYPE1,self.DEVICEINDEX1,self.can_Index1,self.ID1,
                                             self.SendType_flag1, self.Remote_flag1, self.Extern_flag1, self.Data1):
                    self.trigger.emit(self.message1)
                    time.sleep(self.time_cont1)
                else:
                    self.trigger3.emit()
                    break
            self.trigger2.emit()

class MyThread2(QtCore.QThread):
    trigger = pyqtSignal(str)
    trigger2 = pyqtSignal()
    trigger3 = pyqtSignal()

    def __init__(self, parent=None):
        super(MyThread2, self).__init__(parent)
        self.can_command = can_command()

    def run_(self,DEVICETYPE,DEVICEINDEX,can_Index, message=None,a = 1, time_cont = 0.0,ID = [],
             SendType_flag = 0, Remote_flag = [], Extern_flag = [], Data = []):
        self.num            = len(ID)
        self.DEVICETYPE2    = DEVICETYPE
        self.DEVICEINDEX2   = DEVICEINDEX
        self.can_Index2     = can_Index
        self.message2       = message
        self.a2             = a
        self. time_cont2    = time_cont
        self.ID2            = ID
        self.SendType_flag2 = SendType_flag
        self.Remote_flag2   = Remote_flag
        self.Extern_flag2   = Extern_flag
        self.Data2          =  Data
        self.start()

    def run(self):
        if self.a2 == 1:
            if self.num == 1:
                ID = self.ID2[0]
                Remote_flag = self.Remote_flag2[0]
                Extern_flag = self.Extern_flag2[0]
                Data = self.Data2[0]
                if self.can_command.can_send(self.DEVICETYPE2, self.DEVICEINDEX2, self.can_Index2, ID,
                                             self.SendType_flag2, Remote_flag, Extern_flag, Data):
                    self.trigger.emit(self.message2[0])
                    self.trigger2.emit()
                else:
                    self.trigger3.emit()
            else:
                for i in range(self.num):
                    ID          = self.ID2[i]
                    Remote_flag = self.Remote_flag2[i]
                    Extern_flag = self.Extern_flag2[i]
                    Data        = self.Data2[i]
                    if self.can_command.can_send(self.DEVICETYPE2,self.DEVICEINDEX2,self.can_Index2,ID,
                                                 self.SendType_flag2,Remote_flag,Extern_flag,Data):
                        self.trigger.emit(self.message2[i])
                        self.trigger2.emit()
                    else:
                        self.trigger3.emit()
                        break
        else:
            for i in range(self.a2):
                if self.num == 1:
                    ID = self.ID2[0]
                    Remote_flag = self.Remote_flag2[0]
                    Extern_flag = self.Extern_flag2[0]
                    Data = self.Data2[0]
                    if self.can_command.can_send(self.DEVICETYPE2, self.DEVICEINDEX2, self.can_Index2, ID,
                                                 self.SendType_flag2, Remote_flag, Extern_flag, Data):
                        self.trigger.emit(self.message2[0])
                        self.trigger2.emit()
                    else:
                        self.trigger3.emit()
                else:
                    for i in range(self.num):
                        ID = self.ID2[i]
                        Remote_flag = self.Remote_flag2[i]
                        Extern_flag = self.Extern_flag2[i]
                        Data = self.Data2[i]
                        if self.can_command.can_send(self.DEVICETYPE2, self.DEVICEINDEX2, self.can_Index2, ID,
                                                     self.SendType_flag2, Remote_flag, Extern_flag, Data):
                            self.trigger.emit(self.message2[i])
                            self.trigger2.emit()
                        else:
                            self.trigger3.emit()
                            break
            self.trigger2.emit()

class MainWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        self.can_command = can_command()
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.can_command.Close()
            self.can_command.Close()
            self.can_command.Close()
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    MainWindow = MainWindow()
    ui = Can_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())