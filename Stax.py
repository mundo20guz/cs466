#Stax
#part 1: search the desktop for .png, .jpg, and .gif files, then move them into a new desktop folder labeled "pics"
#part 2: search the desktop for .doc, .pdf, .rtf, and .txt files, then move them into a new desktop folder labeled "docs"m

import os
import shutil

class Stax():
    def __init__(self):
        self.desktop_file_list = os.listdir(os.path.expanduser("~\\Desktop"))
        if not os.path.exists(os.path.expanduser("~\\Desktop") + "\\PictureStax"):
            os.makedirs(os.path.expanduser("~\\Desktop") + "~\\PictureStax")
        if not os.path.exists(os.path.expanduser("~\\Desktop") + "\\DocumentStax"):
            os.makedirs(os.path.expanduser("~\\Desktop") + "\\DocumentStax")

        self.dox = os.path.expanduser("~\\Desktop") + "\\DocumentStax"
        self.pix = os.path.expanduser("~\\Desktop") + "\\PictureStax"

    def stack(self): #group files on the desktop into folders based on file type
        for i in self.desktop_file_list:
            if i.endswith('.png') or i.endswith('.jpg') or i.endswith('.gif'):   #check pictures first
                shutil.move(src=os.path.expanduser("~\\Desktop") + "\\" + i, dst=self.pix)
            if i.endswith('.docx') or i.endswith('.pdf') or i.endswith('.rtf') or i.endswith('.txt'):   #check docs first
                shutil.move(src=os.path.expanduser("~\\Desktop") + "\\" + i, dst=self.dox)

    def unstack(self):
        if os.path.exists(self.pix):  #unstack pictures
            pix_file_list = os.listdir(os.path.expanduser("~\\Desktop" + "\\PictureStax"))
            for e in pix_file_list:
                shutil.move(src=self.pix + "\\" + e, dst=os.path.expanduser("~\\Desktop"))
        if os.path.exists(self.dox): #unstack documents
            dox_file_list = os.listdir(os.path.expanduser("~\\Desktop" + "\\DocumentStax"))
            for o in dox_file_list:
                shutil.move(src=self.dox + "\\" + o, dst=os.path.expanduser("~\\Desktop"))







test = Stax()
test.stack()


