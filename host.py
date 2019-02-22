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
#from uninstallFunc 		import *
#from choose_startupFunc 	import *
#from cleanup_folderFunc 	import *
#from placeholderFunc		import *

#################################################################################################

def unzip_button():
	""" Unzips folder """
	unzip()


def uninstall_program_button():
	""" Select program to uninstall """
	#uninstall_program()
	pass

def choose_startupprograms_button():
	""" Select which programs to allow to begin upon startup """
	#choose_startupprograms()
	pass

def cleanup_folder_button():
	""" Clean up selected folder. Looks for old or out of place files and 
	asks users to delete.
	"""
	#cleanup_folder()
	pass

def placeholder_button():
	""" Placeholder for some other functionality """
	#placeholder()
	pass

# Create Proto GUI for 1st iteration
gui = Gui('CS-466 Gui')
gui.addLabel('Available Functions')
gui.addButton('Unzip',unzip_button)
gui.addButton('Uninstall Program',uninstall_program_button)
gui.addButton('Select Startup Programs',choose_startupprograms_button)
gui.addButton('Cleanup Folder',cleanup_folder_button)
gui.addButton('Placeholder',placeholder_button)
gui.launch()
