# -*- coding: utf-8 -*-
#   ____ ____        _  _    __    __   
#  / ___/ ___|      | || |  / /_  / /_  
# | |   \___ \ _____| || |_| '_ \| '_ \ 
# | |___ ___) |_____|__   _| (_) | (_) |
#  \____|____/         |_|  \___/ \___/ 
#
#                                       
# host.py
# Host program for CS 466 term project. Builds baseline GUI for easy prototyping. GUI has 5 buttons 
# that will perform some task that we described in the requirements. Each function shall be defined 
# in its own .py file to keep host.py file clean and presentable.
#
# Dependencies
import admin
import sys
from PyQt5                  import QtCore, QtGui, QtWidgets
from zipFuncs               import *
from ContextMenu            import *
from choose_startupFunc     import *
from cleanup_folderFunc     import *
from help_menuFunc          import *
from unstax                 import *
from zipsettings            import *
from cleanupsettings        import *
from execute                import *
from executesettings        import *
from staxsettings           import *
from egopreferences         import *
#################################################################################################

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

class Ui_Ego(object):

    def openEgoPref(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ego_Pref()
        self.ui.setupUi(self.window)
        self.window.show()

    def openExsettings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Execute_Setting()
        self.ui.setupUi(self.window)
        self.window.show()

    def openZipSettings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ZipSettings()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCleanUpSettings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CleanUpSettings()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def staxsettings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = staxsettings()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Ego):
        Ego.setObjectName("Ego")
        Ego.resize(178, 385)
        self.centralwidget = QtWidgets.QWidget(Ego)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 181, 375))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 158, 360))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.staxsettings)
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.staxFunc = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.staxFunc.setObjectName("staxFunc")
        self.staxFunc.clicked.connect(stax)
        self.verticalLayout_2.addWidget(self.staxFunc)
        self.unstaxFunc = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.unstaxFunc.setObjectName("unstaxFunc")
        self.verticalLayout_2.addWidget(self.unstaxFunc)
        self.unstaxFunc.clicked.connect(unstax)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.toolButton_3 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.clicked.connect(self.openZipSettings)
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.zipFunc = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.zipFunc.setObjectName("zipFunc")
        self.zipFunc.clicked.connect(zip)
        self.verticalLayout.addWidget(self.zipFunc)
        self.unzipFunc = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.unzipFunc.clicked.connect(unzip)
        self.unzipFunc.setObjectName("unzipFunc")
        self.verticalLayout.addWidget(self.unzipFunc)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.toolButton_4 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_4.addWidget(self.toolButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.startupFunc = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.startupFunc.clicked.connect(choose_startupprograms_button)
        self.startupFunc.setObjectName("startupFunc")
        self.verticalLayout_5.addWidget(self.startupFunc)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.toolButton_2 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.clicked.connect(self.openCleanUpSettings)
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.cleanupFunc = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.cleanupFunc.setObjectName("cleanupFunc")
        self.cleanupFunc.clicked.connect(cleanup_folder_button)
        self.verticalLayout_3.addWidget(self.cleanupFunc)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.toolButton_5 = QtWidgets.QToolButton(self.verticalLayoutWidget_2)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.clicked.connect(self.openExsettings)
        self.horizontalLayout_5.addWidget(self.toolButton_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.executeFunc = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.executeFunc.setObjectName("executeFunc")
        self.executeFunc.clicked.connect(executeScript)
        self.verticalLayout_4.addWidget(self.executeFunc)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayoutWidget_2.raise_()
        Ego.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ego)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 178, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Ego.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ego)
        self.statusbar.setObjectName("statusbar")
        Ego.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Ego)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Ego)
        self.actionSave.setObjectName("actionSave")
        self.actionEdit = QtWidgets.QAction(Ego)
        self.actionEdit.setObjectName("actionEdit")
        self.actionClose = QtWidgets.QAction(Ego)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(Ego)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(quit)
        self.actionSee_Help = QtWidgets.QAction(Ego)
        self.actionSee_Help.setObjectName("actionSee_Help")
        self.actionSee_Help.triggered.connect(help)
        self.actionEGO_Preferences = QtWidgets.QAction(Ego)
        self.actionEGO_Preferences.setObjectName("actionEGO_Preferences")
        self.actionEGO_Preferences.triggered.connect(self.openEgoPref)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionEGO_Preferences)
        self.menuQuit.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionSee_Help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Ego)
        QtCore.QMetaObject.connectSlotsByName(Ego)

    def retranslateUi(self, Ego):
        _translate = QtCore.QCoreApplication.translate
        Ego.setWindowTitle(_translate("Ego", "EGO"))
        Ego.setWindowIcon(QtGui.QIcon('ego_logo.png'))
        self.label.setText(_translate("Ego", "Stax Commands"))
        self.toolButton.setText(_translate("Ego", "..."))
        self.staxFunc.setText(_translate("Ego", "Stax"))
        self.unstaxFunc.setText(_translate("Ego", "UnStax"))
        self.label_2.setText(_translate("Ego", "ZipFile Commands"))
        self.toolButton_3.setText(_translate("Ego", "..."))
        self.zipFunc.setText(_translate("Ego", "Zip File"))
        self.unzipFunc.setText(_translate("Ego", "UnZip File"))
        self.label_4.setText(_translate("Ego", "Startup Programs"))
        self.toolButton_4.setText(_translate("Ego", "..."))
        self.startupFunc.setText(_translate("Ego", "Select Startup Programs"))
        self.label_3.setText(_translate("Ego", "Clean Up Folder"))
        self.toolButton_2.setText(_translate("Ego", "..."))
        self.cleanupFunc.setText(_translate("Ego", "Clean Up Folder"))
        self.label_5.setText(_translate("Ego", "Execute Scripts"))
        self.toolButton_5.setText(_translate("Ego", "..."))
        self.executeFunc.setText(_translate("Ego", "Execute"))
        self.menuFile.setTitle(_translate("Ego", "File"))
        self.menuQuit.setTitle(_translate("Ego", "Quit"))
        self.menuHelp.setTitle(_translate("Ego", "Help"))
        self.actionOpen.setText(_translate("Ego", "Open"))
        self.actionSave.setText(_translate("Ego", "Save"))
        self.actionEdit.setText(_translate("Ego", "Edit"))
        self.actionClose.setText(_translate("Ego", "Close"))
        self.actionQuit.setText(_translate("Ego", "Quit"))
        self.actionSee_Help.setText(_translate("Ego", "See Help"))
        self.actionEGO_Preferences.setText(_translate("Ego", "EGO Preferences"))
        Ego.shortcut1 = QShortcut(QKeySequence('z'),Ego)
        Ego.shortcut1.activated.connect(zip)
        Ego.shortcut2 = QShortcut(QKeySequence('u'),Ego)
        Ego.shortcut2.activated.connect(unzip)
        Ego.shortcut3 = QShortcut(QKeySequence('c'),Ego)
        Ego.shortcut3.activated.connect(cleanup_folder_button)
        Ego.shortcut4 = QShortcut(QKeySequence('s'),Ego)
        Ego.shortcut4.activated.connect(stax)
        Ego.shortcut5 = QShortcut(QKeySequence('q'),Ego)
        Ego.shortcut5.activated.connect(quit)
        Ego.shortcut6 = QShortcut(QKeySequence('h'),Ego)
        Ego.shortcut6.activated.connect(help)


