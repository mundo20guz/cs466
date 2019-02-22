# unzipFunc.py

import zipfile
import easygui

def unzip():
	""" Python Script to unzip file of users choice and extract files to location
	specified by the user. 
	-1st draft of unzip function. Most basic functionality. Does not crash.
	"""
	path = easygui.fileopenbox('Which file would you like to unzip?')
	zip_ref = zipfile.ZipFile(path, 'r')
	path_to = easygui.diropenbox('Where would you like to extract the files to?')
	zip_ref.extractall(path_to)
	zip_ref.close()
