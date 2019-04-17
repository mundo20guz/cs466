# choose_startupFunc.py

# pywin32 install required

import easygui
import os
import win32com.client
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Startup_Gui(QWidget):
    
    # create the gui window where the user can manage startup programs
    def __init__(self):
        super().__init__()
        
        # folder containing all programs that should run at startup
        self.startup_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup'
        
        self.setWindowTitle('Manage Startup Programs')
        layout = QVBoxLayout()
        self.setMinimumSize(375, 150)
        
        instructionLabel = QLabel('Add a new program or select a program to remove')
        instructionLabel.setAlignment(Qt.AlignCenter)
        
        addButton = QPushButton('Add new startup program')
        addButton.clicked.connect(self.add_to_startup)
        
        self.startupComboBox = QComboBox()
        self.update_startup_programs()
        
        currentProgramsLabel = QLabel('Current startup programs:')
        currentProgramsLabel.setBuddy(self.startupComboBox)
        
        removeButton = QPushButton('Remove selected program from startup')
        removeButton.clicked.connect(self.remove_from_startup)
        
        self.statusLabel = QLabel('Choose an option')
        
        programsLayout = QHBoxLayout()
        programsLayout.addWidget(currentProgramsLabel)
        programsLayout.addWidget(self.startupComboBox)
        
        layout.addWidget(instructionLabel)
        layout.addWidget(addButton)
        layout.addLayout(programsLayout)
        layout.addWidget(removeButton)
        layout.addWidget(self.statusLabel)
        self.setLayout(layout)
    
    # update the comboBox with the current programs in the startup folder
    def update_startup_programs(self):
        self.startupComboBox.clear()
        
        # go through all shortcuts in the startup folder, and add them to the ComboBox
        for file in os.listdir(self.startup_path):
            if file.endswith('.lnk'):
                self.startupComboBox.addItem(file.split(".lnk")[0])
    
    # adds a chosen program to startup file
    # by creating a shortcut to the program in the startup folder
    def add_to_startup(self):
        #have the user select a program to add
        target_path = easygui.fileopenbox('Which program would you like to run on startup')
        
        # if user fails to select a program, exit function early
        if target_path is None:
            self.statusLabel.setText('Unable to add: No file selected')
            return
        
        # make the shortcut name (same name as original program, but with .lnk extension)
        file_name = os.path.basename(target_path).rsplit('.', 1)[0]
        shortcut_name = (file_name + '.lnk')
        
        # check to see if the same program is already in the startup folder
        for file in os.listdir(self.startup_path):
            if file.endswith('.lnk'):
                if(shortcut_name == file):
                    self.statusLabel.setText('Unable to add: ' + file_name + ' is already in startup programs')
                    return
        
        # the path for the new shortcut, will be put in the startup folder
        path = os.path.join(self.startup_path, shortcut_name)
        
        # create the shortcut - will now run at startup
        try:
            shortcut = win32com.client.Dispatch("WScript.Shell").CreateShortCut(path)
            shortcut.Targetpath = target_path
            shortcut.WorkingDirectory = os.path.dirname(target_path)
            shortcut.save()
        except OSException:
            self.statusLabel.setText('Error: unable to create shortcut')
            return
        
        self.statusLabel.setText('Added program ' + file_name + ' to startup programs')
        
        # new program should be added to the ComboBox
        self.update_startup_programs()

    # removes a chosen program from the startup file
    # by deleting the shortcut from the startup folder
    def remove_from_startup(self):
    
        # make sure there are programs in the startup folder
        if self.startupComboBox.count() == 0:
            self.statusLabel.setText('Unable to remove: No startup programs found')
            return
        
        # program to be deleted is the one currently selected in the ComboBox
        selected_program = self.startupComboBox.currentText() + '.lnk'
        program_path = self.startup_path + '/' + selected_program
        
        # if the file doesn't exist, exit early
        if not os.path.exists(program_path):
            self.statusLabel.setText('Unable to remove: Shortcut not found')
            return
        
        # remove the (shortcut) file - will no longer run at startup
        try:
            os.remove(program_path)
        except OSError:
            self.statusLabel.setText('Error: removing file')
            return
        
        self.statusLabel.setText('Removed program ' + self.startupComboBox.currentText() + ' from startup programs')
        
        # new program should be removed from the ComboBox
        self.update_startup_programs()

# runs the startup gui where user can manage startup programs
def choose_startupprograms(gui):

    gui.startup_gui = Startup_Gui()
    gui.startup_gui.show()

