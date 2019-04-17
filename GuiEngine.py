# MMTGuiEngine.py
#
# PyQt5 Wrapper Class 
# Easily create Gui Applications on top of existing programs
#
#
# Mundo Guzman
# 6/29/2018

#######################
# Dependencies
#######################
import sys
from GuiObjects import *

# Must Create a QApplication before a QWidget
app = QApplication(sys.argv)

###################################################################################################
#
#   Creates Gui Application
#
###################################################################################################

class Gui(QWidget):

    # Pass in Title of GUI Application
    def __init__(self, title = 'Gui'):
        super().__init__()

        self.title = title
        # Create lists to hold Gui Widgets, Plots, Labels, and Divies
        self.GuiObjects = list()
        self.labels = list()
        self.plots = list()
        self.divies = list()
        # Number of objects since last Divie
        self.lastDivie = 0
        # Call Initialize Function
        self.__initUI()
        
        self.startup_gui = None
        self.helpmenu_gui = None


    #########################################
    #   Initializes GUI 
    #########################################

    def __initUI(self):

        self.setWindowTitle(self.title)
        self.move(100,100)
        
    #########################################
    #   Adds Button to GUI
    #########################################

    def addButton(self,buttonID,funcName,size = 's'):

        # Add Widget to Gui Objects List
        self.GuiObjects.append(JPLButton(self,buttonID,funcName,size))
        self.labels.append(JPLLabel(self,""))

    #########################################
    #   Adds LED Switch to GUI  
    #########################################

    def addLED(self,buttonID,funcName = None,size = 's'):

        self.GuiObjects.append(JPLButton(self,buttonID,funcName,size))
        self.labels.append(JPLLabel(self,""))
        
    #########################################
    #   Adds Indicator to GUI
    #########################################

    def addIndicator(self,indicatorID,output = None):

        self.GuiObjects.append(JPLIndicator(self,indicatorID,str(output)))
        self.labels.append(JPLLabel(self,indicatorID))
      
    #########################################
    #   Updates an existing Indicator on GUI
    #########################################

    def updateIndicator(self,indicatorID,output):

        i = 0
        # Searches for Gui Object given an ID
        for objects in self.GuiObjects:
            if (self.GuiObjects[i].id == indicatorID):
                # Once found, set the Indicator 
                self.GuiObjects[i].setText(str(output))
            i += 1
        QApplication.processEvents()

    #########################################
    #   Adds InputBox to GUI (takes any type) 
    #########################################

    def addInputBox(self,userInputID,value = None):

        self.GuiObjects.append(JPLUserInput(self,userInputID,value))
        self.labels.append(JPLLabel(self,userInputID))

    #########################################
    #   Adds Spinbox to GUI  
    #########################################
    
    def addSpinBox(self,userInputID,value = 0):

        self.GuiObjects.append(JPLSpinBox(self,userInputID,value))
        self.labels.append(JPLLabel(self,userInputID))

    #########################################
    #   Adds ComboBox to GUI  
    #########################################

    def addComboBox(self,menuID,*args):

        self.GuiObjects.append(JPLComboBox(self,menuID,*args))
        self.labels.append(JPLLabel(self,menuID))

	#########################################
    #   Adds Label to GUI  
    #########################################

    def addLabel(self,labelID):

        self.GuiObjects.append(JPLLabel(self,labelID))
        self.labels.append(JPLLabel(self,''))

    #########################################
    #   Adds Plot Axes to GUI  
    #########################################

    def addPlot(self,*args):
        self.plots.append(JPLPlot(self,*args))

    #########################################
    #   Updates Plot on GUI  
    #########################################

    def updatePlot(self,plotID,x,y,xlabel = None, ylabel = None):
        self.plots[0].plot(plotID,x,y,xlabel,ylabel)
        QApplication.processEvents()

    #########################################
    #   Returns Int
    #########################################
    
    def getInt(self,userInputID):

        i = 0
        for objects in self.GuiObjects:
            if(self.GuiObjects[i].id == userInputID):
                try:
                    if self.GuiObjects[i].text():
                        return int(self.GuiObjects[i].text())

                except ValueError:
                    print('WARNING: getInt() did not receive input of type INT.' +
                        ' Check input or consider using getString() or getFloat()')
                    return 'NaN'
            i+=1

    #########################################
    #   Returns Float
    #########################################
    
    def getFloat(self,userInputID):

        i = 0
        for objects in self.GuiObjects:
            if(self.GuiObjects[i].id == userInputID):
                try:
                    if self.GuiObjects[i].text():
                        return float(self.GuiObjects[i].text())

                except ValueError:
                    print('WARNING: getFloat() did not receive input of type FLOAT.' +
                        ' Check input or consider using getString()')
                    return 'NaN'
            i+=1

    #########################################
    #   Returns Bool
    #########################################

    def getBool(self,buttonID):

        i = 0
        for objects in self.GuiObjects:
            if (self.GuiObjects[i].id == buttonID):
                try:
                    # Return True or False
                    return self.GuiObjects[i].switch
                except ValueError:
                    print('WARNING: getBool() did not receive input of type BOOL.' +
                        ' Check input or consider using getString()')
                    return 'NaN'
            i += 1
        
    #########################################
    #   Returns String
    #########################################

    def getString(self,userInputID):

        i = 0
        for objects in self.GuiObjects:
            if(self.GuiObjects[i].id == userInputID):
                try:
                    if self.GuiObjects[i].text():
                        return self.GuiObjects[i].text()

                except ValueError:
                    print('WARNING: getString() did not receive input of type String')
                    return 'NaN'
            i+=1            

    #########################################
    #   Returns Value of any type
    #########################################

    def getVal(self,userInputID):
        i = 0
        for objects in self.GuiObjects:
            if(self.GuiObjects[i].id == userInputID):
                try:
                    return self.getInt(userInputID)
                except TypeError:
                    pass
                try:
                    return self.getFloat(userInputID)
                except TypeError:
                    pass
                try:
                    return self.getString(userInputID)
                except TypeError:
                    print('WARNING: Unrecognized type.')
                    return 'NaN'
            i+=1   
    
    #########################################
    #   Function Creates Grid Layout
    #########################################

    def __createGridLayout(self):

        Vlayout = QVBoxLayout()

        if self.lastDivie == 0:
            Vlayout.setContentsMargins(25,25,25,25)
            i = 0
            for objects in self.GuiObjects:
                Vlayout.addWidget(self.labels[i])
                Vlayout.addWidget(self.GuiObjects[i])
                i += 1
            i = 0
            if len(self.plots) > 0:
                for plot in self.plots:
                    Vlayout.addWidget(self.plots[i])
                    i+=1

        else:       
            # Create Gui Grid Layout Widget
            layout = QGridLayout()
            layout.setColumnStretch(1, 4)

            i = 0
            j = 0
            k = 0
            m = 0
            n = 0
            tmp = 0
            for divie in self.divies:
                if (self.divies[i].type == 'row'):
                    for j in range(0,self.divies[i].numobjects):
                        layout.addWidget(self.labels[n],k,m+j)
                        layout.addWidget(self.GuiObjects[n],k+1,m+j)
                        n+=1
                    k+=2

                elif(self.divies[i].type == 'col'):
                    tmp = k
                    for j in range(0,self.divies[i].numobjects):
                        tmp+=j
                        layout.addWidget(self.labels[n],tmp,m)
                        layout.addWidget(self.GuiObjects[n],tmp+1,m)
                        tmp+=1
                        n+=1
                    m+=1
                i+=1
            Vlayout.addLayout(layout)
            i = 0
            if len(self.plots) > 0:
                for plot in self.plots:
                    Vlayout.addWidget(self.plots[i])
                    i+=1

        # Set the layout that you just created
        self.setLayout(Vlayout)

    #########################################
    #   Functions Create Divies in the Layout
    #########################################

    def endCol(self):

        # Find number of GUI objects since last divie call
        num = 0
        for objects in self.GuiObjects:
            num+=1
        distance = num - self.lastDivie
        self.divies.append(JPLDivies('col',distance))
        self.lastDivie = num

    def endRow(self):

        # Find number of GUI objects since last divie call
        num = 0
        for objects in self.GuiObjects:
            num+=1
        distance = num - self.lastDivie
        self.divies.append(JPLDivies('row',distance))
        self.lastDivie = num

    #########################################
    #   Function to run JPL Gui
    #########################################

    def launch(self):   

        self.__createGridLayout()
        # Display the GUI
        self.show()
        # System call to execute the QApplication
        sys.exit(app.exec_())


