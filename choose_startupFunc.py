# choose_startupFunc.py

# pywin32 install required

import easygui
import os
import win32com.client

# allow user to select programs to be loaded on computer startup

# adds a chosen program to startup file
def add_to_startup():
    
    #have the user select a program to add
    target_path = easygui.fileopenbox('Which program would you like to run on startup')
    
    # if user fails to select a program, exit function early
    if target_path is None:
        print('no file selected')
        return
    
    # folder containing all programs that should run at startup
    startup_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup'
    
    # make the shortcut name (same name as original program, but with .lnk extension)
    file_name = os.path.basename(target_path).split('.')[0]
    shortcut_name = (file_name + '.lnk')
    
    # the path for the new shortcut, will be in the startup folder
    path = os.path.join(startup_path, shortcut_name)
    
    # create the shortcut - will now run at startup
    try:
        shortcut = win32com.client.Dispatch("WScript.Shell").CreateShortCut(path)
        shortcut.Targetpath = target_path
        shortcut.WorkingDirectory = os.path.dirname(target_path)
        shortcut.save()
    except OSException:
        print('Error: unable to create shortcut')
        return
    
    print('Added program ' + file_name + ' to startup programs')

# removes a chosen program from the startup file
def remove_from_startup():
    
    startup_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup'
    
    print('enter the name of the program to remove from the list above: ', end = '')
    selected_program = input() + '.lnk'
    program_path = startup_path + '/' + selected_program
    
    # if the file doesn't exist, exit early
    if not os.path.exists(program_path):
        print('program not found')
        return
    
    # remove the (shortcut) file - will no longer run at startup
    try:
        os.remove(program_path)
    except OSError:
        print("Error: removing file")
        return
    
    print('Removed program ' + selected_program + ' from startup programs')

# have user select if they want to add or remove programs to run on startup
def choose_startupprograms():
    
    # first, list current startup programs
    print('Current Startup Programs: ')
    startup_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup'
    
    for file in os.listdir(startup_path):
        if file.endswith(".lnk"):
            # show the program, without .lnk at the end
            print('\t' + file.split(".lnk")[0])
    
    # either add a new program, or remove an existing one from the startup folder
    print('Would you like to add or remove a program from the list? (a/r): ', end = '')
    answer = input()
    
    if answer == 'a' or answer == 'add':
        add_to_startup()
    elif answer == 'r' or answer == 'remove':
        remove_from_startup()
    else:
        print("unrecognized command, next time enter 'a' or 'r'")
