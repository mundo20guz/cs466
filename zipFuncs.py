# unzipFunc.py
import time
import zipfile
import os
import easygui
from functools import partial
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def unzip():
	""" Python Script to unzip file of users choice and extract files to location
	specified by the user. 
	"""
	path = easygui.fileopenbox('Which file would you like to unzip?')
	zip_ref = zipfile.ZipFile(path, 'r')
	path_to = easygui.diropenbox('Where would you like to extract the files to?')
	zip_ref.extractall(path_to)
	zip_ref.close()


def unzipAll(dir='C:\\Users\\eguzman\\Downloads'):
	""" Python Script to unzip all files in a downloads directory. Will Extract
	files to directory of the same name.
	"""
	dir_name = dir
	extension = ".zip"

	os.chdir(dir_name)

	for item in os.listdir(dir_name):
		if item.endswith(extension):
			file_name = os.path.abspath(item)

			with zipfile.ZipFile(file_name,'r') as zip:
				zip.extractall(dir_name)

			os.remove(file_name)


def zipfiles(dir_in,file_out):
	""" Python Script to zip a collection of files.
	@param dir: a directory of files to be zipped.
	"""
	cwd = os.getcwd()
	os.chdir(os.path.split(dir_in)[0])

	file_paths = get_all_file_paths('.\\' + os.path.split(dir_in)[1])
  
	# printing the list of all files to be zipped 
	for file_name in file_paths: 
		print(file_name)
		
	# writing files to a zipfile
	with zipfile.ZipFile(file_out,'w') as zip: 
		# writing each file one by one 
		for file in file_paths:
			zip.write(file)
	os.chdir(cwd)
  
	print('All files zipped successfully!') 
	

def get_all_file_paths(directory): 
  
	# initializing empty file paths list 
	file_paths = [] 
  
	# crawling through directory and subdirectories 
	for root, directories, files in os.walk(directory): 
		for filename in files: 
			# join the two strings in order to form the full filepath. 
			filepath = os.path.join(root, filename) 
			file_paths.append(filepath) 
  
	# returning all file paths 
	return file_paths     


def automateUnZip():
	""" Python Script to unzip all files in a downloads directory. Will Extract
	files to same directory.
	"""
	w = Watcher()
	w.run()
	

class Watcher:
	DIRECTORY_TO_WATCH = 'C:\\Users\\eguzman\\Downloads'
	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
		self.observer.start()

		try:
			while True:
				time.sleep(2)
		except:
			self.observer.stop()
			#print("Error")

		self.observer.join()


class Handler(FileSystemEventHandler):
	@staticmethod
	def on_any_event(event):
		if event.is_directory:
			return None
		elif event.event_type == 'created':
			# Take any action here when a file is first created.
			print('UNZIP')
			unzipAll()
		elif event.event_type == 'modified':
			# Taken any action here when a file is modified.
			unzipAll()
