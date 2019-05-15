# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cleanupsettings.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CleanUpSettings(object):
    def setupUi(self, Ui_CleanUpSettings):
        Ui_CleanUpSettings.setObjectName("Ui_CleanUpSettings")
        Ui_CleanUpSettings.resize(310, 186)
        self.centralwidget = QtWidgets.QWidget(Ui_CleanUpSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 291, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 90, 251, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(Ui_CleanUpSettings.hide)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(Ui_CleanUpSettings.hide)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        Ui_CleanUpSettings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_CleanUpSettings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 21))
        self.menubar.setObjectName("menubar")
        Ui_CleanUpSettings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_CleanUpSettings)
        self.statusbar.setObjectName("statusbar")
        Ui_CleanUpSettings.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_CleanUpSettings)
        QtCore.QMetaObject.connectSlotsByName(Ui_CleanUpSettings)

    def retranslateUi(self, Ui_CleanUpSettings):
        _translate = QtCore.QCoreApplication.translate
        Ui_CleanUpSettings.setWindowTitle(_translate("Ui_CleanUpSettings", "Ui_CleanUpSettings"))
        self.pushButton.setText(_translate("Ui_CleanUpSettings", "Choose Directory to Clean"))
        self.pushButton_2.setText(_translate("Ui_CleanUpSettings", "Save"))
        self.pushButton_3.setText(_translate("Ui_CleanUpSettings", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_CleanUpSettings = QtWidgets.QMainWindow()
    ui = Ui_CleanUpSettings()
    ui.setupUi(Ui_CleanUpSettings)
    Ui_CleanUpSettings.show()
    sys.exit(app.exec_())
