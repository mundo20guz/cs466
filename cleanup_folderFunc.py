import os
import winshell
from win32com.client import Dispatch
import datetime



class CleanUp:
    def __init__(self):
        self.directory = './Old_Files/'


    def create_folder(self):
        try:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        except OSError:
            print('Error: Creating directory' + self.directory)

    def create_shortcut(self):
        number = 1
        with open("OldFiles.txt",'r') as file:
            fixedLine = ""
            content = file.readlines()
            for line in content:
                print(line)
                for letter in line[-20:]:
                    if letter == "/":
                        fixedLine += ""
                    elif letter == "$":
                        fixedLine += ""
                    elif letter == "\\":
                        fixedLine += ""
                    else:
                        fixedLine += letter
                print(fixedLine)
                count = "file" + str(number)
                shell = Dispatch('WScript.Shell')
                shortcut_file = os.path.join('./Old_Files/', fixedLine[:-1] + '.lnk')
                shortcut = shell.CreateShortCut(shortcut_file)

                target = "C:"
                #fixes the line before making target path
                for letter in line[2:]:
                    if letter == "\\":
                        target += "/"
                    else:
                        target += letter
                shortcut.Targetpath = target[:-1]
                shortcut.IconLocation = "icon"
                shortcut.save()
                fixedLine = ""






    def open_folder(self):
        try:
            if os.path.exists(self.directory):
                os.system(f'start {os.path.realpath(self.directory)}')
        except OSError:
            print('Error: Directory not found')

    #gathers every file that hasn't been accessed in months
    def gather_old_files(self):
        text_file = open("OldFiles.txt", "w")


        count = 0
        least = 9999999999
        check = ""
        #os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
        for (root, dirs, files) in os.walk('/./', topdown=False, onerror=None, followlinks=False):
            for name in files:
                print(os.path.join(root, name))

                #grabs every file on the computer at the moment
                #if end of file ends with .dll then dont add it
                temp = os.path.join(root, name)


                if not temp[:11] == "/./$Recycle":
                    if temp[-4:] == ".png":
                        text_file.write(temp + "\n")
                    elif temp[-5:] == ".jpeg":
                        text_file.write(temp + "\n")
                    elif temp[-5:] == ".doc":
                        text_file.write(temp + "\n")
                    elif temp[-5:] == ".rtf":
                        text_file.write(temp + "\n")

            for filename in files:
                if os.path.exists(filename):
                    statinfo = os.stat(filename).st_mtime
                    if statinfo < least:
                        least = statinfo
                        check = filename
                    print(statinfo)
                    count += 1
        print(count)
        print(least)
        print(check)
        text_file.close()




        count = 0
        for (directory, dirs, files) in os.walk('.'):
            for filename in files:
                if filename.endswith('.txt'):
                    count = count + 1
        print('Files:', count)


    def delete_folder(self):
        try:
            if os.path.exists(self.directory):
                os.rmdir(self.directory)
        except OSError:
            print('Error: Cannot find directory' + self.directory)
