# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hhhhh.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import sys
import os
import time
from visa_ctl import connect_can, sens
from visa_command import X_visa

sate_num = ['选择频点','07','08']

class auto_ui(object):

    def __init__(self):
        super(auto_ui, self).__init__()
        self.flag = 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 733)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.add_tab()
        self.dock_ui(MainWindow)

        self.pushButton_1.clicked.connect(self.sens_test)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def dock_ui(self,objectname):
        self.dockWidget = QtWidgets.QDockWidget(objectname)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        # self.dockWidgetContents.setMinimumSize(QtCore.QSize(0, 125))
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setMaximumHeight(150)
        self.dockWidget.setMinimumHeight(150)

        self.label_1  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_4  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_5  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_6  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_7  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_8  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_9  = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_11 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_12 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_14 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_15 = QtWidgets.QLabel(self.dockWidgetContents)

        self.pushButton_1  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_2  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_3  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_4  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_5  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_6  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_7  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_8  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_9  = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_10 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_11 = QtWidgets.QPushButton(self.dockWidgetContents)

        self.progressBar = QtWidgets.QProgressBar(self.dockWidgetContents)

        self.checkBox_1 = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.checkBox_2 = QtWidgets.QCheckBox(self.dockWidgetContents)

        self.comboBox   = QtWidgets.QComboBox(self.dockWidgetContents)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dockWidgetContents)

        self.radioButton_1 = QtWidgets.QRadioButton(self.dockWidgetContents)
        self.radioButton_2 = QtWidgets.QRadioButton(self.dockWidgetContents)

        self.setSite(70, 10, 90, 20, self.comboBox, sate_num)
        self.setSite(190, 10, 30, 20, self.label_1, "上行")
        self.setSite(225, 10, 100, 20, self.lineEdit_1, "输入上行",1)
        self.setSite(330, 10, 25, 20, self.label_2, "MHz")
        self.setSite(380, 10, 30, 20, self.label_3, "下行")
        self.setSite(415, 10, 100, 20, self.lineEdit_2, "输入下行",1)
        self.setSite(520, 10, 25, 20, self.label_4, "MHz")
        self.setSite(560, 10, 55, 20, self.label_15, "Channel")
        self.setSite(630, 10, 45, 20, self.radioButton_1, "05")
        self.setSite(680, 10, 45, 20, self.radioButton_2, "06")

        self.setSite(15, 40, 80, 20, self.label_5, "载波灵敏度",1)
        self.setSite(95, 38, 80, 24, self.pushButton_1, "开始")
        self.setSite(200, 40, 100, 20, self.checkBox_1, "遥控灵敏度")
        self.setSite(300, 38, 80, 24, self.pushButton_2, "开始")
        self.setSite(405, 40, 80, 20, self.label_6, "扫描灵敏度",1)
        self.setSite(485, 38, 80, 24, self.pushButton_3, "开始")
        self.setSite(590, 40, 30, 20, self.label_7, "进度",1)
        self.setSite(625, 38, 118, 24, self.progressBar,num = 0)

        self.setSite(15, 70, 80, 20, self.label_8, "相干转发比",1)
        self.setSite(95, 68, 80, 24, self.pushButton_4, "开始")
        self.setSite(200, 70, 100, 20, self.checkBox_2, "转发测距音")
        self.setSite(300, 68, 80, 24, self.pushButton_5, "开始")
        self.setSite(405, 70, 80, 20, self.label_9, "AGC曲线",1)
        self.setSite(485, 68, 80, 24, self.pushButton_6, "开始")
        self.setSite(590, 70, 30, 20, self.label_10, "功率",1)
        self.setSite(625, 68, 80, 24, self.pushButton_7, "开始")

        self.setSite(15, 100, 80, 20, self.label_11, "CAN",1)
        self.setSite(95, 98, 80, 24, self.pushButton_8, "连接")
        self.setSite(235, 100, 50, 20, self.label_12, "信号源",1)
        self.setSite(300, 98, 80, 24, self.pushButton_9, "连接")
        self.setSite(405, 100, 80, 20, self.label_13, "频谱仪",1)
        self.setSite(485, 98, 80, 24, self.pushButton_10, "连接")
        self.setSite(580, 100, 45, 20, self.label_14, "功率计",1)
        self.setSite(625, 98, 80, 24, self.pushButton_11, "连接")

        self.dockWidget.setWidget(self.dockWidgetContents)
        objectname.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)

    def setSite(self,x,y,l,h,object,text = None, num = 10):
        object.setGeometry(QtCore.QRect(x,y,l,h))
        if type(text) == str:
            object.setText(text)
            if num == 1:
                object.setAlignment(QtCore.Qt.AlignCenter)
            else:
                pass
        elif type(text) == list:
            object.addItems(text)
            if num == 10:
                pass
            else:
                object.setCurrentIndex(num)
        elif text == None:
            object.setProperty("value", num)

    def add_tab(self):
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        # self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # self.tableView = QtWidgets.QTableView(self.tab)
        # self.tableView.setObjectName("tableView")
        # self.horizontalLayout_5.addWidget(self.tableView)
        if self.flag == 0:
            name = 'test'
            self.test_tab(self.tab)
        elif 0 < self.flag < 4:
            name = '灵敏度'
            self.sensitivity(self.tab)
        elif self.flag == 4:
            name = '调制度'
            self.modulation(self.tab)
        elif self.flag == 5:
            name = '转发比'
        elif self.flag == 6:
            name = 'AGC曲线'
            self.AGC(self.tab)
        else:
            name = 'test'
        self.tabWidget.addTab(self.tab, name)

    def test_tab(self,objectname):
        horizontalLayout = QtWidgets.QHBoxLayout(objectname)
        horizontalLayout.setObjectName("horizontalLayout")
        label = QtWidgets.QLabel(objectname)
        label.setObjectName("label")
        horizontalLayout.addWidget(label)
        label.setText('请选择测试项')
        font = QtGui.QFont()
        font.setPointSize(14)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)

    def sensitivity(self,objectname):
        horizontalLayout = QtWidgets.QHBoxLayout(objectname)
        horizontalLayout.setObjectName("horizontalLayout")
        tableView = QtWidgets.QTableView(objectname)
        tableView.setObjectName("tableView")
        self.myModel = QtGui.QStandardItemModel(objectname)
        horizontalLayout.addWidget(tableView)

        self.model_s = QtGui.QStandardItemModel(tableView)

        self.model_s.setRowCount(10)
        self.model_s.setColumnCount(6)
        tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
        self.model_s.setHorizontalHeaderLabels(['表头','状态','载波','载波','副载波','副载波'])
        self.model_s.setItem(0, 2, QtGui.QStandardItem("A"))
        self.model_s.setItem(0, 3, QtGui.QStandardItem("B"))
        self.model_s.setItem(0, 4, QtGui.QStandardItem("A"))
        self.model_s.setItem(0, 5, QtGui.QStandardItem("B"))
        self.model_s.setItem(1, 0, QtGui.QStandardItem("05"))
        self.model_s.setItem(4, 0, QtGui.QStandardItem("06"))
        self.model_s.setItem(1, 1, QtGui.QStandardItem("A开B关"))
        self.model_s.setItem(2, 1, QtGui.QStandardItem("A关B开"))
        self.model_s.setItem(3, 1, QtGui.QStandardItem("A关B关"))
        self.model_s.setItem(4, 1, QtGui.QStandardItem("A开B关"))
        self.model_s.setItem(5, 1, QtGui.QStandardItem("A关B开"))
        self.model_s.setItem(6, 1, QtGui.QStandardItem("A关B关"))
        self.model_s.setItem(7, 0, QtGui.QStandardItem("扫描灵敏度"))
        self.model_s.setItem(8, 0, QtGui.QStandardItem("05"))
        self.model_s.setItem(9, 0, QtGui.QStandardItem("06"))

        tableView.setModel(self.model_s)
        tableView.setColumnWidth(0, 50)
        tableView.setColumnWidth(1, 80)
        tableView.setColumnWidth(2, 80)
        tableView.setColumnWidth(3, 80)
        tableView.setColumnWidth(4, 80)
        tableView.setColumnWidth(5, 80)
        tableView.setSpan(1, 0, 3, 1)
        tableView.setSpan(4, 0, 3, 1)
        tableView.setSpan(7, 0, 1, 6)
        tableView.setSpan(8, 0, 1, 2)
        tableView.setSpan(9, 0, 1, 2)
        tableView.setSpan(8, 2, 1, 2)
        tableView.setSpan(9, 2, 1, 2)
        tableView.setSpan(8, 4, 1, 2)
        tableView.setSpan(9, 4, 1, 2)
        for i in range(10):
            for j in range(6):
                if self.model_s.item(i,j) == None:
                    self.model_s.setItem(i, j, QtGui.QStandardItem(" "))
                    self.model_s.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)

    def sens_test(self):
        x = sens()
        x.sens_t(0)

    def updata_s(self,data,x,y):
        if self.radioButton_1.isChecked():
            self.model_s.setItem(x, y, QtGui.QStandardItem(data))
        elif self.radioButton_2.isChecked():
            self.model_s.setItem(x + 3, y, QtGui.QStandardItem(data))

    def modulation(self,objectname):
        horizontalLayout = QtWidgets.QHBoxLayout(objectname)
        horizontalLayout.setObjectName("horizontalLayout")
        tableView = QtWidgets.QTableView(objectname)
        tableView.setObjectName("tableView")
        self.myModel = QtGui.QStandardItemModel(objectname)
        horizontalLayout.addWidget(tableView)

        model = QtGui.QStandardItemModel(tableView)

        model.setRowCount(6)
        model.setColumnCount(10)
        model.setItem(1, 0, QtGui.QStandardItem(" "))
        model.setItem(1, 5, QtGui.QStandardItem(" "))
        model.setItem(0, 0, QtGui.QStandardItem(" "))
        model.setItem(0, 1, QtGui.QStandardItem("调制度"))
        model.setItem(0, 5, QtGui.QStandardItem(" "))
        model.setItem(0, 6, QtGui.QStandardItem("测距音"))
        model.setItem(1, 1, QtGui.QStandardItem("A"))
        model.setItem(1, 3, QtGui.QStandardItem("B"))
        model.setItem(1, 6, QtGui.QStandardItem("A"))
        model.setItem(1, 8, QtGui.QStandardItem("B"))
        model.setItem(2, 0, QtGui.QStandardItem("无上行"))
        model.setItem(3, 0, QtGui.QStandardItem("遥控"))
        model.setItem(4, 0, QtGui.QStandardItem("测距"))
        model.setItem(5, 0, QtGui.QStandardItem("遥控+测距"))
        model.setItem(2, 5, QtGui.QStandardItem("100K"))
        model.setItem(3, 5, QtGui.QStandardItem("20K"))
        model.setItem(4, 5, QtGui.QStandardItem("15K"))
        model.setItem(5, 5, QtGui.QStandardItem("8K"))

        tableView.setModel(model)
        tableView.setColumnWidth(0, 90)
        tableView.setColumnWidth(1, 60)
        tableView.setColumnWidth(2, 60)
        tableView.setColumnWidth(3, 60)
        tableView.setColumnWidth(4, 60)
        tableView.setColumnWidth(5, 60)
        tableView.setColumnWidth(6, 60)
        tableView.setColumnWidth(7, 60)
        tableView.setColumnWidth(8, 60)
        tableView.setColumnWidth(9, 60)
        tableView.setSpan(0, 1, 1, 4)
        tableView.setSpan(0, 6, 1, 4)
        tableView.setSpan(1, 1, 1, 2)
        tableView.setSpan(1, 3, 1, 2)
        tableView.setSpan(1, 6, 1, 2)
        tableView.setSpan(1, 8, 1, 2)
        for i in range(6):
            for j in range(10):
                if model.item(i,j) == None:
                    model.setItem(i, j, QtGui.QStandardItem("0"))
                model.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)

    def AGC(self,objectname):
        horizontalLayout = QtWidgets.QHBoxLayout(objectname)
        horizontalLayout.setObjectName("horizontalLayout")
        tableView = QtWidgets.QTableView(objectname)
        tableView.setObjectName("tableView")
        self.myModel = QtGui.QStandardItemModel(objectname)
        horizontalLayout.addWidget(tableView)

        model = QtGui.QStandardItemModel(tableView)

        model.setRowCount(13)
        model.setColumnCount(9)
        model.setItem(1, 0, QtGui.QStandardItem(" "))
        model.setItem(1, 5, QtGui.QStandardItem(" "))
        model.setItem(0, 0, QtGui.QStandardItem(" "))
        model.setItem(0, 1, QtGui.QStandardItem("A机"))
        model.setItem(0, 5, QtGui.QStandardItem(" "))
        model.setItem(0, 5, QtGui.QStandardItem("B机"))
        model.setItem(1, 1, QtGui.QStandardItem("05"))
        model.setItem(1, 3, QtGui.QStandardItem("06"))
        model.setItem(1, 5, QtGui.QStandardItem("05"))
        model.setItem(1, 7, QtGui.QStandardItem("06"))
        model.setItem(2, 1, QtGui.QStandardItem("数字"))
        model.setItem(2, 2, QtGui.QStandardItem("模拟"))
        model.setItem(2, 3, QtGui.QStandardItem("数字"))
        model.setItem(2, 4, QtGui.QStandardItem("模拟"))
        model.setItem(2, 5, QtGui.QStandardItem("数字"))
        model.setItem(2, 6, QtGui.QStandardItem("模拟"))
        model.setItem(2, 7, QtGui.QStandardItem("数字"))
        model.setItem(2, 8, QtGui.QStandardItem("模拟"))
        model.setItem(2, 0, QtGui.QStandardItem(" "))
        model.setItem(3, 0, QtGui.QStandardItem("-34"))
        model.setItem(4, 0, QtGui.QStandardItem("-44"))
        model.setItem(5, 0, QtGui.QStandardItem("-54"))
        model.setItem(6, 0, QtGui.QStandardItem("-64"))
        model.setItem(7, 0, QtGui.QStandardItem("-74"))
        model.setItem(8, 0, QtGui.QStandardItem("-84"))
        model.setItem(9, 0, QtGui.QStandardItem("-89"))
        model.setItem(10, 0, QtGui.QStandardItem("-94"))
        model.setItem(11, 0, QtGui.QStandardItem("-99"))
        model.setItem(12, 0, QtGui.QStandardItem("门限"))

        tableView.setModel(model)
        tableView.setColumnWidth(0, 90)
        tableView.setColumnWidth(1, 60)
        tableView.setColumnWidth(2, 60)
        tableView.setColumnWidth(3, 60)
        tableView.setColumnWidth(4, 60)
        tableView.setColumnWidth(5, 60)
        tableView.setColumnWidth(6, 60)
        tableView.setColumnWidth(7, 60)
        tableView.setColumnWidth(8, 60)
        tableView.setColumnWidth(9, 60)
        tableView.setSpan(0, 1, 1, 4)
        tableView.setSpan(0, 5, 1, 4)
        tableView.setSpan(1, 1, 1, 2)
        tableView.setSpan(1, 3, 1, 2)
        tableView.setSpan(1, 5, 1, 2)
        tableView.setSpan(1, 7, 1, 2)

        for i in range(13):
            for j in range(9):
                if model.item(i, j) == None:
                    model.setItem(i, j, QtGui.QStandardItem("0"))
                model.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # MainWindow = MainWindow()
    ui = auto_ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())