##################################### Functions #####################################################

def quit():
    sys.exit()

def stax():
    test = Stax()
    test.stack()

def unstax():
    test = Stax()
    test.unstack()

def cleanup_folder_button():
    """ Clean up selected folder. Looks for old or out of place files and 
    asks users to delete.
    """
    clean = CleanUp()
    clean.create_folder()
    clean.open_folder()
    clean.gather_old_files()

    #self, tool_name, exe_path, startin, icon_path
    clean.create_shortcut()

def choose_startupprograms_button():
    """ Select which programs to allow to begin upon startup """
    choose_startupprograms(Ego)

def help():
    """ Display a help menu with instructions for each function/functionality """
    show_help_menu(Ego)

def unzip():
    """ Python Script to unzip file of users choice and extract files to location
    specified by the user. 
    """
    path = easygui.fileopenbox('Which file would you like to unzip?')
    zip_ref = zipfile.ZipFile(path, 'r')
    path_to = easygui.diropenbox('Where would you like to extract the files to?')
    zip_ref.extractall(path_to)
    zip_ref.close()

def zip():
    dir_in = easygui.diropenbox('Which directory would you like to zip?')
    filename = easygui.filesavebox('Where would you like to zip?')
    zipfiles(dir_in,filename)

if __name__ == "__main__":
    if not admin.isUserAdmin():
        admin.runAsAdmin()

    app = QtWidgets.QApplication(sys.argv)
    Ego = QtWidgets.QMainWindow()
    ui = Ui_Ego()
    ui.setupUi(Ego)
    Ego.show()
    sys.exit(app.exec_())
