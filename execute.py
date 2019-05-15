import easygui
import sys
import os

def executeScript(ext='.py'):
	script_name = easygui.fileopenbox()
	cwd = os.getcwd()
	os.chdir(os.path.dirname(script_name))
	print(sys.executable + ' ' + script_name)
	os.system(sys.executable + ' ' + script_name)
	os.chdir(cwd)