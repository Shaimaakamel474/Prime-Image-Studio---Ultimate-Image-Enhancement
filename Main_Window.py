import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget , QRadioButton, QButtonGroup
from PyQt5 import uic 
from Imag_Widget import ImageWidget
from PyQt5.QtWidgets import QWidget, QFileDialog
from PIL import Image, ImageQt, ImageEnhance
from numpy.fft import ifft2, ifftshift
import numpy as np
from scipy.fft import fft2, fftshift
from frequncy_domain import *
from PyQt5.QtWidgets import QVBoxLayout
from Noise_and_filter import *
from EdgeDetection import *
from frequncy_domain import *
from EnhanceImg_Display import *

# Load the UI file
Ui_MainWindow, QtBaseClass = uic.loadUiType("Main_Window_UI_2color.ui")

# Main Window
class MainWindow(QMainWindow , Ui_MainWindow ):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setupUi(self)

       # make groups for  radio buttons 
        self.Mode_group = QButtonGroup(self)
        self.Mode_group.addButton(self.RadioButton_Histogram)
        self.Mode_group.addButton(self.RadioButton_Normalizer)
        self.Mode_group.addButton(self.RadioButton_Threshold)
        self.Mode_group.addButton(self.RadioButton_Domain_Filter)
        self.Mode_group.addButton(self.RadioButton_DetectEdges)
        self.Mode_group.addButton(self.RadioButton_NoiseandFilter)
        self.Mode_group.addButton(self.RadioButton_Mixer)
        self.Remove_checked_Radios()

        self.noisy_img=None
        self.org_img=None


        
        
        
        
    



        layout = QVBoxLayout(self.Widget_Org_Image)
        self.org_ImgWidget = ImageWidget(None, self.Widget_Org_Image)
        layout.addWidget(self.org_ImgWidget)
        self.Widget_Org_Image.setLayout(layout)

        self.org_ImgWidget.image_uploaded.connect(self.on_new_image_uploaded)
       
       
        layout_2 = QVBoxLayout(self.Widget_Output_1)
        self.Output_Widget_1 = ImageWidget(None, self.Widget_Output_1)
        layout_2.addWidget(self.Output_Widget_1)
        self.Widget_Output_1.setLayout(layout_2)
      
        self.Output_Widget_1.image_uploaded.connect(self.on_new_image_uploaded)
      
        layout_3 = QVBoxLayout(self.Widget_Output_2)
        self.Output_Widget_2 = ImageWidget(None, self.Widget_Output_2)
        layout_3.addWidget(self.Output_Widget_2)
        self.Widget_Output_2.setLayout(layout_3)


        self.Combox_Edges.currentIndexChanged.connect(self.Apply_Edge_Filter)
        self.Combox_Noise.currentIndexChanged.connect(self.Apply_Noise_and_Filter)
        self.Combox_Filter.currentIndexChanged.connect(self.Apply_Noise_and_Filter)   
        self.slider_param_1.sliderReleased.connect(self.Apply_Noise_and_Filter)
        self.slider_param_2.sliderReleased.connect(self.Apply_Noise_and_Filter)
        self.slider_param_3.sliderReleased.connect(self.Apply_Noise_and_Filter)
        self.slider_freq_domain.sliderReleased.connect(self.Apply_Frequency_Filter)
        self.slider_freq_img1.sliderReleased.connect(self.Apply_hyprid_filter)
        self.slider_freq_img2.sliderReleased.connect(self.Apply_hyprid_filter)



        self.RadioButton_Histogram.clicked.connect(self.Draw_Histogram)
        self.checkBox_rgbImg.clicked.connect(self.Draw_Histogram_rgb)
        self.RadioButton_Normalizer.clicked.connect(self.Normalize_and_Equalize)
        self.RadioButton_Threshold.clicked.connect(self.Apply_Thersholding)
        self.RadioButton_NoiseandFilter.clicked.connect(self.Apply_Noise_and_Filter)
        self.RadioButton_DetectEdges.clicked.connect(self.Apply_Edge_Filter)
        self.RadioButton_Domain_Filter.clicked.connect(self.Apply_Frequency_Filter)
        self.RadioButton_Mixer.clicked.connect(self.Apply_hyprid_filter)




    def on_new_image_uploaded(self):
        selected_button = self.Mode_group.checkedButton()

        if selected_button == self.RadioButton_Histogram:
            self.Draw_Histogram()
        elif selected_button == self.RadioButton_Normalizer:
            self.Normalize_and_Equalize()
        elif selected_button == self.RadioButton_Threshold:
            self.Apply_Thersholding()
        elif selected_button == self.RadioButton_NoiseandFilter:
            self.Apply_Noise_and_Filter()
        elif selected_button == self.RadioButton_DetectEdges:
            self.Apply_Edge_Filter()
        elif selected_button == self.RadioButton_Domain_Filter:
            self.Apply_Frequency_Filter()
        elif selected_button == self.RadioButton_Mixer:
            self.Apply_hyprid_filter()
        


    def Apply_Edge_Filter(self):
        self.Set_Output_Labels("Gradient X" , "Gradient Y")
        
        curr_filter=self.Combox_Edges.currentText()
        curr_grayImg=self.org_ImgWidget.get_curr_GrayImg()
        if curr_grayImg is not None:
            if curr_filter=="Sobel":
                img_1 , img_2=Sobel_Filter(curr_grayImg)
            elif curr_filter=="Roberts":
                img_1 , img_2=Robert_Filter(curr_grayImg)
            elif curr_filter=="Prewitt":
                img_1 , img_2=Prewitt_Filter(curr_grayImg)
            elif curr_filter=="Canny":
                self.Set_Output_Labels("Gradient " , "Output_2")
                img_1 , img_2=Canny_Filter(curr_grayImg)

            self.Output_Widget_1.Set_Image(img_1)
            self.Output_Widget_2.Set_Image(img_2)
    
    def Apply_Noise(self):
        self.Set_noise_label()
        curr_noise=self.Combox_Noise.currentText()
        curr_grayImg=self.org_ImgWidget.get_curr_GrayImg()
        if curr_grayImg is not None:
            param_1=self.slider_param_1.value()
            param_2=self.slider_param_2.value()
            if curr_noise == "Gaussian":
                noisy_image = apply_gaussian_noise(curr_grayImg,param_1,param_2)
            elif curr_noise == "Uniform":
                noisy_image = apply_uniform_noise(curr_grayImg,param_1,param_2)
            elif curr_noise == "Salt and Pepper":
                noisy_image = apply_salt_and_pepper_noise(curr_grayImg,param_1/100,param_2/100)
            
            self.noisy_img=noisy_image
            self.Output_Widget_1.Set_Image(noisy_image)
            
    
    def Apply_Filter(self):
        self.handel_carnel_size()
        ksize=self.slider_param_3.value()
        curr_filter=self.Combox_Filter.currentText()
        curr_grayImg=self.noisy_img
        if self.noisy_img is not None:
            if curr_filter == "Gaussian":
                filterd_img = apply_gaussian_filter(curr_grayImg,ksize)
            elif curr_filter == "Median":
                filterd_img = apply_median_filter(curr_grayImg,ksize)
            elif curr_filter == "Average":
                filterd_img = apply_averaging_filter(curr_grayImg,ksize)
            self.Output_Widget_2.Set_Image(filterd_img)
    
    def Apply_Noise_and_Filter(self):
        self.Set_Output_Labels("Noisy Image " , "Filtered Image")
        self.Apply_Noise()
        self.Apply_Filter()

    
    
    
    
    
    def Apply_Frequency_Filter(self):
        self.Set_Output_Labels("Low Pass Filter " , "High Pass Filter")
        curr_grayImg=self.org_ImgWidget.get_curr_GrayImg()
        if curr_grayImg is not None:
            radius=self.slider_freq_domain.value()
            print(radius)
            low_pass_filterd_img = low_pass_filter(curr_grayImg,radius)
            
            high_pass_filterd_img = high_pass_filter(curr_grayImg,radius)
            self.Output_Widget_1.Set_Image(low_pass_filterd_img)
            self.Output_Widget_2.Set_Image(high_pass_filterd_img)

    def Apply_hyprid_filter(self):  
        curr_grayImg=self.org_ImgWidget.get_curr_GrayImg()
        curr_grayImg_2=self.Output_Widget_1.get_curr_GrayImg()
        self.Set_Output_Labels("Image_2" , "Hybrid Image")
        if curr_grayImg is not None and curr_grayImg_2 is not None:
            radius1=self.slider_freq_img1.value()
            radius2=self.slider_freq_img2.value()
            hyprid_img = hybrid(curr_grayImg,curr_grayImg_2,radius1,radius2)
            self.Output_Widget_2.Set_Image(hyprid_img)  





    def Draw_Histogram(self):
        self.Set_Output_Labels("Histogram" , " CDF ")
        curr_img=self.org_ImgWidget.get_curr_GrayImg()
        if curr_img is not None:
            if self.checkBox_rgbImg.isChecked():
                curr_img_rgb =self.org_ImgWidget.get_curr_RGBImg()
                self.org_ImgWidget.display_RGBImg()
                hist_bars_img, cdf_img=process_image(curr_img_rgb , mode="rgb")
            else:
                self.org_ImgWidget.display_GrayImg()
                hist_bars_img, cdf_img=process_image(curr_img, mode="gray")
            
            self.Output_Widget_1.Set_Image(hist_bars_img)
            self.Output_Widget_2.Set_Image(cdf_img)

    
    def Draw_Histogram_rgb(self):
        selected_button = self.Mode_group.checkedButton()
        if selected_button == self.RadioButton_Histogram :
            self.Draw_Histogram()
        else :
            self.org_ImgWidget.display_GrayImg()



    def Normalize_and_Equalize(self):
        self.Set_Output_Labels("Normalized Image" , " Equalized Image ")
        curr_img=self.org_ImgWidget.get_curr_GrayImg()
        if curr_img is not None:
            norm_Img=normalize_image(curr_img )
            equal_Img=equalize_image(curr_img)
            self.Output_Widget_1.Set_Image(norm_Img)
            self.Output_Widget_2.Set_Image(equal_Img)
    
    def Apply_Thersholding(self):
        self.Set_Output_Labels("Global Thershold" , " Local Thershold ")
        curr_img=self.org_ImgWidget.get_curr_GrayImg()
        if curr_img is not None:
            global_ther_Img=manual_global_threshold(curr_img )
            local_ther_Img=manual_local_threshold(curr_img)
            self.Output_Widget_1.Set_Image(global_ther_Img)
            self.Output_Widget_2.Set_Image(local_ther_Img)








    def Remove_checked_Radios(self):
        self.RadioButton_Histogram.setChecked(False) 
        self.RadioButton_Normalizer.setChecked(False) 
        self.RadioButton_Threshold.setChecked(False) 
        self.RadioButton_Domain_Filter.setChecked(False) 

    
    def Set_Output_Labels(self,label_1 , label_2=None):
        self.Label_output_1.setText(label_1)
        if label_2:
            self.Label_output_2.setText(label_2)
    def Set_noise_label(self):
        curr_label=self.Combox_Noise.currentText()
        fixed_width = 150

        self.label_param_1.setFixedWidth(fixed_width)
        self.label_param_2.setFixedWidth(fixed_width)
        if curr_label=="Salt and Pepper":
            self.label_param_1.setText("Salt Probability :   ")
            self.label_param_2.setText("Pepper Probability : ")
            self.slider_limit(self.slider_param_1)
            self.slider_limit(self.slider_param_2)

        elif curr_label=="Gaussian":   
            self.label_param_1.setText("Mean :               ")
            self.label_param_2.setText("Variance :           ")
            self.slider_limit(self.slider_param_1)
            self.slider_limit(self.slider_param_2,min=1)

        elif curr_label =="Uniform":                         
            self.label_param_1.setText("Min Value :          ")
            self.label_param_2.setText("Max Value :          ")
            self.slider_limit(self.slider_param_1)
            self.slider_limit(self.slider_param_2)


    def slider_limit(self,slider,min=0,max=100,step=1):
        slider.setMinimum(min)
        slider.setMaximum(max)
        slider.setSingleStep(step)

    def handel_carnel_size(self):
        value=self.slider_param_3.value()
        if value%2==0:
            value=value+1
        self.slider_param_3.setValue(value)

if __name__=="__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    

    mainWindow.show()
    sys.exit(app.exec_())
