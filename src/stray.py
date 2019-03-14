# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stray.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import simulate
from PyQt5.QtCore import pyqtSignal

class stray_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(561, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        # self.textBrowser.setMinimumSize(QtCore.QSize(0, 200))
        self.textBrowser.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lineEdit_7)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 26))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.reset_data()
        self.pushButton.clicked.connect(self._pushButtonclick)

        self.threads = MyThread()
        self.threads.trigger.connect(self.update_text)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RF"))
        self.label_2.setText(_translate("MainWindow", "RFPLL"))
        self.label_3.setText(_translate("MainWindow", "IFPLL"))
        self.label_4.setText(_translate("MainWindow", "TF"))
        self.label_5.setText(_translate("MainWindow", "TFPLL"))
        self.label_6.setText(_translate("MainWindow", "BASE"))
        self.label_13.setText(_translate("MainWindow", "SPAN"))
        self.label_7.setText(_translate("MainWindow", "MHz"))
        self.label_8.setText(_translate("MainWindow", "MHz"))
        self.label_9.setText(_translate("MainWindow", "MHz"))
        self.label_10.setText(_translate("MainWindow", "MHz"))
        self.label_11.setText(_translate("MainWindow", "MHz"))
        self.label_12.setText(_translate("MainWindow", "MHz"))
        self.label_14.setText(_translate("MainWindow", "MHz"))
        self.pushButton.setText(_translate("MainWindow", "计算"))
        self.lineEdit.setText('2244.984')
        self.lineEdit_2.setText('1884.4')
        self.lineEdit_3.setText('340.5')
        self.lineEdit_4.setText('2067.2561')
        self.lineEdit_5.setText('1967.2')
        self.lineEdit_6.setText('20.2')
        self.lineEdit_7.setText('20')

    def reset_data(self):
        self.RF      = float(self.lineEdit.text())
        self.RFPLL   = float(self.lineEdit_2.text())
        self.IFPLL   = float(self.lineEdit_3.text())
        self.TF      = float(self.lineEdit_4.text())
        self.TFPLL   = float(self.lineEdit_5.text())
        self.BASE    = float(self.lineEdit_6.text())
        self.SPAN    = float(self.lineEdit_7.text())
        self.CLK     = 40

    def _pushButtonclick(self):
        self.reset_data()
        a1, a2, a3 = simulate.main(self.RF,self.RFPLL,self.TF,self.TFPLL,self.IFPLL,self.BASE,self.SPAN,self.CLK)
        for i in range(len(a2)):
            if (len(a1[i]) != 0):
                message = str(a2[i]) + " " + str(len(a1[i]))
                self.threads.run_(message)
                str_name = a2[i]
                str_name = str_name.split('_')
                if len(str_name) == 2:
                    str_name = str_name[1]
                    for j in range(len(a1[i])):
                        message = str(j + 1) + " " + str(str_name) + " " + '*' + " " + str(a3[i][j]) + " " +  '=' + " " + str(a1[i][j])
                        self.threads.run_(message)
                    self.threads.terminate()
                elif len(str_name) == 3:
                    str_name1 = str_name[1]
                    str_name2 = str_name[2]
                    for j in range(len(a1[i])):
                        message = str(j + 1) + " " + str(str_name1) + " " + '*' + " " + str(a3[i][j][0]) + " " + '+' + " " + str(str_name2) + " " + '*' + " " + str(a3[i][j][1]) + " " +  '=' + " " + str(a1[i][j])
                        self.threads.run_(message)
                    self.threads.terminate()
                else:
                    continue
            else:
                continue

    def update_text(self, message):
        self.textBrowser.append(message)
        self.textBrowser.repaint()    #实时更新显示

class MyThread(QtCore.QThread):
    trigger = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def run_(self,message = "NO Stray"):
        self.trigger.emit(message)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = stray_ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())