# MMTGuiObjects.py
#
# PyQt5 Wrapper Classes for Gui Objects
# Classes are used in MMTGuiEngine Create Functions
# JPL Twist on PyQt5 Widget Classes
#
# Mundo Guzman
# 8/7/2018

#######################
# Dependencies
#######################
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph as pg
import pyqtgraph.exporters

###################################################################################################
#
#   Creates Button
#
###################################################################################################

class JPLButton(QPushButton):

    def __init__(self,mainwindow,buttonID,funcName,size):
        super().__init__(buttonID,mainwindow)
        self.id = buttonID
        
        # Creates LED Switch version of button
        if(funcName == None):
            self.switch = False
            self.clicked.connect(self.Switch)
        # Creates Regular Button
        else:
            self.clicked.connect(funcName)

        if (size == "l"):
            width = 180
            height = 100
        elif (size == "m"):
            width = 150
            height = 60
        else:
            width = 120
            height = 25

        self.setFixedWidth(width)
        self.setFixedHeight(height)

    #########################################
    #   Turns LED on and off
    #########################################

    def Switch(self):
        # Flip bool value each time its called
        self.switch = not self.switch
        # If OFF then use default button color
        if (self.switch != True):
            self.setStyleSheet('')
        # If ON use LED
        else:
            self.setStyleSheet('background-color:rgb(144,238,144)' ';color:black')

###################################################################################################
#
#   Creates Indicator 
#
###################################################################################################

class JPLIndicator(QLineEdit):

    def __init__(self,mainwindow,indicatorID,output):
        super().__init__(mainwindow)
        self.id = indicatorID

        if (output == str(None)):
            self.setText('')
        else:
            self.setText(output)

        self.resize(10,10)
        self.setFixedWidth(120)
        self.setReadOnly(True)
        self.setStyleSheet('background-color:rgb(103, 111, 112)' ';color:white')

###################################################################################################
#
#   Creates User Input Box
#
###################################################################################################

class JPLUserInput(QLineEdit):

    def __init__(self,mainwindow,userInputID,value):
        super().__init__(mainwindow)
        self.id = userInputID

        self.setFixedWidth(120)
        self.setText(value)

###################################################################################################
#
#   Creates SpinBox
#
###################################################################################################

class JPLSpinBox(QDoubleSpinBox):

    def __init__(self,mainwindow,userInputID,value):
        super().__init__(mainwindow)
        self.id = userInputID

        self.setFixedWidth(120)
        # Determines if Int or Float
        if (isinstance(value,int)):
            prec = 0
            maximum = value * 10000
            step = 1

            if (value > 1000):
                step = 10

        elif (isinstance(value,float)):
            # Finds out how many numbers are after Decimal
            val = str(value)
            if not '.' in val:
                prec = 0
            prec = len(val) - val.index('.')
            step = float('.' + ((prec-1) * '0') + '1')
            maximum = 10000

        # Sets proper precision, step-size, and range
        self.setDecimals(prec)
        self.setSingleStep(step)
        self.setRange(0,maximum)
        self.setValue(value)

###################################################################################################
#
#   Creates ComboBox
#
###################################################################################################

class JPLComboBox(QComboBox):

    def __init__(self,mainwindow,boxID,*args):
        super().__init__(mainwindow)
        self.id = boxID

        for arg in args:
            self.addItem(arg)
            

###################################################################################################
#
#   Creates Plot
#
###################################################################################################

class JPLPlot(FigureCanvas):
    __width=5 
    __height=4
    __dpi=100

    def __init__(self,parent, *args):
        self.ids = list()
        self.axes = list()


        for arg in args:
            self.ids.append(arg)

        fig = Figure(figsize=(JPLPlot.__width, JPLPlot.__height), dpi=JPLPlot.__dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        for i in range(0,len(self.ids)):
            self.axes.append(fig.add_subplot(1,len(self.ids),i+1))

    def plot(self,plotID,x,y,xlabel,ylabel):
        i = 0
        for axe in self.axes:
            if (plotID == self.ids[i]):
                self.axes[i].clear()
                self.axes[i] = self.figure.add_subplot(1,len(self.ids),i+1)
                self.axes[i].plot(x,y)
                self.axes[i].set_xlabel(xlabel)
                self.axes[i].set_ylabel(ylabel)
                self.draw()
            i += 1
            
###################################################################################################
#
#   Creates Label
#
###################################################################################################

class JPLLabel(QLabel):

    def __init__(self,mainwindow,labelID):
        super().__init__(mainwindow)
        self.id = labelID
        self.setText(str(labelID))

###################################################################################################
#
#   Creates FileInputDialogBox
#
###################################################################################################

class JPLFileDialog(QFileDialog):

    def __init__(self,mainwindow):
        super().__init__(mainwindow)

###################################################################################################
#
#   Creates Custom Divide in Grid Layout
#
###################################################################################################

class JPLDivies():

    def __init__(self,mytype,numobjects):

        self.type = mytype
        self.numobjects = numobjects
