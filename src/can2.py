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
import can_ctl

Mode_list = ["正常发送","自发自收"]
Index_list = [0,1]
Remote_list = ["数据帧","远程帧"]
Extern_list = ["标准帧","扩展帧"]

DEVICETYPE = 21
DEVICEINDEX = 0

class Can_Ui(QtWidgets.QMainWindow):

    def __init__(self,can_Index = 0, bound = 0):
        super(Can_Ui,self).__init__()
        self.bound = bound
        self.can_Index = can_Index

    def initC(self, num=None, can_Index = None, bound = None):
        if num == 0:
            if can_ctl.OpenDevices(DEVICETYPE,DEVICEINDEX,can_Index) == 1:
                return 1
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "OpenCan Error", QtWidgets.QMessageBox.Yes)
                return 0
        elif num == 1:
            if can_ctl.SetReference(DEVICETYPE,DEVICEINDEX,can_Index,0,bound) == 1:
                return 1
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "SetReferenceCan Error", QtWidgets.QMessageBox.Yes)
                return 0
        elif num == 2:
            if can_ctl.InitCAN(DEVICETYPE, DEVICEINDEX, can_Index, 0,0,0,0,0,0,0) == 1:
                return 1
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "InitCan Error", QtWidgets.QMessageBox.Yes)
                return 0
        elif num == 3:
            if can_ctl.StartCAN(DEVICETYPE,DEVICEINDEX,can_Index) == 1:
                return 1
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "StartCan Error", QtWidgets.QMessageBox.Yes)
                return 0

    def OpenDevices(self):
        if self.initC(0,self.can_Index, self.bound):
            if self.initC(1, self.can_Index, self.bound):
                if self.initC(2, self.can_Index, self.bound):
                    pass
                else:
                    pass
            else:
                pass
        else:
            pass
    # def SetReference(self):
    #     self.init(1,0,234)
    # def InitCAN(self):
    #     self.init(2,0,234)
    def StartCAN(self):
        if self.initC(3,self.can_Index,self.bound):
            self.threads3.run_(self.can_Index)

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

        self.threads2 = MyThread2()
        self.threads2.trigger.connect(self.update_text)
        self.threads2.trigger2.connect(self._pushButtonclick_4)

        self.threads3 = Rec()
        self.threads3.trigger3.connect(self.update_text)

        self.Open = self.createAction(MainWindow,"&Open", self.OpenDevices, "Open")
        # self.SetReference = self.createAction(MainWindow,"&SetRef", self.SetReference, "SetReference")
        # self.InitCAN = self.createAction(MainWindow,"&Init", self.InitCAN, "Init")
        self.StartCAN = self.createAction(MainWindow,"&Start", self.StartCAN, "Start")
        self.SaveData = self.createAction(MainWindow,"&SaveData", self.fileSave, "SaveData")
        ftoolb = MainWindow.addToolBar("tool")
        self.addActions(ftoolb,(self.Open, self.StartCAN, self.SaveData))

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

    def setSite(self,x,y,l,h,object,text = None):
        object.setGeometry(QtCore.QRect(x,y,l,h))
        if type(text) == str:
            object.setText(text)
        elif type(text) == list:
            object.addItems(text)

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

    def setCheckBox(self, x, y, file_name = "command.txt"):
        self.checkBox_list1   = []
        self.comboBox_5_list1 = []
        self.comboBox_6_list1 = []
        self.lineEdit_list1   = []
        self.lineEdit_4_list1 = []
        f = open(file_name)
        lines = f.readlines()
        num = 0
        for line in lines:
            if len(line) < 32:
                continue
            else:
                num += 1
                b = line.upper()
                a = b.strip('\n')
                self.lineEdit_list1.append(a[0:8])
                self.lineEdit_4_list1.append(a[9:32])
        for i in range(num):
            self.checkBox_5   = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.comboBox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            self.comboBox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
            self.lineEdit_7   = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.setSite(x, y + 20 * i, 40, 20, self.checkBox_5, str(i))
            self.setSite(x + 40, y + 20 * i, 80, 20, self.comboBox_5, Remote_list)
            self.setSite(x + 120, y + 20 * i, 80, 20, self.comboBox_6, Extern_list)
            self.setSite(x + 200, y + 20 * i, 80, 20, self.lineEdit_7, self.lineEdit_list1[i])
            self.setSite(x + 280, y + 20 * i, 200, 20, self.lineEdit_8, self.lineEdit_4_list1[i])
            self.checkBox_list1.append(self.checkBox_5)
            self.comboBox_5_list1.append(self.comboBox_5)
            self.comboBox_6_list1.append(self.comboBox_6)

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
        message = ""
        Data = []
        Data.append(self.str2dec(self.lineEdit_2.text()[0:2]))
        Data.append(self.str2dec(self.lineEdit_2.text()[3:5]))
        Data.append(self.str2dec(self.lineEdit_2.text()[6:8]))
        Data.append(self.str2dec(self.lineEdit_2.text()[9:11]))
        Data.append(self.str2dec(self.lineEdit_2.text()[12:14]))
        Data.append(self.str2dec(self.lineEdit_2.text()[15:17]))
        Data.append(self.str2dec(self.lineEdit_2.text()[18:20]))
        Data.append(self.str2dec(self.lineEdit_2.text()[21:23]))
        x = 1
        if Extern_flag == 0:
            message = self.lineEdit.text() + " " + self.lineEdit_2.text()
            ID = self.str2dec(self.lineEdit.text()[4:9]) >> 5
            x = can_ctl.Transmit(DEVICETYPE,DEVICEINDEX,self.can_Index,ID,SendType_flag,Remote_flag,Extern_flag,Data,1)
        elif Extern_flag == 1:
            message = self.lineEdit.text() + " " + self.lineEdit_2.text()
            ID = self.str2dec(self.lineEdit.text()) >> 3
            x = can_ctl.Transmit(DEVICETYPE, DEVICEINDEX, self.can_Index, ID, SendType_flag, Remote_flag, Extern_flag, Data, 1)
        if x == 0:
            QtWidgets.QMessageBox.warning(self, "Error", "Send Error", QtWidgets.QMessageBox.Yes)
        else:
            if a == 1:
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(False)
            else:
                self.pushButton.setEnabled(False)
                self.pushButton_2.setEnabled(True)
            self.threads.run_(message, a, time_cont)
        # test code
        # if a == 1:
        #     self.pushButton.setEnabled(True)
        #     self.pushButton_2.setEnabled(False)
        # else:
        #     self.pushButton.setEnabled(False)
        #     self.pushButton_2.setEnabled(True)
        # self.threads.run_(message, a, time_cont)

    def _pushButtonclick_2(self):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.threads.terminate()

    def _pushButtonclick_3(self):
        message = []
        a = int(self.lineEdit_5.text())
        time_cont = int(self.lineEdit_6.text())/1000
        ID_cont = len(self.checkBox_list1)
        for i in range(ID_cont):
            if self.checkBox_list1[i].isChecked():
                message.append(self.lineEdit_list1[i].text() + " " + self.lineEdit_4_list1[i].text())
        if len(message) == 0:
            print('请选择指令')
        else:
            self.threads2.run_(message, a, time_cont)
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

    def update_text(self, message):
        self.textBrowser.append(message)
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

