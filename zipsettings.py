# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zipsettings.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from zipFuncs import unzipAll, automateUnZip
import threading
from functools import partial


class Ui_ZipSettings(object):
    def setupUi(self, ZipSettings):
        self.auto = False
        ZipSettings.setObjectName("ZipSettings")
        ZipSettings.resize(306, 169)
        self.centralwidget = QtWidgets.QWidget(ZipSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 291, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dir_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dir_name.setObjectName("dir_name")
        self.dir_name.setText("C:\\Users\\eguzman\\Downloads")
        self.horizontalLayout_2.addWidget(self.dir_name)
        self.choose_dir_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.choose_dir_btn.setObjectName("choose_dir_btn")
        self.horizontalLayout_2.addWidget(self.choose_dir_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 251, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.savebtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.savebtn.setObjectName("savebtn")
        self.savebtn.clicked.connect(partial(self.do_zip,ZipSettings))
        self.horizontalLayout.addWidget(self.savebtn)
        self.cancelbtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelbtn.setObjectName("cancelbtn")
        self.cancelbtn.clicked.connect(ZipSettings.hide)
        self.horizontalLayout.addWidget(self.cancelbtn)
        ZipSettings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ZipSettings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 306, 21))
        self.menubar.setObjectName("menubar")
        ZipSettings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ZipSettings)
        self.statusbar.setObjectName("statusbar")
        ZipSettings.setStatusBar(self.statusbar)

        self.retranslateUi(ZipSettings)
        QtCore.QMetaObject.connectSlotsByName(ZipSettings)

    def retranslateUi(self, ZipSettings):
        _translate = QtCore.QCoreApplication.translate
        ZipSettings.setWindowTitle(_translate("ZipSettings", "MainWindow"))
        self.checkBox.setText(_translate("ZipSettings", "Automate UnZip-ing"))
        self.choose_dir_btn.setText(_translate("ZipSettings", "Choose Unzip All Directory"))
        self.savebtn.setText(_translate("ZipSettings", "Save"))
        self.cancelbtn.setText(_translate("ZipSettings", "Cancel"))


    def do_zip(self,ZipSettings):
        if self.checkBox.isChecked():
            if not self.auto:
                print('Automate')
                self.auto = AutoThread()
                self.auto.start()
        else:
            if self.auto:
                self.auto.do_run = False
        ZipSettings.hide()

class AutoThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        t = threading.currentThread()
        while getattr(t,'do_run',True):
            automateUnZip()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ZipSettings = QtWidgets.QMainWindow()
    ui = Ui_ZipSettings()
    ui.setupUi(ZipSettings)
    ZipSettings.show()
    sys.exit(app.exec_())
