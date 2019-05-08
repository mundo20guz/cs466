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
        
        startupButton = QPushButton('Startup Help')
        startupButton.clicked.connect(self.startup_help_button)
        
        cleanupButton = QPushButton('Cleanup Help')
        cleanupButton.clicked.connect(self.cleanup_help_button)
        
        staxButton = QPushButton('Stax Help')
        staxButton.clicked.connect(self.stax_help_button)
        
        #buttons with bullet points
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(unzipButton)
        buttonLayout.addWidget(startupButton)
        buttonLayout.addWidget(cleanupButton)
        buttonLayout.addWidget(staxButton)
        
        self.helpText = QTextEdit()
        self.helpText.setReadOnly(True)
        self.helpText.setText('Select a Guide')
        
        layout.addLayout(buttonLayout)
        layout.addWidget(self.helpText)
        self.setLayout(layout)
        
        self.shortcut1 = QShortcut(QKeySequence('1'), self)
        self.shortcut1.activated.connect(self.unzip_help_button)
        
        self.shortcut3 = QShortcut(QKeySequence('2'), self)
        self.shortcut3.activated.connect(self.startup_help_button)
        
        self.shortcut4 = QShortcut(QKeySequence('3'), self)
        self.shortcut4.activated.connect(self.cleanup_help_button)
        
        self.shortcut2 = QShortcut(QKeySequence('4'), self)
        self.shortcut2.activated.connect(self.stax_help_button)
    
    def unzip_help_button(self):
        message = 'Unzip Help\n'
        message += '\n• Lets user select a file of their choice to unzip and unzips it'
        message += '\n• it then places extracted files in another chosen location'
        message += '\n\nAuto Unzip Help\n'
        message += '\n• Continously checks the downloads folder for new zip files'
        message += '\n• when one is found, its files are extracted'
        message += '\n• extracted files are placed in a new folder'
        message += '\n• the originial zip file is then deleted'
        self.helpText.setText(message)
    
    def stax_help_button(self):
        message = 'Stax Help\n'
        message += '\n• Groups scattered documents and pictures on the desktop together'
        message += '\n• pdf, txt, & rtf files are put into a DocumentStax desktop file'
        message += '\n• jpg, png, & gif files are put into a PictureStax desktop file'
        message += '\n\nUnstax Help\n'
        message += '\n• Undoes what the Stax operation did'
        message += '\n• moves files from DocumentStax & PictureStax back to the desktop'
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
        message += '\n• Creates and uses the Old_Files directory to store results'
        message += '\n• gathers files that have not been accessed in months'
        message += '\n• creates a shortcut to each of these files in the Old_Files folder'
        self.helpText.setText(message)

# display a gui with instructions for how to use the program
def show_help_menu(gui):

    gui.helpmenu_gui = HelpMenu_Gui()
    gui.helpmenu_gui.show()

