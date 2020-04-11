#imports 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import caffe
import my_custom_io
import wrapper_net

from PyQt4 import QtGui
import sys
import Initial_Window
import graphics_module
import read_values_online
import cv2 # SOLO PARA PROBAAR!

class Controlador:
	app=0
	IWindow=0
	ControlPanelWindow=0
    	network_file=''
        weights_file=''
        images_path=''
        load_file=''
   	reader_object = None	
	def __init__ (self):
		caffe.set_mode_cpu()
		self.app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
        	self.IWindow = graphics_module.IWindow(self)                
        	self.IWindow.show()                         # Show the form
        	self.app.exec_()

	def change_to_get_statistics(self, current_network_file, current_weights_file, current_image_path, windows_path):
		windows_path.close()
		self.network_file=current_network_file
		self.weights_file=current_weights_file
		self.images_path=current_image_path
		Statistics_Window=graphics_module.StatisticsWindow(self)
                Statistics_Window.show()
		self.IWindow.hiden()
                self.IWindow.close()
		
		
	def start_getting_data_online(self, window):
		window.close()
		print('Se ejecuta modo online')
		self.reader_object=read_values_online.read_values_online()
		self.reader_object.init_net(self.network_file, self.weights_file, self.images_path) #valores actualizados en change_to_get_statistics
		self.ControlPanelWindow=graphics_module.ControlPanel_Window(self)
		self.ControlPanelWindow.show()
		self.IWindow.hiden()		

	def start_getting_general_statistics(self):
		self.reader_object=read_values_online.read_values_online()
                self.reader_object.init_net(self.network_file, self.weights_file, self.images_path) #valores actualizados en change_to_get_statistics	
	def get_next_image_online(self):
		ok, blobs, image_name, params, layers, layer_names = self.reader_object.get_next_data()
		return ok, blobs, image_name, params, layers, layer_names

	def start_getting_data_from_file(self, load_file, window):
		window.close()
                self.load_file = load_file

	def write_file(self, network_file, weights_file, images_path, window): # El archivo lo escribira en la ruta actual
		window.close()
		print('Se ejecuta escritura en fichero')
                self.network_file=network_file
                self.weights_file=weights_file
                self.images_path=images_path
		#SOLO PARA PROBAR!!
		#images_list = my_custom_io.get_list_images(self.images_path)
		#img = cv2.imread(self.images_path+images_list[0])
		img = np.zeros((512,512), np.uint8)
		graphics_module.Draw_fmap(img, 10)
		#print(self.images_path+images_list[0])
		#cv2.imshow('image', img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()		


	def restart_getting_data_online(self):
		self.reader_object.restart_net() #Empieza a contar desde la imagen 0 de nuevo
	

		
		
