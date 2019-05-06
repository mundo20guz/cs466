# unzipFunc.py
import time
import zipfile
import os
import easygui
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


def unzipAll():
	""" Python Script to unzip all files in a downloads directory. Will Extract
	files to directory of the same name.
	"""
	dir_name = 'C:\\Users\\eguzman\\Downloads'
	extension = ".zip"

	os.chdir(dir_name)

	for item in os.listdir(dir_name):
	    if item.endswith(extension):
	        file_name = os.path.abspath(item)

	        with zipfile.ZipFile(file_name,'r') as zip:
	        	zip.extractall(dir_name)

	        os.remove(file_name)


def zipFiles(dir):
	""" Python Script to zip a collection of files.
	@param dir: a directory of files to be zipped.
	"""
	pass


def automateUnZip():
	""" Python Script to unzip all files in a downloads directory. Will Extract
	files to same directory.
	"""
	w = Watcher()
	w.run()
	

class Watcher:

    DIRECTORY_TO_WATCH = "C:\\Users\\eguzman\\Downloads"

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
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            unzipAll()
            #print("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            #print("Received modified event - %s." % event.src_path)
            unzipAll()
