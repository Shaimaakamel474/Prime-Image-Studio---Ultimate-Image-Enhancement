import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget , QRadioButton, QButtonGroup
from PyQt5 import uic 
from Imag_Widget import ImageWidget
from PyQt5.QtWidgets import QWidget, QFileDialog
from PIL import Image, ImageQt, ImageEnhance
from numpy.fft import ifft2, ifftshift
import numpy as np
from scipy.fft import fft2, fftshift
import logging


# Load the UI file
Ui_MainWindow, QtBaseClass = uic.loadUiType("Main.ui")

# Main Window
class MainWindow(QMainWindow , Ui_MainWindow ):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setupUi(self)

       # make groups for  radio buttons 
        Mode_group = QButtonGroup(self)
        Mode_group.addButton(self.RadioButton_Histogram)
        Mode_group.addButton(self.RadioButton_Normalizer)
        Mode_group.addButton(self.RadioButton_Threshold)
        Mode_group.addButton(self.RadioButton_Domain_Filter)
        self.Remove_checked_Radios()




        self.org_Image = ImageWidget(None, self.Widget_Org_Image)
        self.org_Image.setGeometry(self.Widget_Org_Image.geometry())
        self.org_Image.setParent(self)
        



    def Remove_checked_Radios(self):
        self.RadioButton_Histogram.setChecked(False) 
        self.RadioButton_Normalizer.setChecked(False) 
        self.RadioButton_Threshold.setChecked(False) 
        self.RadioButton_Domain_Filter.setChecked(False) 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