class Rec(QtCore.QThread):
    trigger3 = pyqtSignal(str)
    # trigger4 = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Rec, self).__init__(parent)

    def run_(self, can_Index=None):
        self.can_Index = can_Index
        # self.Rec_Data = can_ctl.Receive(DEVICETYPE,DEVICEINDEX,can_Index)
        self.start()

    def run(self):
        while 1:
            Rec_Data = can_ctl.Receive(DEVICETYPE, DEVICEINDEX, self.can_Index)
            for i in Rec_Data:
                # self.trigger4.emit(i)
                cnt = 0
                message = []
                if type(i) == int:
                    pass
                else:
                    for s in i:
                        if 0< cnt < 5:
                            continue
                        else:
                            message.append(str(s))
                            message.append(" ")
                            string = " ".join(message)
                    self.trigger3.emit(string)

class MyThread(QtCore.QThread):
    trigger = pyqtSignal(str)
    trigger2 = pyqtSignal()

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def run_(self, message=None, a=None, time_cont=None):
        self.message = message
        self.a = a
        self.time_cont = time_cont
        self.start()

    def run(self):
        if self.a == 1:
            self.trigger.emit(self.message)
        else:
            for i in range(self.a):
                self.trigger.emit(self.message)
                time.sleep(self.time_cont)
            self.trigger2.emit()

class MyThread2(QtCore.QThread):
    trigger = pyqtSignal(str)
    trigger2 = pyqtSignal()

    def __init__(self, parent=None):
        super(MyThread2, self).__init__(parent)

    def run_(self, message=None, a=None, time_cont=None):
        self.message = message
        self.a = a
        self.time_cont = time_cont
        self.start()

    def run(self):
        if len(self.message) == 1:
            for y in range(self.a):
                self.trigger.emit(self.message[0])
                time.sleep(self.time_cont)
            self.trigger2.emit()
        else:
            for y in range(self.a):
                for x in range(len(self.message)):
                    message_cont = self.message[x]
                    self.trigger.emit(message_cont)
                    time.sleep(self.time_cont)
            self.trigger2.emit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Can_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
