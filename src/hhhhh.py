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
from threading import Thread
from stray import stray_ui
from can import Can_Ui
from can_reset import Ui_Dialog


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.init_flag = 0
        self.Tab_count = 0
        self.Tab_Index = 0
        self.flag = [None] * 3
        self.can0_flag = None
        self.can1_flag = None
        self.stray_flag = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 733)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget_2")
        self.tabWidget.setVisible(False)

        self.pushButton = QtWidgets.QPushButton("can",self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton("杂散",self.centralwidget)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.stray_ui)
        self.pushButton_2.clicked.connect(self.Tab_visible)

        self.tabWidget.tabBarDoubleClicked.connect(self.tab_event)
        self.tabWidget.currentChanged.connect(self.Tab_CurrentIndex)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 26))
        self.menubar.setObjectName("menubar")

        fileMenu = self.menubar.addMenu('&文件')

        self.can0_menubar = self.createAction(MainWindow,"&Can0", self.can0_ui,"Ctrl+T", "can0")
        self.can1_menubar = self.createAction(MainWindow,"&Can1", self.can1_ui,"Ctrl+M", "can1")
        self.stary_Tab = self.createAction(MainWindow,"&杂散", self.stray_ui,"Ctrl+F", "杂散")
        self.QuitAction = self.createAction(MainWindow,"&Quit", QtWidgets.qApp.quit,"Ctrl+Q", "quit")
        self.can0_menubar.setVisible(False)
        self.can1_menubar.setVisible(False)
        self.stary_Tab.setVisible(False)
        self.QuitAction.setVisible(False)
        fileMenu.addAction(self.can0_menubar)
        fileMenu.addAction(self.can1_menubar)
        fileMenu.addAction(self.stary_Tab)
        fileMenu.addAction(self.QuitAction)

        MainWindow.setMenuBar(self.menubar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def createAction(self,objectname, text, slot=None, shortcut=None,tip=None):
        action = QtWidgets.QAction(text, objectname)
        action.setShortcut(shortcut)  # 设置快捷键
        action.setStatusTip(tip)
        action.triggered.connect(slot)
        return action

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def can_ui(self,bound):
        self.can0_ui(bound)
        self.can1_ui(bound)
        self.Tab_visible()
        self.tabWidget.setCurrentIndex(self.Tab_count - 2)

    def can0_ui(self,bound):
        self.can0_tab = QtWidgets.QMainWindow()
        self.can0_tab.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.can0_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.can0_Widgets = Can_Ui()
        self.can0_Widgets.__init__(0,bound)
        # self.can0_Widgets.StartCAN()
        self.verticalLayout_2.addWidget(self.can0_Widgets.setupUi(self.can0_tab))
        self.tabWidget.addTab(self.can0_tab, "can0")

        self.Tab_Index = self.Tab_count
        self.flag[0] = self.Tab_count
        self.Tab_count += 1
        self.tabWidget.setCurrentIndex(self.Tab_count - 1)
        if self.init_flag == 0:
            self.Tab_visible()
        else:
            self.menubar_visible()

    def can1_ui(self,bound):
        self.can1_tab = QtWidgets.QMainWindow()
        self.can1_tab.setObjectName("tab_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.can1_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # Can_Ui.__init__(can_Index = self.can_Index,bound = self.bound)
        self.can1_Widgets = Can_Ui()
        self.can1_Widgets.__init__(1, bound)
        # self.can1_Widgets.StartCAN()
        self.verticalLayout_3.addWidget(self.can1_Widgets.setupUi(self.can1_tab))
        self.tabWidget.addTab(self.can1_tab, "can1")

        self.Tab_Index = self.Tab_count
        self.flag[1] = self.Tab_count
        self.Tab_count += 1
        self.tabWidget.setCurrentIndex(self.Tab_count - 1)
        if self.init_flag == 0:
            self.Tab_visible()
        else:
            self.menubar_visible()

    def stray_ui(self):
        self.stray = QtWidgets.QMainWindow()
        self.stray.setObjectName("stray")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.stray)
        self.verticalLayout_4.setObjectName("verticalLayout_3")
        self.haha = stray_ui()
        self.verticalLayout_4.addWidget(self.haha.setupUi(self.stray))
        self.tabWidget.addTab(self.stray, "杂散")
        self.Tab_Index = self.Tab_count
        self.flag[2] = self.Tab_count
        self.Tab_count += 1
        self.tabWidget.setCurrentIndex(self.Tab_count - 1)
        if self.init_flag == 0:
            self.Tab_visible()
        else:
            self.menubar_visible()

    def Tab_visible(self):
        self.init_flag = 1
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.tabWidget.setVisible(True)
        self.verticalLayout.addWidget(self.tabWidget)
        self.QuitAction.setVisible(True)
        self.menubar_visible()

    def Tab_CurrentIndex(self):
        self.Tab_Index2 = self.Tab_Index
        self.Tab_Index = self.tabWidget.currentIndex()

    def tab_event(self):
        self.Tab_count -= 1
        self.a = self.tabWidget.currentIndex()
        if self.Tab_Index2 == self.Tab_Index:
            self.tabWidget.setCurrentIndex(self.a - 1)
        else:
            self.tabWidget.setCurrentIndex(self.Tab_Index2)
        self.tabWidget.removeTab(self.a)
        # self.close_tab = self.flag[self.a]
        for i in range(len(self.flag)):
            if self.flag[i] == self.a:
                self.flag[i] = None
            elif self.flag[i] > self.a:
                self.flag[i] = self.flag[i] - 1
            else:
                pass
        self.menubar_visible()

    def menubar_visible(self):
        if self.flag[0] == None:
            self.can0_menubar.setVisible(True)
        else:
            self.can0_menubar.setVisible(False)
        if self.flag[1] == None:
            self.can1_menubar.setVisible(True)
        else:
            self.can1_menubar.setVisible(False)
        if self.flag[2] == None:
            self.stary_Tab.setVisible(True)
        else:
            self.stary_Tab.setVisible(False)

class Main(QtWidgets.QMainWindow):
    signal = QtCore.pyqtSignal()

    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog = can_rst()
        self.dialog_done = False

        self.ui.pushButton.clicked.connect(self.start_thread)

    def complete_dialog(self,can_Index = None,bound = None):
        self.dialog_done = True
        if can_Index == 0:
            self.ui.can0_ui(bound)
        elif can_Index == 1:
            self.ui.can1_ui(bound)
        elif can_Index == 2:
            self.ui.can_ui(bound)

    def wait_for_dialog(self):
        while  not self.dialog_done:
            pass
        self.dialog_done = False

    def start_thread(self):
        t = Thread(target=self.show_dialog)
        t.daemon = True
        t.start()

    def show_dialog(self):
        # Do lots of background stuff here
        self.signal.emit()
        # Wait for the dialog to get closed
        self.wait_for_dialog()

# class MainWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        self.can = Can_Ui()
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.can.CloseCAN()
            self.can.CloseCAN()
            self.can.CloseCAN()
            event.accept()
        else:
            event.ignore()

class can_rst(QtWidgets.QDialog):
    signal = QtCore.pyqtSignal(int,int)

    def __init__(self, parent=None):
        super(can_rst, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.close)

    def show_message(self):
        super(can_rst, self).exec_()
        self.can_Index = self.ui.comboBox.currentIndex()
        self.bound = self.ui.comboBox_2.currentIndex()
        self.signal.emit(self.can_Index,self.bound)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    # ui.setupUi(MainWindow)
    ui.show()

    # can_rt = Main()
    dialog = can_rst()
    ui.signal.connect(dialog.show_message)
    dialog.signal.connect(ui.complete_dialog)
    sys.exit(app.exec_())
