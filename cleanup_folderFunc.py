import os


class CleanUp:
    def __init__(self):
        self.directory = './Old_Files/'


    def create_folder(self):
        try:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        except OSError:
            print('Error: Creating directory' + self.directory)

    def open_folder(self):
        try:
            if os.path.exists(self.directory):
                os.system(f'start {os.path.realpath(self.directory)}')
        except OSError:
            print('Error: Directory not found')

    #gathers every file that hasn't been accessed in months
    def gather_old_files(self):
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
