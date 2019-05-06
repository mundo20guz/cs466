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

# Dependencies
from GuiEngine 				import *
from unzipFunc 				import *
from ContextMenu 			import *
from choose_startupFunc 	import *
from cleanup_folderFunc 	import *
from help_menuFunc			import *
import admin


#################################################################################################

def unzip_button():
	""" Unzips folder """
	unzipAll()

def auto_unzip():
	automateUnZip()


def uninstall_program_button():
	""" Select program to uninstall """
	#uninstall_program()
	pass

def choose_startupprograms_button():
	""" Select which programs to allow to begin upon startup """
	choose_startupprograms(gui)

def cleanup_folder_button():
	""" Clean up selected folder. Looks for old or out of place files and 
	asks users to delete.
	"""
	clean = CleanUp()
	clean.create_folder()
	clean.open_folder()
	#clean.gather_old_files()

	#self, tool_name, exe_path, startin, icon_path
	clean.create_shortcut()


def help_menu_button():
	""" Display a help menu with instructions for each function/functionality """
	show_help_menu(gui)

if not admin.isUserAdmin():
        admin.runAsAdmin()

# Add context menu feature
con = ContextMenu('C:\\Users\\eguzman\\AppData\\Local\\Continuum\\anaconda3\\python.exe',
		" \".\\stax.py\" \"%1\"",
		" \".\\stax.py\" \"%1\"")

con.edit_registry()

# Build the Gui
gui = Gui('CS-466 Gui')
gui.addLabel('Available Functions')
gui.addButton('Unzip (z)',unzip_button)
gui.addButton('Auto Unzip All (u)',auto_unzip)
gui.addButton('Select Startup Programs (s)',choose_startupprograms_button)
gui.addButton('Cleanup Folder (c)',cleanup_folder_button)
gui.addButton('Help Menu (h)',help_menu_button)

# Create shortcut keys
gui.shortcut1 = QShortcut(QKeySequence('z'), gui)
gui.shortcut1.activated.connect(unzip_button)
gui.shortcut2 = QShortcut(QKeySequence('u'), gui)
gui.shortcut2.activated.connect(uninstall_program_button)
gui.shortcut3 = QShortcut(QKeySequence('s'), gui)
gui.shortcut3.activated.connect(choose_startupprograms_button)
gui.shortcut4 = QShortcut(QKeySequence('c'), gui)
gui.shortcut4.activated.connect(cleanup_folder_button)
gui.shortcut5 = QShortcut(QKeySequence('h'), gui)
gui.shortcut5.activated.connect(help_menu_button)

gui.launch()
