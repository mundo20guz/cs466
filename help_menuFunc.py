# help_menuFunc.py

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class HelpMenu_Gui(QWidget):

    # create the gui window where the user can manage startup programs
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Help Menu')
        layout = QVBoxLayout()
        self.setMinimumSize(375, 0)
        
        unzipButton = QPushButton('Unzip Help')
        unzipButton.clicked.connect(self.unzip_help_button)
        
        uninstallButton = QPushButton('Uninstall Help')
        uninstallButton.clicked.connect(self.uninstall_help_button)
        
        startupButton = QPushButton('Startup Help')
        startupButton.clicked.connect(self.startup_help_button)
        
        cleanupButton = QPushButton('Cleanup Help')
        cleanupButton.clicked.connect(self.cleanup_help_button)
        
        #buttons with bullet points
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(unzipButton)
        buttonLayout.addWidget(uninstallButton)
        buttonLayout.addWidget(startupButton)
        buttonLayout.addWidget(cleanupButton)
        
        self.helpText = QTextEdit()
        self.helpText.setReadOnly(True)
        self.helpText.setText('Select a Guide')
        
        layout.addLayout(buttonLayout)
        layout.addWidget(self.helpText)
        self.setLayout(layout)
        
        self.shortcut1 = QShortcut(QKeySequence('1'), self)
        self.shortcut1.activated.connect(self.unzip_help_button)
        
        self.shortcut2 = QShortcut(QKeySequence('2'), self)
        self.shortcut2.activated.connect(self.uninstall_help_button)
        
        self.shortcut3 = QShortcut(QKeySequence('3'), self)
        self.shortcut3.activated.connect(self.startup_help_button)
        
        self.shortcut4 = QShortcut(QKeySequence('4'), self)
        self.shortcut4.activated.connect(self.cleanup_help_button)
    
    def unzip_help_button(self):
        message = 'Unzip Help\n'
        message += '\n•'
        message += '\n•'
        message += '\n•'
        self.helpText.setText(message)
    
    def uninstall_help_button(self):
        message = 'Uninstall Help\n'
        message += '\n•'
        message += '\n•'
        message += '\n•'
        self.helpText.setText(message)
    
    def startup_help_button(self):
        message = 'Startup Help\n'
        message += '\n• To Add a new startup program'
        message += '\n    * first press the add new startup program button'
        message += '\n    * then choose the program you want to run at system startup\n'
        message += '\n• To Remove an existing startup program'
        message += '\n    * first pick a file in the list of current startup programs'
        message += '\n    * then press the remove selected program button'
        self.helpText.setText(message)
    
    def cleanup_help_button(self):
        message = 'Cleanup Help\n'
        message += '\n•'
        message += '\n•'
        message += '\n•'
        self.helpText.setText(message)

# display a gui with instructions for how to use the program
def show_help_menu(gui):

    gui.helpmenu_gui = HelpMenu_Gui()
    gui.helpmenu_gui.show()

