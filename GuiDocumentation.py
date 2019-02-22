# MMTGuiEngine Documentation
#
# This Document is intended to outline key features of the MMTGuiEngine so users 
# can get started making simple Gui Applications.
# 
# Their are two libraries apart of the MMTGuiEngine
# MMTGuiEngine.py and MMTGuiObjects
# 
# The former outlines scripting functions users can tack onto existing programs to easily transform
# text-based apps to Gui Applications.
#
# MMTGuiObjects.py is a reference to individual classes that each Gui object is derived from. 
# The user should not access these classes directly. They shall only exist within the main window.

#####################################################################################################

# The main class that will create the actual Gui, from this class we can customize with widgets
# All Gui Applications should begin with creating an instance of the JPLGui class

ex = Gui()

# Users can pass in an optional variable to set a title
# i.e. ex.JPLGui('Example Gui Application')

# The next section describes widgets that can be added to 
# the GUI
# All widget declarations begin by initializing with an ID
# The ID will then be transformed to a label on the actual GUI

######################################################
################# INDICATORS #########################

# Users can now add a variety of widgets to thier Gui
# You can easily add an indicator like such

ex.addIndicator('Output 1')

# we can also set an indicator with an initial value like so

ex.addIndicator('Output 2',1000)

# throughout your program you may need to update an indicator
# you can easily do so by calling the function below

ex.updateIndicator('Output 1',123456)


######################################################
################# USER INPUT #########################

# User input can be obtained from a number of widgets

# The first is the userInputBox() which a user can input
# a string, int, or float value

ex.addInputBox('Input')

# You can initialize the inputBox as well

ex.addInputBox('Input 2',199.99)

# Using the function getVal() you can return the exact 
# datatype of whatever the user entered. This function works
# for returning a value in almost all cases

ex.getVal('Input')
ex.getVal('Input2')

# in more specific cases you may need to always return a 
# string, float, or input despite what the used enters.

ex.addUserInputBox('User Input 1')
ex.getString('User Input 1')

# User input can be obtained from a SpinBox which can be intialized
# to a int or float type

ex.addSpinBox('Numeric Control 1')
ex.getInt('Numerica Control 1')

ex.addSpinBox('Numeric Control 2', 1.0)
ex.getFloat('Numeric Control 2')

# Lastly, a comboBox is perfect for implementing a visual case
# statement. The arguments given will become selectable cases in a 
# drop-down like menu format.
# NOTE: Don't forget the first argument is the WidgetID

ex.addComboBox('Control','Plot','Build','Delete','Transform')
ex.getString('Control')

######################################################
################# BUTTONS ############################

# Buttons are essential to any GUI Application
# All buttons are initalized with a button name and a 
# callback function that will execute on a button click

# i.e. add is a callback function 

ex.addButton('ADD',add)

# The user can also add LED switches that can be toggled on 
# and off
# The user can retrieve the status of the LED using the 
# getBool() function

ex.addLED('On/Off')
ex.getBool('On/Off')

######################################################
################# PLOTS ##############################

# Plots can also be added on the GUI
# For now, they will only be added to the bottom of the GUI

# Plots can be initialized with a variable number of subplots
# subplots are added simply by adding more PlotIDs in addPlot()

ex.addPlot('Plot1','Plot2','Plot3','Plot4')

# addPlot intializes an empty axes that can be updated 
# using the updatePlot function()

ex.updatePlot('Plot1','X-Axis Label','Y-Axis Label',x,y)

# You can also add multiple plots to one axes by simply

ex.updatePlot('Plot2','X','Y',x1,x2,y1,y2,[1,2,3,4],[1,10,1,10])

######################################################
#################### DIVIES ##########################

# Users can create their own Divies to ensure the Gui
# comes out how they envisioned it. 
# The divies functions only work with Widgets that 
# aren't plots so you can not embed plots anywhere but
# after all the controls and indicators

# An endRow() call will tell the Gui to place all
# widgets before the call in a row and start the next 
# set of widget on a new line
ex.endRow()

# An endCol() call will do the same as the endRow()
# call, but you guessed it! It'll place all widgets in 
# a single column instead.
ex.endCol()

# By default the Gui will add all widgets vertically
# if no divie calls are made.

######################################################
################## LAUNCH ############################

# This should be the last function the user should call
# This will assess the elements the user has added,
# create the layout, and display the Gui.
# From there, the user can interact with the Gui just
# how they intended
ex.launch()


