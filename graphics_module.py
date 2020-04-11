
from PyQt4 import QtGui
import sys
import Initial_Window
import Select_Paths_Window
import easygui as eg
import Load_File_Path_Window
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import cv2
import ControlPanel_Window
import Statistics_Menu_Windows
import os
import datetime
import StatisticPanel
import GeneralStatisticControlPanel
import time
import collections
import shutil
class ControlPanel_Window(QtGui.QMainWindow, ControlPanel_Window.Ui_ControlPanel):
	 controlador=1
	 blobs=1
	 imname=1
	 dir_str=''
	 def LayerIndexChanged(self):
		print('Se ejecuta layerindexchanged')
		currentLayer = str(self.LayerComboBox.currentText())		
		#Borramos los fmaps anteriores
		self.FmapComboBox.clear()
		#Anadimos los nuevos para esa capa
		
		Fmap_list=['']
		if(currentLayer != ''):
                	for i in range(0, self.blobs[currentLayer].data.shape[1]): #la primera capa
                        	Fmap_list.append(str(i))
                self.FmapComboBox.addItems(Fmap_list) #esto llama automaticamente a FmapIndexChanged
		#self.print_current_state()

	 def FmapIndexChanged(self):
		print('Se ejecuta fmapindexchanged')
		self.print_current_state()
	 def print_current_state(self):
		cv2.destroyAllWindows() #eliminamos las imagenes actuales 
		plt.close()
		if(self.ShowSpinBox.isChecked()):
			if(self.LayerComboBox.count()>0):
				currentLayer = str(self.LayerComboBox.currentText())
				if(currentLayer != ''):
					nfmaps=self.blobs[currentLayer].data.shape[1]
					for i in range(0, nfmaps):
						currentFmap=self.blobs[currentLayer].data[0][i]
						accuracy = self.AccuracySpinBox.value()
						Draw_fmap(currentFmap, self.imname, currentLayer, str(i), self.dir_str)
						#Draw_Histogram(image_clases, self.imname, currentLayer, str(i), self.dir_str)

		else:
			if((self.FmapComboBox.count()>0) and (self.LayerComboBox.count()>0)): #Esto lo hacemos por el clear
				currentLayer = str(self.LayerComboBox.currentText())
				currentFmap_str = str(self.FmapComboBox.currentText())
				if(currentLayer != '' and currentFmap_str != ''):
					currentFmap= int(currentFmap_str)
					accuracy = self.AccuracySpinBox.value() #Cogemos el nivel de precision a nivel de pixel actual
					print('Datos a mostrar:')
					print(currentLayer)
					print(currentFmap)
					current_fmap = self.blobs[currentLayer].data[0][currentFmap] #batch=1 since there is just one image.
					Draw_fmap(current_fmap, self.imname, currentLayer, currentFmap_str, self.dir_str)
					#Draw_Histogram(image_clases, self.imname, currentLayer, currentFmap_str, self.dir_str) #Esto pintara el histograma junto con la imagen
	 def change_image(self): #Las capas convolucionales no cambian
		print('Comenzando a cambiar de imagen')
		ok, self.blobs, self.imname=self.controlador.get_next_image_online()
		if(ok==True):
                        self.FmapComboBox.clear()
			Fmap_list=['']
			if(self.LayerComboBox.currentText() != ''):
                		for i in range(0, self.blobs[str(self.LayerComboBox.currentText())].data.shape[1]): #la primera capa
                        		Fmap_list.append(str(i))
                	self.FmapComboBox.addItems(Fmap_list)
                	self.print_current_state()
		else:
			print('No quedan mas imagenes!')

	 def showSpinBoxChanged(self):
		if(self.ShowSpinBox.isChecked()):
			self.FmapComboBox.setVisible(False)
			self.print_current_state()
		else:
			self.FmapComboBox.setVisible(True)
			

					
	 def __init__(self, controlador):
                super(self.__class__, self).__init__()
                self.setupUi(self)
                self.controlador=controlador
		ok, self.blobs, self.imname, params, layers, layer_names=self.controlador.get_next_image_online()
		if(ok==False):
			print('No hay mas imagenes!') #TODO esto despues se tratara ocultando el boton de siguiente
		#Rellenamos el ComboBox Layer con las capas de la red
                self.LayerComboBox.clear() #Borramos lo que hay por defecto

		layer_list=['']
		for key in self.blobs:
			layer_list.append(key)
		
		self.LayerComboBox.addItems(layer_list)
		
		#Rellenamos el ComboBox Fmap con los fmaps de cada capa
		Fmap_list=['']
                self.FmapComboBox.clear()
		self.FmapComboBox.addItems(Fmap_list)
		self.LayerComboBox.currentIndexChanged.connect(self.LayerIndexChanged)
		self.FmapComboBox.currentIndexChanged.connect(self.FmapIndexChanged)
		self.NextTestButton.clicked.connect(self.change_image)
		now = datetime.datetime.now()
                self.dir_str='Graphs_Simulation_'+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)+'_'+str(now.second)+'_Specific'
                os.mkdir(self.dir_str)
		self.ShowSpinBox.stateChanged.connect(self.showSpinBoxChanged)

		#self.print_current_state()
			
		

class Load_File_Path_Window(QtGui.QMainWindow, Load_File_Path_Window.Ui_SelectPaths):
	controlador=1
	def read_file_path(self):
		extension=['*']
		path=eg.fileopenbox(msg='Select the File To Load', title='Select a File', default='', filetypes=extension)
                self.FileLoadLineEditor.setText(path)

	def path_accept(self):
		error=0
                self.FileLoadLineEditor.setStyleSheet("background-color: white")
                current_load_file=str(self.FileLoadLineEditor.text())
                if(current_load_file==''):
                        self.FileLoadLineEditor.setStyleSheet("background-color: red")
			error=error+1
		if(error == 0):
                	self.controlador.start_getting_data_from_file(current_load_file, self) #La ventana la cierra el controlador
                	

	def path_cancel(self):
		self.close()
	

	def __init__(self, controlador):
                super(self.__class__, self).__init__()
		self.setupUi(self)
                self.FileLoadButton.clicked.connect(self.read_file_path)
		self.acceptLoadFileButton.accepted.connect(self.path_accept)
                self.acceptLoadFileButton.rejected.connect(self.path_cancel)
		self.controlador=controlador
	



class Select_Paths_Window(QtGui.QMainWindow, Select_Paths_Window.Ui_SelectPaths):
	controlador=1 # Only for making it suitable to the type (we could simply put a number since python is dynamic type
	mode=0
	def read_network_file(self):
		extension=["*"]
		archivo=eg.fileopenbox(msg='Select the Network Definition File', title='Select a File', default='', filetypes=extension)
		self.NetworkFileLineEditor.setText(archivo)

	def read_weights_file(self):
                extension=["*"]
                archivo=eg.fileopenbox(msg='Select the Weights Definition File', title='Select a File', default='', filetypes=extension)
                self.WeightsLineEdit.setText(archivo)

	def read_image_path(self):
                path=eg.diropenbox(msg='Select the Images Path', title='Select a Path', default='.')
                self.ImagePathLineEdit.setText(path)

	def path_accept(self):
		error = 0
		self.NetworkFileLineEditor.setStyleSheet("background-color: white")
		self.WeightsLineEdit.setStyleSheet("background-color: white")
		self.ImagePathLineEdit.setStyleSheet("background-color: white")
		current_network_file=str(self.NetworkFileLineEditor.text())
		current_weights_file=str(self.WeightsLineEdit.text())
		current_image_path=str(self.ImagePathLineEdit.text())
		if(current_network_file==''):
			self.NetworkFileLineEditor.setStyleSheet("background-color: red")
			error = error + 1
		if(current_weights_file==''):
                        self.WeightsLineEdit.setStyleSheet("background-color: red")
			error = error +1
		if(current_image_path==''):
			self.ImagePathLineEdit.setStyleSheet("background-color: red")
			error = error + 1
		if(error == 0):
			if(self.mode==0): #mode = 0 getting data from data online
				#self.controlador.start_getting_data_online(current_network_file, current_weights_file, current_image_path, self)
				self.controlador.change_to_get_statistics(current_network_file, current_weights_file, current_image_path, self)

			elif(self.mode==1):#mode = 0 getting data and write it in a file
				self.controlador.write_file(current_network_file, current_weights_file, current_image_path, self)



	def path_cancel(self):
		self.close()
	
	def __init__(self, controlador, mode):
		super(self.__class__, self).__init__()
		self.setupUi(self) 
		self.NetworkFileButton.clicked.connect(self.read_network_file)
		self.WeightsButton.clicked.connect(self.read_weights_file)
		self.ImagePathButton.clicked.connect(self.read_image_path)
		self.buttonBox.accepted.connect(self.path_accept)
		self.buttonBox.rejected.connect(self.path_cancel)		
		self.controlador = controlador
		self.mode=mode

class GeneralStatisticControlPanel(QtGui.QMainWindow,GeneralStatisticControlPanel.Ui_GeneralStatisticControlPanel):
	controlador=1
	statisticValue=0
	initial_blob=1 #Solo para la parte onlyOneCheck
	initial_ok=1
	first_blob=1
	first_params=1
	params=1
	#Esta funcion devuelve la estadistica seleccionada por el usuario usando los datos recogidos en el algoritmo de segmentacion de fmaps
	def calculate_current_value(self, pixeles, accuracy, statistic):
		if(statistic==0): #Pixeles por clase
			img_custom, library=generate_segments(pixeles, accuracy)
			num_clases=len(library)
                        height, weight=pixeles.shape
                        n_pixeles=height*weight
                        pixeles_per_clase=n_pixeles/num_clases
			return pixeles_per_clase
		if(statistic==1): #Porcentaje de pixeles por clase respecto al total (este porcentaje puede ser pequeno)
			img_custom, library=generate_segments(pixeles, accuracy)
			num_clases=len(library)
                        height, weight=pixeles.shape
                        n_pixeles=height*weight
                        pixeles_per_clase=n_pixeles/num_clases
			percent=(pixeles_per_clase/n_pixeles)*100
			return percent
		if(statistic==2): #Minimo valor del fmap
			return np.amin(pixeles)

		if(statistic==3): #Maximo valor del fmap
			return np.amax(pixeles)
		if(statistic==4):
			return np.mean(pixeles)
		if(statistic==5):
			return np.std(pixeles)
				
	def get_axis_parameters(self, accuracy):
		x='N. Images'
		if(self.statisticValue==0):
			y='Average number of pixels per cluster'
			title='Pixels/cluster acc='+str(accuracy)
	
		if(self.statisticValue==1):
			y='Percentage of Repeated Pixels'
			title='% of Consecutive Pixels with an Accuracy of '+str(accuracy)
		if(self.statisticValue==2):
			y='Minimum Value of Fmap'
			title='Minimum Value of Fmap'
		if(self.statisticValue==3):
			y='Maximum Value of Fmap'
                        title='Maximum Value of Fmap'
		if(self.statisticValue==4):
			y='Average Value of Fmap'
                        title='Average Value of Fmap'
		if(self.statisticValue==5):
			y='Std Value of Fmap'
			title='Std Value of Fmap'
		return x, y, title
	
	def contar_veces(self, elemento, lista):
		num_veces=0
		for i in lista:
			if(elemento==i):
				num_veces+=1
		return num_veces
	def calculateSimilarity(self, fmap1, fmap2, accuracy):
		height=fmap1.shape[0]
        	weight=fmap2.shape[1]
		size_fmap=height*weight
		similar_values=0
		for i in range(0, height):
			for j in range(0, weight):
				diff=abs(fmap1[i,j]-fmap2[j,j]);
				if(diff<=accuracy):
					similar_values=similar_values+1
		similarity=similar_values*100
		similarity=similarity/size_fmap
		return similarity
	
	def contar_repeticiones_consecutivas(self, array, size_h, size_w, channels):
		diccionario_rep_consecutivas={}
		grupo_actual=0
		n_activaciones_repetidas=1
		size_array=size_h*size_w
		porcentaje_activaciones_repetidas_consecutivas_por_channel=[]
		for d in range(0, channels):
			n_activaciones_repetidas=0 #reseteamos por canal
			grupo_actual=0 #reseteamos el grupo actual
			diccionario_rep_consecutivas={} #reseteamos el diccionario
			for x_h in range(0, size_h):
				#El primer elemento de la nueva fila lo comparamos con el ultimo de la anterior (siempre y cuando haya anterior)
                                if(x_h > 0): #Si no es la primera fila...
                                	if(array[d][x_h][0]==array[d][x_h-1][size_w-1]):
                                        	n_activaciones_repetidas=n_activaciones_repetidas+1
                                        else:
                                        	diccionario_rep_consecutivas[grupo_actual]=n_activaciones_repetidas
                                        	grupo_actual=grupo_actual+1
                                                n_activaciones_repetidas=1

				for x_w in range(1, size_w): #empezamos 1 activacion por delante hasta el final que se compara con la siguinete fila
					#El primer elemento de la nueva fila lo comparamos con el ultimo de la anterior (siempre y cuando haya anterior)
					if(array[d][x_h][x_w]==array[d][x_h][x_w-1]):
						n_activaciones_repetidas=n_activaciones_repetidas+1
					else:
						#guardamos el grupo que acaba de terminar
						diccionario_rep_consecutivas[grupo_actual]=n_activaciones_repetidas
						grupo_actual=grupo_actual+1
						n_activaciones_repetidas=1

						
			#Guardamos el grupo al acabar el canal		
			diccionario_rep_consecutivas[grupo_actual]=n_activaciones_repetidas
                        grupo_actual=grupo_actual+1
                        n_activaciones_repetidas=1
			#Calculamos el porcentaje de repetidos en ese canal
			n_activaciones_repetidas_consecutivas=size_array / float(len(diccionario_rep_consecutivas))
			porcentaje_activaciones_repetidas_consecutivas=n_activaciones_repetidas_consecutivas*100
			porcentaje_activaciones_repetidas_consecutivas=porcentaje_activaciones_repetidas_consecutivas / float(size_array)
			porcentaje_activaciones_repetidas_consecutivas_por_channel.append(porcentaje_activaciones_repetidas_consecutivas)
		return porcentaje_activaciones_repetidas_consecutivas_por_channel
					
		
	def contar_repeticiones_y_ceros(self, array, comienzo_h, comienzo_w, size_h, size_w, channels):
		#print(array.shape)
		#print('channels: '+str(channels))
		diccionario_rep_per_window={} #diccionario temporal para contar
		size_window=size_h*size_w*channels
		n_ceros=0
		for d in range(0, channels):
			for x_h in range(0, size_h):
                        	for x_w in range(0, size_w):
                                	activation=array[d][comienzo_h+x_h][comienzo_w+x_w]
                                	if(activation in diccionario_rep_per_window):
                                        	diccionario_rep_per_window[activation]=diccionario_rep_per_window[activation]+1 #Sumamos uno al contador
                                        else:
                                        	diccionario_rep_per_window[activation]=1 # Le decimos que hemos encontrado un valor de ese grupo 
					if(activation==0.0):
						n_ceros=n_ceros+1

		n_repeticiones=size_window/float(len(diccionario_rep_per_window))
		porcentaje_total=n_repeticiones*100
     		porcentaje_total=porcentaje_total/float(size_window)
		
		porcentaje_ceros=n_ceros*100
		porcentaje_ceros=porcentaje_ceros/float(size_window)
      		return porcentaje_total, porcentaje_ceros, diccionario_rep_per_window

	#Esta funcion compara las repeticiones que hay en una misma ventana y tambien entre esa ventana y la anterior, si esque existe anterior.
	#devuelve:
	# porcentaje_total: es el porcentaje de repeticiones que hay en la ventana
	# porcentaje_repeticiones_anterior: es el porcentaje de repeticiones que hay con respecto a la ventana anterior teniendo en cuenta la posicion y el valor. 
	def contar_repeticiones_and_comparar_anterior(self, array, comienzo_h, comienzo_w, size_h, size_w, first_channel, n_channels,  stride):
		diccionario_rep_per_window={} #diccionario temporal para contar
		
		size_window=size_h*size_w*n_channels
		n_repeticiones_anterior=0
		for d in range(first_channel, first_channel+n_channels):
			for x_h in range(0, size_h):
                        	for x_w in range(0, size_w):
                                	activation=array[d][comienzo_h+x_h][comienzo_w+x_w]
                                	if(activation in diccionario_rep_per_window):
                                        	diccionario_rep_per_window[activation]=diccionario_rep_per_window[activation]+1 #Sumamos uno al contador
                                        else:
                                        	diccionario_rep_per_window[activation]=1 # Le decimos que hemos encontrado un valor de ese grupo 
					#comparamos con la ventana anterior si no es la primera ventana
					if((comienzo_w-stride)>=0):
						activation_anterior=array[d][comienzo_h+x_h][comienzo_w-stride+x_w]
						if(activation==activation_anterior):
							n_repeticiones_anterior=n_repeticiones_anterior+1
							

		n_repeticiones=size_window/float(len(diccionario_rep_per_window))
		porcentaje_total=n_repeticiones*100
     		porcentaje_total=porcentaje_total/float(size_window)
		if((comienzo_w-stride)<0): #si se ha comparado con el anterior porque es de la segunda ventana en adelante entonces devolvemos valor valido
			return porcentaje_total, -1
		#si el valor es valido...
		porcentaje_repeticiones_anterior=n_repeticiones_anterior*100
		porcentaje_repeticiones_anterior=porcentaje_repeticiones_anterior/float(size_window)
      		return porcentaje_total, porcentaje_repeticiones_anterior
	
	#esta funcion sirve para contar la repeticiones de un array de 4 dimensiones como todos los filtros de pesos
	def contar_repeticiones_filtros(self, array, comienzo_h, comienzo_w, size_h, size_w, channels, ofmaps):
		diccionario_rep_per_window={} #diccionario temporal para contar
		size_window=size_h*size_w*channels*ofmaps
		for o in range(0, ofmaps):
			for d in range(0, channels):
				for x_h in range(0, size_h):
                        		for x_w in range(0, size_w):
                                	 	activation=array[o][d][comienzo_h+x_h][comienzo_w+x_w]
                                		if(activation in diccionario_rep_per_window):
                                        		diccionario_rep_per_window[activation]=diccionario_rep_per_window[activation]+1 #Sumamos uno al contador
                                        	else:
                                        		diccionario_rep_per_window[activation]=1 # Le decimos que hemos encontrado un valor de ese grupo 

		n_repeticiones=size_window/float(len(diccionario_rep_per_window))
		porcentaje_total=n_repeticiones*100
      		porcentaje_total=porcentaje_total/float(size_window)
      		return porcentaje_total


        def contar_multiplicaciones_and_comparar_anterior_and_contar_ceros(self, fmap, filters):
		n_ofmaps=filters.shape[0]
		n_channel_fmaps=fmap.shape[0]
                n_channel_filters=filters.shape[1] #igual a fmap.shape[0]
                h_filter=filters.shape[2]
                w_filter=filters.shape[3]
                h_fmap=fmap.shape[1]
                w_fmap=fmap.shape[2]
                size_fmap=n_channel_fmaps*h_fmap*w_fmap
                size_window=h_filter*w_filter*n_channel_filters
		stride=1
                diccionario_rep_per_window={} #diccionario temporal para contar
                n_repeticiones_anterior=0
		diccionario_rep_per_ofmap={}
		diccionario_rep_total={}
		n_repeticiones_window=0
		n_repeticiones_ofmap=0
		repeticiones_multiplicaciones_por_ventana=[] #lleva el porcentaje de multiplicaciones por ventana
		repeticiones_multiplicaciones_entre_ventanas=[] # lleva el porcentaje de repeticiones de multiplicaciones entre una ventana y otra teniendo en cuenta la posicion de los elementos
		repeticiones_multiplicaciones_por_ofmap=[] # lleva el porcentaje de repeticiones de multiplicaciones por ofmap
		repeticiones_multiplicaciones_total=0 #lleva el porcentaje de repeticiones de multiplicaciones total. Es decir, entre todos los ofmaps
		n_multiplicaciones_por_ofmap=0 #lleva el numero de multiplicaciones por ofmap totales para luego calcular el porcentaje de similitud
		n_multiplicaciones_totales=0 #lleva el numero de multiplicaciones TOTALES en el calculo de todos los ofmap spara luego calcular el porcentaje de similitud
		n_multiplicaciones_ventana=0
		porcentaje_ceros_multiplicacion_por_ofmap=[]
		n_ceros_multiplicacion_actual=0
		for o in range(0, n_ofmaps):
			j=0
			diccionario_rep_per_ofmap={} #reseteamos el diccionario por ofmap
			n_multiplicaciones_por_ofmap=0 #reseteamos el numero de multiplicaciones por ofmap
			n_ceros_multiplicacion_actual=0
                	while((j+h_filter-1) < h_fmap):
                        	z=0
                        	while((z+w_filter-1) < w_fmap):
					diccionario_rep_per_window={}
					n_repeticiones_anterior=0
					n_multiplicaciones_ventana=0
					#MobileNets
					if((n_channel_filters < n_channel_fmaps) and (n_ofmaps == n_channel_fmaps) and (n_channel_filters==1) ):
						#reseteamos diccionario temporal y parametros
		                     		for x_h in range(0, h_filter):
		                             		for x_w in range(0, w_filter):
								n_multiplicaciones_por_ofmap=n_multiplicaciones_por_ofmap+1
								n_multiplicaciones_totales=n_multiplicaciones_totales+1
								n_multiplicaciones_ventana=n_multiplicaciones_ventana+1
								#Accedemos al ifmap con el mismo indice del ofmap
								activation = fmap[o][j+x_h][z+x_w] #
								#para que sea mas general puede ser o+d, asi vale para grupos >1. VER
								d=0 #Solo hay un filtro ya que hay tantos ofmaps como channels fmaps
								peso=filters[o][d][x_h][x_w] #El peso es correcto tanto con group como no
								#contamos 0 si alguno de los operandos lleva un 0
								if((activation==0.0) or (peso==0.0)):
									n_ceros_multiplicacion_actual=n_ceros_multiplicacion_actual+1
								#repeticiones de las multiplicaciones. 
								#la idea es colocar siempre el menor valor en la tupla al principio. Asi lo guardamos en el diccionario de la misma forma 
								#haciendolo independiente del orden de los operandos
								multiplicacion=(activation, peso) #Accederemos con la tupla peso, activacion, siendo el primer valor el menor
								if(peso<activation): #Siempre guardamos el menor antes. Es la forma de asegurarnos de que la tupla es siempre igual sin importar orden
									multiplicacion=(peso, activation)
		                                     		if(multiplicacion in diccionario_rep_per_window):
		                                             		diccionario_rep_per_window[multiplicacion]=diccionario_rep_per_window[multiplicacion]+1 #Sumamos uno al contador
		                                     		else:
		                                             		diccionario_rep_per_window[multiplicacion]=1 # Le decimos que hemos encontrado un valor de ese grupo 
		                                     		#comparamos con la ventana anterior si no es la primera ventana
		                                     		if((z-stride)>=0):
									#Acceso al fmap correpondiente al indice del ofmap
									activation_anterior=fmap[o][j+x_h][z-stride+x_w]
		                                             		if(activation==activation_anterior): #el peso es siempre el mismo, ya que ventana se desplaza, pero se multiplica por el mismo
		                                                   		n_repeticiones_anterior=n_repeticiones_anterior+1
								if(multiplicacion in diccionario_rep_per_ofmap): #diccionario por ofmap
									diccionario_rep_per_ofmap[multiplicacion]=diccionario_rep_per_ofmap[multiplicacion]+1
								else:
									diccionario_rep_per_ofmap[multiplicacion]=1
					
								if(multiplicacion in diccionario_rep_total):
									diccionario_rep_total[multiplicacion]=diccionario_rep_total[multiplicacion]+1
								else:
									diccionario_rep_total[multiplicacion]=1
					else:
		             			for d in range(0, n_channel_filters):
							#reseteamos diccionario temporal y parametros
		                     			for x_h in range(0, h_filter):
		                             			for x_w in range(0, w_filter):
									n_multiplicaciones_por_ofmap=n_multiplicaciones_por_ofmap+1
									n_multiplicaciones_totales=n_multiplicaciones_totales+1
									n_multiplicaciones_ventana=n_multiplicaciones_ventana+1
		                                     			activation=fmap[d][j+x_h][z+x_w]
									peso=filters[o][d][x_h][x_w] #El peso es correcto tanto con group como no
									#contamos 0 si alguno de los operandos lleva un 0
									if((activation==0.0) or (peso==0.0)):
										n_ceros_multiplicacion_actual=n_ceros_multiplicacion_actual+1
									#repeticiones de las multiplicaciones. 
									#la idea es colocar siempre el menor valor en la tupla al principio. Asi lo guardamos en el diccionario de la misma forma 
									#haciendolo independiente del orden de los operandos
									multiplicacion=(activation, peso) #Accederemos con la tupla peso, activacion, siendo el primer valor el menor
									if(peso<activation): #Siempre guardamos el menor antes. Es la forma de asegurarnos de que la tupla es siempre igual sin importar orden
										multiplicacion=(peso, activation)
		                                     			if(multiplicacion in diccionario_rep_per_window):
		                                             			diccionario_rep_per_window[multiplicacion]=diccionario_rep_per_window[multiplicacion]+1 #Sumamos uno al contador
		                                     			else:
		                                             			diccionario_rep_per_window[multiplicacion]=1 # Le decimos que hemos encontrado un valor de ese grupo 
		                                     			#comparamos con la ventana anterior si no es la primera ventana
		                                     			if((z-stride)>=0):
		                                             			activation_anterior=fmap[d][j+x_h][z-stride+x_w]
		                                             			if(activation==activation_anterior): #el peso es siempre el mismo, ya que ventana se desplaza, pero se multiplica por el mismo
		                                                    				n_repeticiones_anterior=n_repeticiones_anterior+1
									if(multiplicacion in diccionario_rep_per_ofmap): #diccionario por ofmap
										diccionario_rep_per_ofmap[multiplicacion]=diccionario_rep_per_ofmap[multiplicacion]+1
									else:
										diccionario_rep_per_ofmap[multiplicacion]=1
					
									if(multiplicacion in diccionario_rep_total):
										diccionario_rep_total[multiplicacion]=diccionario_rep_total[multiplicacion]+1
									else:
										diccionario_rep_total[multiplicacion]=1


					#Calculamos el porcentaje de repeticiones de la ventana
					n_repeticiones_window=size_window/float(len(diccionario_rep_per_window))
					porcentaje_repeticiones_window=n_repeticiones_window*100
					porcentaje_repeticiones_window=porcentaje_repeticiones_window/float(size_window)
					repeticiones_multiplicaciones_por_ventana.append(porcentaje_repeticiones_window)
					if((z-stride)>=0):
						porcentaje_repeticiones_anterior=n_repeticiones_anterior*100
                                		porcentaje_repeticiones_anterior=porcentaje_repeticiones_anterior/float(n_multiplicaciones_ventana)
						repeticiones_multiplicaciones_entre_ventanas.append(porcentaje_repeticiones_anterior)
					z=z+stride
				j=j+stride
			#esto ocurre por cada ofmap
                	n_repeticiones_ofmap=n_multiplicaciones_por_ofmap/float(len(diccionario_rep_per_ofmap))
                	porcentaje_ofmap=n_repeticiones_ofmap*100
                	porcentaje_ofmap=porcentaje_ofmap/float(n_multiplicaciones_por_ofmap)
			repeticiones_multiplicaciones_por_ofmap.append(porcentaje_ofmap)
			#ceros
			porcentaje_ceros_por_ofmap=n_ceros_multiplicacion_actual*100
			porcentaje_ceros_por_ofmap=porcentaje_ceros_por_ofmap/float(n_multiplicaciones_por_ofmap)
			porcentaje_ceros_multiplicacion_por_ofmap.append(porcentaje_ceros_por_ofmap)
		#esto se calcula una vez terminados todos los ofmaps
		n_repeticiones_totales=n_multiplicaciones_totales/float(len(diccionario_rep_total))
		porcentaje_total=n_repeticiones_totales*100
		porcentaje_total=porcentaje_total/float(n_multiplicaciones_totales)
		repeticiones_multiplicaciones_total=porcentaje_total
                return repeticiones_multiplicaciones_por_ventana, repeticiones_multiplicaciones_entre_ventanas, repeticiones_multiplicaciones_por_ofmap, repeticiones_multiplicaciones_total, porcentaje_ceros_multiplicacion_por_ofmap
	def get_descriptive_statistics(self, array):
		mean=np.mean(array)	
		std=np.std(array)
		max_value=np.max(array)
		min_value=np.min(array)
		return mean, std, max_value, min_value
	
	def get_comprehensive_static_statistics(self, filters):
#		filters=np.array([[[[1.0, 0.0], [0.0,0.0]], [[2.0, 2.0], [2.0,2.0]]], [[[2.0, 2.0], [2.0,2.0]], [[2.0, 2.0], [2.0,2.0]]]])
		n_ofmaps=filters.shape[0]
		n_channels=filters.shape[1]
		h_filter=filters.shape[2]
                w_filter=filters.shape[3]
		porcentaje_repeticiones_por_filtro=[] #lista por filtro del porcentaje de repeticion de pesos
                porcentaje_repeticiones_filtros=0 #porcentaje de repeticion medio de pesos entre todos los filtros
		porcentaje_ceros_por_filtro=[]
		porcentaje_repeticiones_consecutivas_por_filtro_por_channel=[] #lleva un valor con el porcentaje de pesos consecutivos y repetidos en el eje w por cada channel de cada ofmap
		mean_value_por_filtro=[]
		std_value_por_filtro=[]
		max_value_por_filtro=[]
		min_value_por_filtro=[]
		ic_por_channel_filtro=[]
		diccionarios_repeticiones_por_ofmap=[] #Lleva una lista de histogramas por cada filtro de pesos.
		#medimos el porcentaje de repeticiones por cada uno de los filtros
                for i in range(0, n_ofmaps):
                        porcentaje_total, porcentaje_ceros, diccionario_ofmap=self.contar_repeticiones_y_ceros(filters[i], 0, 0, h_filter, w_filter, n_channels)
			diccionarios_repeticiones_por_ofmap.append(diccionario_ofmap)
                        porcentaje_repeticiones_por_filtro.append(porcentaje_total)
                        porcentaje_ceros_por_filtro.append(porcentaje_ceros) #el total entre todos los ofmaps al final es un valor medio de cada ofmap
			porcentaje_repeticiones_consecutivas_por_channel=self.contar_repeticiones_consecutivas(filters[i], h_filter, w_filter, n_channels)
			for x in porcentaje_repeticiones_consecutivas_por_channel:
				porcentaje_repeticiones_consecutivas_por_filtro_por_channel.append(x) #Anadimos el valor de cada channel
			#valores de estadistica descriptiva
			mean_value, std_value, max_value, min_value=self.get_descriptive_statistics(filters[i])
			mean_value_por_filtro.append(mean_value)
			std_value_por_filtro.append(std_value)
			max_value_por_filtro.append(max_value)
			min_value_por_filtro.append(min_value)
			#Calculo de IC por cada channel
			for j in range(0, n_channels):
				precision=0.0 #Calculamos los clusters con valores identicos
                        	img_custom, library=generate_segments(filters[i][j], precision)
                        	n_clases=len(library)
                        	size_array=h_filter*w_filter
                        	ic_actual=size_array / float(n_clases)
                        	ic_actual=ic_actual*100
                        	ic_actual=ic_actual / float(size_array)
                        	ic_por_channel_filtro.append(ic_actual)

				
			
                #medimos el porcentaje de repeticiones entre todos los filtros  
                porcentaje_repeticiones_filtros=self.contar_repeticiones_filtros(filters, 0, 0, h_filter, w_filter, n_channels, n_ofmaps)
		
		return porcentaje_repeticiones_por_filtro, porcentaje_repeticiones_filtros, porcentaje_ceros_por_filtro, porcentaje_repeticiones_consecutivas_por_filtro_por_channel, mean_value_por_filtro, std_value_por_filtro, max_value_por_filtro, min_value_por_filtro, ic_por_channel_filtro, diccionarios_repeticiones_por_ofmap

		


		
	def get_comprehensive_dynamic_statistics(self, fmap, filters, long_execution): #long execution calculates multiplications
#		fmap=np.array([[[1.0,1.0,1.0], [2.0, 2.0, 2.0], [2.0, 2.0, 2.0]], [[2.0,2.0,2.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]])
#		filters=np.array([[[[0.0, 0.0], [0.0,0.0]], [[2.0, 2.0], [2.0,2.0]]], [[[2.0, 2.0], [2.0,2.0]], [[2.0, 2.0], [2.0,2.0]]]])
		n_ofmaps=filters.shape[0]
		#n_channels=filters.shape[1] #igual a fmap.shape[0]
		n_channels_fmaps=fmap.shape[0]
		n_channels_filters=filters.shape[1] #Can be different if mobilenets.
		h_filter=filters.shape[2]
		w_filter=filters.shape[3]
		h_fmap=fmap.shape[1]
		w_fmap=fmap.shape[2]
		size_fmap=n_channels_fmaps*h_fmap*w_fmap
		size_window=h_filter*w_filter*n_channels_filters
		porcentaje_repeticiones_por_ventana=[] #lista por ventana del porcentaje de repeticion de las activaciones
		porcentaje_repeticiones_por_fmap=0 #porcentaje de repeticion de las activaciones en el FMAP
		porcentaje_repeticiones_entre_ventanas=[] #porcentaje de repeticion de activacio una ventana con la anterior. Esto es que los valores de una misma posicion i es el mismo en ambas ventanas.
		porcentaje_repeticiones_multiplicaciones_por_ventana=[] #porcentaje de repeticion de las multiplicaciones dentro de una ventana
		porcentaje_repeticiones_multiplicaciones_entre_ventanas=[] #porcentaje de repeticiones de las multiplicaciones entre 2 ventanas consecutivas teniendo en cuenta posicion
		porcentaje_repeticiones_multiplicaciones_por_ofmap=[] #porcentaje de repeticiones de las multiplicaciones de cada ofmap
		porcentaje_repeticiones_multiplicaciones_total=0  #porcentaje de repeticiones de las multiplicaciones totales. 
		porcentaje_ceros_por_fmap=0
		porcentaje_multiplicaciones_con_cero_por_ofmap=[]
		porcentaje_activaciones_repetidas_consecutivas_por_channel=[] # Porcetaje de repeticiones consecutivas en el eje w por cada canal del fmap
		ic_por_channel=[] #lleva el valor de IC de cada canal de ese fmap
		mean_value_por_fmap=0 # lleva el valor medio del fmap
		std_value_por_fmap=0 # lleva el valor de la desviacion tipica del fmap
		max_value_por_fmap=0 # lleva el valor maximo del fmap
		min_value_por_fmap=0 # lleva el valor minimo del fmap
		stride=1 
		
		#for i in range(0, n_ofmaps):  #Para cada ofmap
		j=0
		while((j+h_filter-1) < h_fmap):
			z=0
			while((z+w_filter-1) < w_fmap): #por cada ventana
				if(n_channels_filters < n_channels_fmaps): #Estamos en MobileNets porque un filtro solo recorre un canal
					for o_fmap in range(0, n_channels_fmaps):
						porcentaje_total, porcentaje_total_entre_ventana=self.contar_repeticiones_and_comparar_anterior(fmap, j, z, h_filter, w_filter, o_fmap, 1, stride) #Vamos contando ventana a ventana. Notese que j y z van sumando
						if(porcentaje_total_entre_ventana>=0): #Si es un valor distinto de nulo, es decir que la ventana comparada tiene un anterior, entonces
							porcentaje_repeticiones_entre_ventanas.append(porcentaje_total_entre_ventana)
						porcentaje_repeticiones_por_ventana.append(porcentaje_total)			 
				else: #Es una capa normal
					porcentaje_total, porcentaje_total_entre_ventana=self.contar_repeticiones_and_comparar_anterior(fmap, j, z, h_filter, w_filter, 0, n_channels_fmaps, stride) #Le decimos que el numero de canales de la ventana va de 0 a n_channel_fmaps que ahora 
						   #coincide con n_channels_filters
					if(porcentaje_total_entre_ventana>=0): #Si es un valor distinto de nulo
                                        	porcentaje_repeticiones_entre_ventanas.append(porcentaje_total_entre_ventana)
					porcentaje_repeticiones_por_ventana.append(porcentaje_total)
				z=z+stride #stride
			j=j+stride #stride
		
		#Contamos el fmap
		porcentaje_repeticiones_por_fmap, porcentaje_ceros_por_fmap, diccionario_repeticiones_fmap=self.contar_repeticiones_y_ceros(fmap, 0, 0, h_fmap, w_fmap, n_channels_fmaps)
		#Calculamos el porcentaje de repeticiones de las multiplicaciones de cada ventana, entre ventanas consecutivas, de cada ofmap, y el total
		if(long_execution):
			porcentaje_repeticiones_multiplicaciones_por_ventana, porcentaje_repeticiones_multiplicaciones_entre_ventanas, porcentaje_repeticiones_multiplicaciones_por_ofmap, porcentaje_repeticiones_multiplicaciones_total, porcentaje_multiplicaciones_con_cero_por_ofmap =  self.contar_multiplicaciones_and_comparar_anterior_and_contar_ceros(fmap, filters) #Funcion adaptada a MobileNets. Diferentes groups

		porcentaje_activaciones_repetidas_consecutivas_por_channel=self.contar_repeticiones_consecutivas(fmap, h_fmap, w_fmap, n_channels_fmaps)

		#Valores de estadistica descriptiva del fmap
		mean_value_por_fmap, std_value_por_fmap, max_value_por_fmap, min_value_por_fmap=self.get_descriptive_statistics(fmap)

		#Calculamos el valor de IC para cada channel
		for i in range(0, n_channels_fmaps):
			precision=0.0 #Calculamos los clusters con valores identicos
			img_custom, library=generate_segments(fmap[i], precision)
			n_clases=len(library)
			size_array=h_fmap*w_fmap
			ic_actual=size_array / float(n_clases)
                        ic_actual=ic_actual*100
                        ic_actual=ic_actual / float(size_array)
			ic_por_channel.append(ic_actual)
			

		
		
		return porcentaje_repeticiones_por_ventana, porcentaje_repeticiones_entre_ventanas, porcentaje_repeticiones_por_fmap, porcentaje_repeticiones_multiplicaciones_por_ventana, porcentaje_repeticiones_multiplicaciones_entre_ventanas, porcentaje_repeticiones_multiplicaciones_por_ofmap, porcentaje_repeticiones_multiplicaciones_total, porcentaje_ceros_por_fmap, porcentaje_multiplicaciones_con_cero_por_ofmap, porcentaje_activaciones_repetidas_consecutivas_por_channel, mean_value_por_fmap, std_value_por_fmap, max_value_por_fmap, min_value_por_fmap,ic_por_channel, diccionario_repeticiones_fmap

		
	def generate_images(self, max_images, accuracy, max_layers, max_fmaps_allowed, max_range_value):
		#Check default values
		if(max_images==0):
			max_images=10
		if(accuracy==0):
			accuracy=0
		point_size=3
		list_names=[]
		self.controlador.start_getting_general_statistics()
		ok, self.first_blob, imname, self.first_params, layers, layer_names=self.controlador.get_next_image_online() #Guardamos el primer blob para luego sacar tamanos de el 
		list_names.append(imname)
		blobs=self.first_blob #Despues se recalcula, pero first_blob no cambia
		params=self.first_params
		raw_data=collections.OrderedDict({}) #Para no perder el orden de las claves que indica las capas de la red
		#creamos la estructura de datos
		if(max_layers==0 or max_layers>len(blobs)):
                	max_layers=len(blobs)

		n_layers=0
		for key in blobs: #Creamos espacio para cada layer. Y para cada fmap dentro de cada layer.
			max_fmaps=max_fmaps_allowed
			raw_data[key]=[]
			n_fmaps=blobs[key].data.shape[1]
			if(max_fmaps==0 or max_fmaps>n_fmaps):
                        	max_fmaps=n_fmaps

			for i in range(0, max_fmaps): #la primera capa
				raw_data[key].append([])
			n_layers+=1
			if(n_layers>=max_layers):
				break
		
		#Computacion
		num_images=0
		
		n_layers=0
		print('Calculating number of repeated pixels for each image...')
		print('-----------------------------------------')
		print('Max images')
		print(max_images)
		f=1
		files_fmaps=[]	
		if(self.statisticValue==7): #Recopilamos la informacion estatica de la red. Esto  solo hace falta hacerlo una vez 
			comprehensive_static_data=collections.OrderedDict({}) #para no perder el orden
			histogram_static_data=collections.OrderedDict({})
			n_layers=0
			key_anterior='data'
			for key in blobs: #para cada capa
				n_fmaps=blobs[key_anterior].data.shape[1]
				max_fmaps=max_fmaps_allowed
                                if(max_fmaps==0 or max_fmaps>n_fmaps):
                                        max_fmaps=n_fmaps
                              #	if((len(blobs[key_anterior].data[0][0].shape)!=2) or (key not in params) or (len(params[key][0].data.shape) != 4)): #comprobamos que la capa no es fc cogiendo un fmap aleatorio y comprobando su dimension
				if((key_anterior in list(layer_names)) and (layers[list(layer_names).index(key_anterior)].type != 'InnerProduct') and (key in params)):
					comprehensive_static_data[key]=collections.OrderedDict({})
					print('Layer filtro: '+key)
					print('Shape filtro:')
					print(params[key][0].data.shape)
					porcentaje_repeticiones_por_filtro, porcentaje_repeticiones_filtros, porcentaje_ceros_por_filtro, porcentaje_repeticiones_consecutivas_por_filtro_por_channel, mean_value_por_filtro, std_value_por_filtro, max_value_por_filtro, min_value_por_filtro, ic_por_channel_filtro, diccionarios_repeticiones_por_ofmap=self.get_comprehensive_static_statistics(params[key][0].data)
					number_of_filters=params[key][0].data.shape[0]
					number_of_channels=params[key][0].data.shape[1]
					size_of_channel=params[key][0].data.shape[2]*params[key][0].data.shape[3]
					comprehensive_static_data[key]['Number_of_Filters']=number_of_filters
			
					comprehensive_static_data[key]['Number_Of_Channels_Per_Filter']=number_of_channels

					comprehensive_static_data[key]['Number_Of_Weights_Per_Channel']=size_of_channel
		
					comprehensive_static_data[key]['Number_Of_Weights_Per_Filter']=size_of_channel*number_of_channels
					
					comprehensive_static_data[key]['Number_Of_Weights_All_Filters']=size_of_channel*number_of_channels*number_of_filters
						
					comprehensive_static_data[key]['Repeated_Weights_Percentage_Inside_Filter']=porcentaje_repeticiones_por_filtro #lista del porcentaje de repeticiones de cada filtro
					comprehensive_static_data[key]['Repeated_Weights_Percentage_Between_Filters']=porcentaje_repeticiones_filtros #float 
					comprehensive_static_data[key]['Zeroes_Percentage_Per_Filter']=porcentaje_ceros_por_filtro #es una lista del porcentaje de ceros por cada filtro
					comprehensive_static_data[key]['Repeated_Consecutive_Weights_Percentage_Per_Filter_Per_Channel']=porcentaje_repeticiones_consecutivas_por_filtro_por_channel
					comprehensive_static_data[key]['Mean_Value_Per_Filter']=mean_value_por_filtro #lista que contiene la media de los valores de cada filtro
					comprehensive_static_data[key]['Std_Value_Per_Filter']=std_value_por_filtro # lista que contiene la desv tipica de los valores de cada filtro
					comprehensive_static_data[key]['Max_Value_Per_Filter']=max_value_por_filtro # lista que contiene el valor maximo de cada filtro
					comprehensive_static_data[key]['Min_Value_Per_Filter']=min_value_por_filtro # lista que contiene el valor minimo de cada filtro
					comprehensive_static_data[key]['CR_Per_Filter_Per_Channel']=ic_por_channel_filtro # lista que contiene el IC de cada canal de cada filtro
		
					histogram_static_data[key]=diccionarios_repeticiones_por_ofmap
				key_anterior=key		
				n_layers+=1
                                if(n_layers>=max_layers): #Cortamos el bucle 
                                        break

			#End bucle for

			#Agrupamos a 1 valor por capa los parametros estaticos (ya que algunos como los relacionados con los ofmaps tienen varios valores por capa. Sacamos la media)
			average_comprehensive_static_data=collections.OrderedDict({}) #para no perder el orden
			for key_layer in comprehensive_static_data:
				average_comprehensive_static_data[key_layer]=collections.OrderedDict({}) #para no perder el orden de las capas


				average_comprehensive_static_data[key_layer]['Number_of_Filters']=comprehensive_static_data[key_layer]['Number_of_Filters'] #es float luego no hay que hacer media

				average_comprehensive_static_data[key_layer]['Number_Of_Channels_Per_Filter']=comprehensive_static_data[key_layer]['Number_Of_Channels_Per_Filter'] #es float luego no hay que hacer media

				average_comprehensive_static_data[key_layer]['Number_Of_Weights_Per_Channel']=comprehensive_static_data[key_layer]['Number_Of_Weights_Per_Channel'] #es float luego no hay que hacer media

				average_comprehensive_static_data[key_layer]['Number_Of_Weights_Per_Filter']=comprehensive_static_data[key_layer]['Number_Of_Weights_Per_Filter'] #es float luego no hay que hacer media

				average_comprehensive_static_data[key_layer]['Number_Of_Weights_All_Filters']=comprehensive_static_data[key_layer]['Number_Of_Weights_All_Filters'] #es float luego no hay que hacer media


				average_comprehensive_static_data[key_layer]['Repeated_Weights_Percentage_Inside_Filter']=sum(comprehensive_static_data[key_layer]['Repeated_Weights_Percentage_Inside_Filter'])/float(len(comprehensive_static_data[key_layer]['Repeated_Weights_Percentage_Inside_Filter']))
                        	average_comprehensive_static_data[key_layer]['Repeated_Weights_Percentage_Between_Filters']=comprehensive_static_data[key_layer]['Repeated_Weights_Percentage_Between_Filters'] #es float luego no hay que hacer media
				average_comprehensive_static_data[key_layer]['Zeroes_Percentage_Per_Filter']=sum(comprehensive_static_data[key_layer]['Zeroes_Percentage_Per_Filter'])/float(len(comprehensive_static_data[key_layer]['Zeroes_Percentage_Per_Filter']))
			
			        average_comprehensive_static_data[key_layer]['Repeated_Consecutive_Weights_Percentage_Per_Filter_Per_Channel']=sum(comprehensive_static_data[key_layer]['Repeated_Consecutive_Weights_Percentage_Per_Filter_Per_Channel'])/float(len(comprehensive_static_data[key_layer]['Repeated_Consecutive_Weights_Percentage_Per_Filter_Per_Channel']))

				average_comprehensive_static_data[key_layer]['Mean_Value_Per_Filter']=sum(comprehensive_static_data[key_layer]['Mean_Value_Per_Filter'])/float(len(comprehensive_static_data[key_layer]['Mean_Value_Per_Filter']))

				average_comprehensive_static_data[key_layer]['Std_Value_Per_Filter']=sum(comprehensive_static_data[key_layer]['Std_Value_Per_Filter'])/float(len(comprehensive_static_data[key_layer]['Std_Value_Per_Filter']))

				average_comprehensive_static_data[key_layer]['Max_Value_Per_Filter']=sum(comprehensive_static_data[key_layer]['Max_Value_Per_Filter'])/float(len(comprehensive_static_data[key_layer]['Max_Value_Per_Filter']))

				average_comprehensive_static_data[key_layer]['Min_Value_Per_Filter']=sum(comprehensive_static_data[key_layer]['Min_Value_Per_Filter'])/float(len(comprehensive_static_data[key_layer]['Min_Value_Per_Filter']))

				average_comprehensive_static_data[key_layer]['CR_Per_Filter_Per_Channel']=sum(comprehensive_static_data[key_layer]['CR_Per_Filter_Per_Channel'])/float(len(comprehensive_static_data[key_layer]['CR_Per_Filter_Per_Channel']))

			#Ahora sacamos la media de todas las capas tanto los parametros estaticos (que ya estan agrupados por capas)

			per_total_comprehensive_static_data=collections.OrderedDict({}) #para no perder el orden
			keys_layer_static=average_comprehensive_static_data.keys()
			for key_param in average_comprehensive_static_data[keys_layer_static[0]]:
				per_total_comprehensive_static_data[key_param]=0.0

			for key_layer in average_comprehensive_static_data:
				for key_param in average_comprehensive_static_data[key_layer]:
					per_total_comprehensive_static_data[key_param]+=average_comprehensive_static_data[key_layer][key_param]

			#dividimos entre el numero de capas

			for key_param in per_total_comprehensive_static_data:
				per_total_comprehensive_static_data[key_param]=per_total_comprehensive_static_data[key_param]/float(len(average_comprehensive_static_data))

			#En este punto 
			# - average_comprehensive_static_data: tenemos los valores medios por cada capa, por cada parametro estatico
			# - per_total_comprehensive_static_data: tenemos los valores medios por cada parametro estatico

			print('Estadisticas estaticas generadas correctamente. Volcando en fichero...')

				
			print('Estadisticas generadas correctamente. Volcando en fichero...')
			now = datetime.datetime.now()
			dir_str='Comprehensive_Simulation_'+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)+'_'+str(now.second)
			os.mkdir(dir_str)
			file_name='Analysis.txt'
			file_histogram_weights_name='Histograms_weights.txt'
			file_histogram_fmaps_name='Histograms_fmaps.txt'
			file_analysis = open(file_name,"w")
			file_histogram_weights = open(file_histogram_weights_name, "w")
			file_histogram_fmaps = open(file_histogram_fmaps_name, "w")
			file_analysis.write("Este fichero contiene estadisticas exhaustivas sobre la red neuronal ejecutada. Especificamente, el fichero se divide en 2 partes, distinguiendo asi parametros estaticos y denamicos. Los parametros estaticos son aquellos que no varian con el proceso de inferencia de la red, como por ejemplo los pesos utilizados. Los parametros de dinamicos muestran valores relacionados con los calculos intermedios que se van realizando (fmaps, operaciones, etc). A continuacion se detallan los parametros dinamicos que se tienen en cuenta:\n -1. Repeated_Activations_Percentage_Inside_Window: representa el porcentaje de activaciones que son iguales en una misma ventana. No tienen porque ser consecutivos. Basicamente este valor representa el numero medio de activaciones que pueden ser reutilizados en una misma ventana por repeticion de las mismas\n\n -2. Repeated_Activations_Percentage_Between_Consecutive_Windows: representa el porcentaje de repeticiones que no varian de una ventana a la siguiente. En este caso, solo hay repeticion en el punto i de la ventana, si en ese mismo punto i de la siguiente, existe un valor identico. Este parametro es de utilidad para medir el porcentaje de reutilizacion de una ventana a la siguiente.\n\n -3. Porcentaje_Repeticiones_APFmap: Este valor representa el numero medio de repeticiones (no tienen porque ser consecutivas) que existen en las activaciones de un mismo fmap. Este parametro es de utilidad para medir elporcentaje de reutilizacion que puede ser aprovechado en las activaciones de un mismo fmap.\n\n -4. Repeated_Multiplications_Percentage_Inside_Window: este valor mide el porcentaje de multiplicaciones identicas (tienen el mismo peso y activacion o viceversa) que se llevan a cabo en una misma ventana. Basicamente el parametro es util para medir la cantidad de multiplicaciones que pueden reutilizarse en una misma ventana.\n\n -5. Repeated_Multiplications_Percentage_Between_Consecutive_Windows: Este parametro mide la cantidad de multiplicaciones identicas (peso*activacion o viceversa) que se llevan a cabo entre 2 ventanas, teniendo en cuenta su posicion. Es decir, mide el porcentaje de multiplicaciones que se repiten en posicion entre una ventana y la siguiente. Basicamente este parametro sirve para medir la cantidad de multiplicaciones que pueden ser reutilizados entre 2 ventanas consecutivas (teniendo en cuenta incluso su posicion).\n\n -6. Repeated_Multiplications_Percentage_Per_Ofmap: Este parametro mide la cantidad de multiplicaciones repetidas que se llevan a cabo para calcular un ofmap completo. Sirve para medir la cantidad de reutilizacion de multiplicaciones que puede aprovecharse en el calculo de un mismo ofmap.\n\n -7. Total_Repeated_Multiplications_Percentage: El parametro mide la cantidad de multiplicaciones que pueden reutilizarse en el calculo de todos los ofmaps de esa capa. Basicamente mide la cantidad de reutilizacion que puede aprovecharse en el calculo completo de una capa.\n\n -8. Zeroes_Percentage_Per_Fmap: Este parametro mide el porcentaje de ceros que existe en cada fmap. Sirve para ver la dispersion de los mismos y realizar comparaciones con las repeticiones.\n\n -9. Porcentaje_Multiplicaciones_Ceros_Por_Ofmap: Este parametro mide la cantidad de multiplicaciones por cada ofmap que contienen un cero en cualquiera de sus operandos (peso, activacion) dando como resultado una multiplicacion con resultado de cero. Sirve para ver la cantidad de calculos que se realizan que en realidad obtienen cero como resultado.\n\n -10. Repeated_Consecutive_Activations_Per_Channel: Este parametro mide el porcentaje de activaciones repetidas CONSECUTIVAS que existen en cada channel de cada fmap. Sirve para evaluar una posible optimizacion de prediccion y/o reutilizacion de activaciones consecutivas identicas.\n\n -11. Mean_Value_Por_Fmap: Mide el valor medio de cada fmap. Sirve para comparar los fmaps de las distintas capas y ver como son en general sus valores.\n\n -12. Std_Value_Por_Fmap: Mide la desviacion tipica de cada fmap. Sirve para comparar los fmaps de las distintas capas y ver como son en general sus valores.\n\n -13. Max_Value_Por_Fmap: Mide el valor maximo de los fmaps. Sirve para comparar las distintas capas y saber cual es el numero de bits minimo que necesitamos para su representacion.\n\n -14. Min_Value_Por_Fmap: Mide el valor minimo de los fmaps. Sirve para comparar las distintas capas y saber cual es el numero de bits minimo que necesitamos para su representacion.\n\n -15. IC_Por_Channel: Es el indice de compresion por cada canal. Se calcula midiendo el numero de clusters con valores identicos y luego dividiendo el tamano del fmap entre el numero de clusters. Basicamente el parametro mide la repeticion en el eje x e y del fmap. \n--------------------------------------------------------------\n Parametros estaticos:\n -1. Repeated_Weights_Percentage_Inside_Filter: este valor mide el porcentaje medio de repeticiones en cada uno de los filtros. Este parametro expresa la cantidad de pesos que pueden ser reutilizados por ser identicos en un mismo filtro (con filtro teniendose en cuenta todas las dimensiones del mismo).\n\n -2. Repeated_Weights_Percentage_Between_Filters: Este valor mide el porcentaje de repeticiones de pesos entre todos los filtros usados para calcular los diferentes ofmaps. Este parametro sirve para identificar la cantidad de repeticiones que existen entre los distintos filtros (y no en el mismo filtro como el anterior parametro).\n\n -3. Zeroes_Percentage_Per_Filter: Este parametro mide el porcentaje de ceros existente en cada filtro. Sirve para ver la dispersion de los mismos.\n\n -4. porcentaje_repeticiones_consecutivas_por_filtro_por_channel: Este parametro contiene el porcentaje de pesos consecutivos repetidos en el eje w por cada canal de cada filtro de la capa. Es una medida que sirve para evaluar una posible optimizacion de compresion y/o prediccion de pesos dentro de los filtros.\n\n -5. Mean_Value_Per_Filter: Este parametro mide el valor medio por cada filtro. Sirve para comparar los valores generales de los filtros.\n\n -6. Std_Value_Per_Filter: Este parametro mide la desviacion tipica por filtro. Sirve para comparar los valores generales de los filtros.\n\n -7. Max_Value_Per_Filter: Este parametro mide el valor maximo de cada filtro. Sirve para comparar los valores generales de cada filtro y saber cuantos bits se necesitan para representarlos.\n\n -8. Min_Value_Per_Filter: Este parametro mide el valor minimo de cada filtro. Sirve para comparar los valores generales de cada filtro y para saber cuantos bits se necesitan para representarlos.\n\n -9. CR_Per_Filter_Per_Channel: Es el indice de compresion medio de cada canal de cada filtro de cada ofmap. Para calcular este valor un algoritmo segmenta el canal en clusters de modo que cada cluster contiene todos los valores identicos consecutivos. Para calcular el IC final se divide el numero de pesos de cada cluster y se divide entre el tamano del canal. Basicamente este parametro mide el porcentaje de valores repetidos y CONSECUTIVOS del filtro, tanto en el eje X como en el Y. \n--------------------------------------------------------\n\n\n ")

			file_analysis.write("******************************PARAMETROS ESTATICOS DE LA RED******************************\n\n")
			file_histogram_weights.write("******************************PARAMETROS ESTATICOS DE LA RED******************************\n\n")

			file_analysis.write("Estadisticas medias estaticas por cada capa\n---------------------------------------------------------\n")
         		contador_capa=0 # lleva el numero de capa para mostrarlo en el fichero
         		for key_layer in average_comprehensive_static_data:
         			file_analysis.write("\tCapa "+str(contador_capa)+": "+key_layer+"\n")
				file_analysis.write("\t----------------------------------------------------------------\n")
			   	file_histogram_weights.write("\tCapa "+str(contador_capa)+": "+key_layer+"\n")
				file_histogram_weights.write("\t----------------------------------------------------------------\n")
               			contador_capa=contador_capa+1 #incrementamos el numero de capa para la siguiente vuelta
               			for key_param in average_comprehensive_static_data[key_layer]:
               				file_analysis.write("\t\t-"+str(key_param)+"="+str(average_comprehensive_static_data[key_layer][key_param])+"\n")
					#Volcamos histograma por ofmap
				contador_filtro=0
				for diccionario_filtro in histogram_static_data[key_layer]:
					file_histogram_weights.write("\t\tFilter "+str(contador_filtro)+"\n")
					file_histogram_weights.write("\t\t----------------------------------------------------------------\n")
					for key_value in diccionario_filtro:
						file_histogram_weights.write(str(key_value)+"="+str(diccionario_filtro[key_value])+"\n")
						contador_filtro+=1

				file_histogram_weights.write("-----------------------------------------------------------------------------------------\n")
         			file_histogram_weights.write("-----------------------------------------------------------------------------------------\n")
         			file_histogram_weights.write("-----------------------------------------------------------------------------------------\n\n\n")

					

			file_analysis.write("-----------------------------------------------------------------------------------------\n")
         		file_analysis.write("-----------------------------------------------------------------------------------------\n")
         		file_analysis.write("-----------------------------------------------------------------------------------------\n")
         		file_analysis.write("Estadisticas medias por cada parametro (haciendo la media de todas las capas)\n---------------------------------------------------------\n")
         		for key_param in per_total_comprehensive_static_data:
         			file_analysis.write("-"+str(key_param)+"="+str(per_total_comprehensive_static_data[key_param])+"\n")
               		file_analysis.write("-----------------------------------------------------------------------------------------\n")
               		file_analysis.write("-----------------------------------------------------------------------------------------\n")
               		file_analysis.write("-----------------------------------------------------------------------------------------\n\n\n")


			file_analysis.write("******************************PARAMETROS DINAMICOS DE LA RED******************************\n\n")
			file_analysis.write("Estadisticas desglosadas por cada imagen y por cada capa en la inferencia de dicha imagen\n---------------------------------------------------------\n")
			file_histogram_fmaps.write("******************************PARAMETROS DINAMICOS DE LA RED******************************\n\n")
         		file_histogram_fmaps.write("Estadisticas desglosadas por cada imagen y por cada capa en la inferencia de dicha imagen\n---------------------------------------------------------\n")
			average_comprehensive_static_data[key_layer]=0 #Cleaning weights statistics to free space
			histogram_static_data=0 #CLeaning weight histograms in order to free space

		#dynamic data	
		#Tabulado fuera del if, porque se hace siempre
		
		histogram_dynamic_data=collections.OrderedDict({})
		per_layer_comprehensive_dynamic_data=collections.OrderedDict({}) #para no perder el orden
		contador_imagen=0
		while((num_images < max_images) and ok==True): # Foreach Image
			average_comprehensive_dynamic_data=collections.OrderedDict({}) #creamos espacio para la informacion de esta imagen
			histogram_dynamic_data=collections.OrderedDict({})
			n_layers=0
			if(self.statisticValue==6):
				f = open(imname+".txt", "w")
				files_fmaps.append(imname+".txt") # Guardamos el nombre del fichero para cada capa
			key_anterior='data'
			for key in blobs: # Para cada capa
				n_fmaps=blobs[key_anterior].data.shape[1]
				max_fmaps=max_fmaps_allowed
				if(max_fmaps==0 or max_fmaps>n_fmaps):
					max_fmaps=n_fmaps
				if(self.statisticValue==7):
				#El problema para las estadisticas esque en la capa siguiente se guardan los filtros de pesos utilizados para computar la capa anterior. Por ello vamos 
				# utilizando los filtros de la capa siguiente y el fmap de la anterior.
				#	if((len(blobs[key_anterior].data[0][0].shape)!=2) or (key not in params) or (len(params[key][0].data.shape) != 4)): #comprobamos que la capa no es fc cogiendo un fmap aleatorio y comprobando su dimension
					long_execution=self.GroupEverything.isChecked() #Ask if it has to execute multiplications

					if((key_anterior in list(layer_names)) and (layers[list(layer_names).index(key_anterior)].type != 'InnerProduct') and (key in params)):
						average_comprehensive_dynamic_data[key]=collections.OrderedDict({}) #para no perder el orden entre las capas

						porcentaje_repeticiones_por_ventana, porcentaje_repeticiones_entre_ventanas, porcentaje_repeticiones_por_fmap, porcentaje_repeticiones_multiplicaciones_por_ventana, porcentaje_repeticiones_multiplicaciones_entre_ventanas, porcentaje_repeticiones_multiplicaciones_ofmap, porcentaje_repeticiones_multiplicaciones_total,  porcentaje_ceros_por_fmap, porcentaje_multiplicaciones_con_cero_por_ofmap, porcentaje_activaciones_repetidas_consecutivas_por_channel, mean_value_por_fmap, std_value_por_fmap, max_value_por_fmap, min_value_por_fmap, ic_por_channel, diccionario_repeticiones_fmap = self.get_comprehensive_dynamic_statistics(blobs[key_anterior].data[0], params[key][0].data, long_execution)

						number_of_channels=blobs[key_anterior].data.shape[1]
						activations_per_channel=blobs[key_anterior].data.shape[2]*blobs[key_anterior].data.shape[3]
						activations_fmap=activations_per_channel*number_of_channels

						average_comprehensive_dynamic_data[key]['Number_Of_Channels']=number_of_channels
							
						average_comprehensive_dynamic_data[key]['Number_Of_Activations_Per_Channel']=activations_per_channel
						average_comprehensive_dynamic_data[key]['Number_Of_Activations_Fmap']=activations_fmap							

						average_comprehensive_dynamic_data[key]['Repeated_Activations_Percentage_Inside_Window']=sum(porcentaje_repeticiones_por_ventana)/float(len(porcentaje_repeticiones_por_ventana))
						if(len(porcentaje_repeticiones_entre_ventanas)==0):
							average_comprehensive_dynamic_data[key]['Repeated_Activations_Percentage_Between_Consecutive_Windows']=0.0
						else:
							average_comprehensive_dynamic_data[key]['Repeated_Activations_Percentage_Between_Consecutive_Windows']=sum(porcentaje_repeticiones_entre_ventanas)/float(len(porcentaje_repeticiones_entre_ventanas))
				
						average_comprehensive_dynamic_data[key]['Repeated_Activations_Percentage_Inside_Fmap']=porcentaje_repeticiones_por_fmap #esta variable es float
						if(long_execution):
							average_comprehensive_dynamic_data[key]['Repeated_Multiplications_Percentage_Inside_Window']=sum(porcentaje_repeticiones_multiplicaciones_por_ventana)/float(len(porcentaje_repeticiones_multiplicaciones_por_ventana))
						
							if(len(porcentaje_repeticiones_multiplicaciones_entre_ventanas) == 0):
								average_comprehensive_dynamic_data[key]['Repeated_Multiplications_Percentage_Between_Consecutive_Windows']=0.0
							else:
								average_comprehensive_dynamic_data[key]['Repeated_Multiplications_Percentage_Between_Consecutive_Windows']=sum(porcentaje_repeticiones_multiplicaciones_entre_ventanas)/float(len(porcentaje_repeticiones_multiplicaciones_entre_ventanas))

							average_comprehensive_dynamic_data[key]['Repeated_Multiplications_Percentage_Per_Ofmap']=sum(porcentaje_repeticiones_multiplicaciones_ofmap)/float(len(porcentaje_repeticiones_multiplicaciones_ofmap))

							average_comprehensive_dynamic_data[key]['Total_Repeated_Multiplications_Percentage']=porcentaje_repeticiones_multiplicaciones_total #esta variable es float

							average_comprehensive_dynamic_data[key]['Zero_Multiplications_Per_Ofmap']=sum(porcentaje_multiplicaciones_con_cero_por_ofmap)/float(len(porcentaje_repeticiones_multiplicaciones_ofmap))
						#End of long_execution

						average_comprehensive_dynamic_data[key]['Zeroes_Percentage_Per_Fmap']=porcentaje_ceros_por_fmap #esta variable es float
						average_comprehensive_dynamic_data[key]['Repeated_Consecutive_Activations_Per_Channel']=sum(porcentaje_activaciones_repetidas_consecutivas_por_channel)/float(len(porcentaje_activaciones_repetidas_consecutivas_por_channel))
						average_comprehensive_dynamic_data[key]['Mean_Value_Per_Fmap']=mean_value_por_fmap #esta variable es float
						average_comprehensive_dynamic_data[key]['Std_Value_Per_Fmap']=std_value_por_fmap #esta variable es float
						average_comprehensive_dynamic_data[key]['Max_Value_Per_Fmap']=max_value_por_fmap #esta variable es float
						average_comprehensive_dynamic_data[key]['Min_Value_Per_Fmap']=min_value_por_fmap #esta variable es float
						average_comprehensive_dynamic_data[key]['CR_Per_Channel']=sum(ic_por_channel)/float(len(ic_por_channel))
						histogram_dynamic_data[key]=diccionario_repeticiones_fmap

						#Average values per layer
						if(key not in per_layer_comprehensive_dynamic_data): #First iteration
							per_layer_comprehensive_dynamic_data[key]=collections.OrderedDict({}) #para no perder el orden
							for param_k in average_comprehensive_dynamic_data[key]:
								per_layer_comprehensive_dynamic_data[key][param_k]=0.0
						
						for param_k in average_comprehensive_dynamic_data[key]: #Over the previous variable
							per_layer_comprehensive_dynamic_data[key][param_k]+=average_comprehensive_dynamic_data[key][param_k] #Vamos sumando para luego dividir entre el numero total de imagenes
							
					key_anterior=key #Guardamos el actual para la siguiente vuelta
				if(self.statisticValue==6):
                                	f.write("Layer "+str(n_layers)+".\n-----------------\n")
					f.write("\t")
					for k in range(0, max_fmaps):
						f.write("fmap "+str(k)+"\t")
					f.write("\n")

				#for i in range(0, max_fmaps): # Para cada fmap
				#	#Computar algoritmo de segmentacion para obtener el numero de clases
				#	pixeles=blobs[key].data[0][i]
				#	if(len(pixeles.shape)!=2):
				#		pass #Capa inservible
				#	else:
				#		if(self.statisticValue<6): # Si es una estadistica que genere graficos...
				#			data_to_insert=self.calculate_current_value(pixeles, accuracy, self.statisticValue)
				#			if((max_range_value != 0) and (data_to_insert>max_range_value)): # Set a maximum limit
				#				data_to_insert=max_range_value
				#			raw_data[key][i].append(data_to_insert)
				#		elif(self.statisticValue==6): #Si es una estadistica que genera valores..
				#			f.write("fmap "+str(i)+":\t")
				#			for k in range(0, i+1):
				#				f.write("\t")
				#			for k in range(i+1, max_fmaps):
				#				data_to_insert=self.calculateSimilarity(blobs[key].data[0][i], blobs[key].data[0][k], accuracy)
				#				f.write(str(data_to_insert)+"\t")
				#			f.write("\n")
							
				n_layers+=1
				if(n_layers>=max_layers): #Cortamos el bucle 
					break
		#print(raw_data)			
			if(self.statisticValue==6):
				f.close()

			#Mostramos los datos de la imagen actual
			if(self.statisticValue==7):
				print('Dumping image statistics of image'+str(contador_imagen))
				file_analysis.write("Imagen "+str(contador_imagen)+": "+imname+"\n")
				file_analysis.write("-----------------------------------------------------------------------\n")
				file_histogram_fmaps.write("Imagen "+str(contador_imagen)+": "+imname+"\n")
            			file_histogram_fmaps.write("-----------------------------------------------------------------------\n")
				contador_capa=0 #sirve para llevar la cuenta del numero de capa y mostrarlo asi en el fichero
				for key_layer in average_comprehensive_dynamic_data:
					file_analysis.write("\tCAPA "+str(contador_capa)+": "+key_layer+"\n")
					file_analysis.write("\t----------------------------------------------------------------\n")
					file_histogram_fmaps.write("\tCAPA "+str(contador_capa)+": "+key_layer+"\n")
               				file_histogram_fmaps.write("\t----------------------------------------------------------------\n")
					contador_capa=contador_capa+1
					for key_param in average_comprehensive_dynamic_data[key_layer]:
						file_analysis.write("\t\t-"+str(key_param)+"="+str(average_comprehensive_dynamic_data[key_layer][key_param])+"\n")
					for key_value in histogram_dynamic_data[key_layer]:
						file_histogram_fmaps.write(str(key_value)+"="+str(histogram_dynamic_data[key_layer][key_value])+"\n")
					file_analysis.write("\t----------------------------------------------------------------\n") #fin de la capa
					file_histogram_fmaps.write("\t----------------------------------------------------------------\n") #fin de la capa
				file_analysis.write("-----------------------------------------------------------------------------------------\n") #Fin de la imagen
				file_analysis.write("-----------------------------------------------------------------------------------------\n") #Fin de la imagen
				file_analysis.write("-----------------------------------------------------------------------------------------\n") #Fin de la imagen
				
			contador_imagen+=1	
			print('Image '+str(num_images)+' Finished')
                        num_images+=1
                        ok, blobs, imname, params, layers, layer_names=self.controlador.get_next_image_online()
                        list_names.append(imname) #Para mostrar el nombre de la imagen

		#Una vez acabado ya podemos mostrar los datos medios
		if(self.statisticValue==7):
			#Reduccion a un valor por imagen y por capa de las variables de tipo lista. En realidad esto se podria haber hecho antes. Pero esto es solo un metodo de representacion	
			#dejamos a esta parte del codigo la capacidad de decidir como representa los datos. En este caso la representacion consiste en imprimir un valor medio de cada parametro
			#por imagen y luego un valor medio entre todas las imagenes. Esto dara una idea general de como funciona una DNN. 
			print('Dumping Average Values...')
			
			file_analysis.write("-----------------------------------------------------------------------------------------\n")
			file_analysis.write("-----------------------------------------------------------------------------------------\n")
			file_analysis.write("-----------------------------------------------------------------------------------------\n")
			file_analysis.write("Estadisticas medias dinamicas por cada capa (haciendo la media con todas las imagenes)\n---------------------------------------------------------\n")	
			contador_capa=0 # lleva el numero de capa para mostrarlo en el fichero
			for key_layer in per_layer_comprehensive_dynamic_data: 
				file_analysis.write("Capa "+str(contador_capa)+": "+key_layer+"\n")
				contador_capa=contador_capa+1 #incrementamos el numero de capa para la siguiente vuelta
				for key_param in per_layer_comprehensive_dynamic_data[key_layer]:
					per_layer_comprehensive_dynamic_data[key_layer][key_param]=per_layer_comprehensive_dynamic_data[key_layer][key_param]/float(contador_imagen) #Dividmos entre el numero de imagenes
					file_analysis.write("\t-"+str(key_param)+"="+str(per_layer_comprehensive_dynamic_data[key_layer][key_param])+"\n") #Ahora ya lo podemos mostrar por pantalla
				file_analysis.write("----------------------------------------------------------------\n") #Espacio por capa
	
	 		file_analysis.write("-----------------------------------------------------------------------------------------\n")
         		file_analysis.write("-----------------------------------------------------------------------------------------\n")
         		file_analysis.write("-----------------------------------------------------------------------------------------\n")
         		file_analysis.write("Estadisticas medias por cada parametro (haciendo la media de todas las imagenes y de todas las capas)\n---------------------------------------------------------\n")
			#Estadisticas medias por parametro, imagen, y capa
			per_total_comprehensive_dynamic_data=collections.OrderedDict({})
			keys_layer_dynamic=per_layer_comprehensive_dynamic_data.keys()
			for key_param in per_layer_comprehensive_dynamic_data[keys_layer_dynamic[0]]: #tomamos la primera capa como referencia
				per_total_comprehensive_dynamic_data[key_param]=0.0
			
			
			for key_layer in per_layer_comprehensive_dynamic_data:
				for key_param in per_layer_comprehensive_dynamic_data[key_layer]:
					per_total_comprehensive_dynamic_data[key_param]+=per_layer_comprehensive_dynamic_data[key_layer][key_param]


			#dividimos entre el numero de capas
			for key_param in per_total_comprehensive_dynamic_data:
				per_total_comprehensive_dynamic_data[key_param]=per_total_comprehensive_dynamic_data[key_param]/float(len(per_layer_comprehensive_dynamic_data))
			for key_param in per_total_comprehensive_dynamic_data: #En realidad se puede integrar en el otro bucle pero es rapido igualmente
				file_analysis.write("-"+str(key_param)+"="+str(per_total_comprehensive_dynamic_data[key_param])+"\n")

			file_analysis.write("-----------------------------------------------------------------------------------------\n")
         		file_analysis.write("-----------------------------------------------------------------------------------------\n")
         		file_analysis.write("--------------------------------FIN DEL FICHERO--------------------------------------------\n")
			file_histogram_weights.write("-----------------------------------------------------------------------------------------\n")
         		file_histogram_weights.write("-----------------------------------------------------------------------------------------\n")
         		file_histogram_weights.write("--------------------------------FIN DEL FICHERO--------------------------------------------\n")
			file_histogram_fmaps.write("-----------------------------------------------------------------------------------------\n")
         		file_histogram_fmaps.write("-----------------------------------------------------------------------------------------\n")
         		file_histogram_fmaps.write("--------------------------------FIN DEL FICHERO--------------------------------------------\n")
			file_analysis.close()
			file_histogram_weights.close()
			file_histogram_fmaps.close()
			#lo movemos a la carpeta
			shutil.move(file_name, dir_str)
			shutil.move(file_histogram_weights_name, dir_str)
			shutil.move(file_histogram_fmaps_name, dir_str)
	
			print('Fichero de estadisticas generado correctamente...')		
			print('Fichero de histogramas de pesos generado correctamente')
			print('Fichero de histogramas de fmaps generado correctamente')
			

						

			
					
		if(self.statisticValue==6):
			print('Creating files...')
			now = datetime.datetime.now()
                        dir_str='Scan_Fmaps_Simulation_'+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)+'_'+str(now.second)
			os.mkdir(dir_str)
			for i in files_fmaps:
				shutil.move(i, dir_str)
		if(self.statisticValue<6):
			print('Creating graphs...')
			print('-------------------------------')
			now = datetime.datetime.now()
			dir_str='Graphs_Simulation_'+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)+'_'+str(now.second)
			os.mkdir(dir_str)
			x=np.arange(0, num_images)
			#Mostramos las graficas. Segun las opciones se crearan de una forma u otra. 
			blobs=self.first_blob #Asignamos blobs al primer blob de manera que si se acaban las imagenes nos aseguramos de que tiene valor valido
			#Agrupamos por fmap
                	plt.clf()
                	valormin=100000
                	valormax=-100000
			sum_fmaps=0
			total_average=[]
			total_average_x=[]
			capas_actuales=0
                	for key in raw_data:
				total_average_x.append(capas_actuales)
				capas_actuales+=1
				sum_fmaps=0
				#fig = plt.figure()
				#ax = fig.add_subplot(111)
				#ax.set_ylim(0,10)
				h_p, w_p=blobs[key].data[0][0].shape #Cogemos el tamano del fmap 0
				valormin=100000
	        		valormax=-100000
				name_image='Statistic_'+'Acc_'+str(accuracy)+'_Layer_'+key.replace("/", "-")+'_fmap_all_size_'+str(h_p)+'x'+str(w_p)+'.png'
                		n_fmaps=len(raw_data[key])
				#Si hay fmaps con el mismo valor, queremos que nos muestre cuantos hay. Lo hacemos ahora
				#Creamos una lista de diccionarios. Un diccionario por imagen. 
				#Cada diccionario almacenara el numero de fmaps iguales. De modo que la clave del diccionario sera el valor
				#y el numero asociado a la clave el numero de elmentos que se repite dicho valor
				lista_de_diccionarios=[]
				diccionario_unit={}
				for i in x: #Creamos la lista de diccionarios. Elemento i corresponde al diccionario de la imagen i
					diccionario_unit={}
					lista_de_diccionarios.append(diccionario_unit) 
				#Recorremos por cada fmap y por cada valor de fmap
				average_value=[0 for q in range(0, max_images)]
				for i in range(0, n_fmaps):
					y=raw_data[key][i]
					for j in range(0, len(y)): #leny es numero de imagenes
						valor_actual=y[j]
						average_value[j]+=valor_actual
						if valor_actual in lista_de_diccionarios[j]:
							lista_de_diccionarios[j][valor_actual]+=1 #diccionario imagen j, clave valor_actual
						else:
							lista_de_diccionarios[j][valor_actual]=1 #creamos el valor de clave valor actual en dicc j.
				media_imagenes=0
				for q in range(0, max_images):
					average_value[q]=average_value[q]/n_fmaps
					media_imagenes+=average_value[q] #Para hacer la media entre todas las imagenes
				media_imagenes=media_imagenes/max_images
				print('Capa '+key+': '+str(media_imagenes))
				total_average.append(media_imagenes)
				#Ahora recorremos la lista de diccionarios. Por cada imagen (numero de diccionarios, eje x), y por cada clave del
				#diccionario (valor, eje y), vemos el numero de fmaps iguales, valor del diccionario para esa imagen.
				point_size=6
				c1='#000000'
				c2='#3D3838'
				c3='#5F5252'
				c4='#A79494'
				plt.xticks(x, list_names)			
				for i in range(0, len(lista_de_diccionarios)):
					for k in lista_de_diccionarios[i]: #Segun el rango pintamos una cosa u otra
						if(lista_de_diccionarios[i][k]==1):
							plt.plot(i, k, marker='.', markersize=point_size, markerfacecolor=c1, markeredgecolor=c1)
						elif(lista_de_diccionarios[i][k]>=2 and lista_de_diccionarios[i][k]<5):
							plt.plot(i, k, marker='x', markersize=point_size, markerfacecolor=c2, markeredgecolor=c2)
						elif(lista_de_diccionarios[i][k]>=5 and lista_de_diccionarios[i][k]<10):
							plt.plot(i, k, marker='_', markersize=point_size, markerfacecolor=c3, markeredgecolor=c3)
						elif(lista_de_diccionarios[i][k]>=10):
							plt.plot(i, k, marker='|', markersize=point_size, markerfacecolor=c4, markeredgecolor=c4)
						#if(lista_de_diccionarios[i][k] > 1):
				#			ax.annotate(str(lista_de_diccionarios[i][k]),xy=(i,k))
							#	plt.text(i, k, str(lista_de_diccionarios[i][k]), fontsize=4) #entre 5 o 6 puede ser adecuado
					#fin del algoritmo para mostrar el numero de fmaps al lado del punto

				#Mostramos valor medio
				for i in range(0, max_images):
					plt.plot(i, average_value[i], marker='*', markersize=point_size+2, markerfacecolor='#FF0000', markeredgecolor='#FF0000') #Color rojo
					plt.text(i, average_value[i], 'm', fontsize=point_size+2) #Colocamos una m al lado del valor medio
				#Mostramos leyenda
				#plt.plot([],[], marker='.',linestyle = 'None', markerfacecolor=c1, markeredgecolor=c1, label='1 fmaps')
				#plt.plot([],[], marker='x',linestyle = 'None', markerfacecolor=c2, markeredgecolor=c2, label='2-4 fmaps')
				#plt.plot([],[], marker='_',linestyle = 'None', markerfacecolor=c3, markeredgecolor=c3, label='5-9 fmaps')
				#plt.plot([],[], marker='|',linestyle = 'None', markerfacecolor=c4, markeredgecolor=c4, label='10+ fmaps')
				#plt.plot([],[], marker='*',linestyle = 'None', markerfacecolor='#FF0000', markeredgecolor='#FF0000', label='Average')
				#plt.legend(loc="upper right") 
                       		x_axis, y_axis, title=self.get_axis_parameters(accuracy)
                       		plt.xlabel(x_axis)
                       		plt.ylabel(y_axis)
                       		plt.title(title+'. L='+key+';S='+str(h_p)+'x'+str(w_p)+';nf='+str(n_fmaps))
                       		plt.savefig(dir_str+'/'+name_image)
                       		plt.clf() #Clean the graph and axis
                       		print(dir_str+'/'+name_image+' Generated..')
				#Ahora mostramos el numero de imagenes que cumplen la estadistica para cada fmap
				for i in range(0, n_fmaps): #TODO este algoritmo es bastante ineficiente
					fmap_current=raw_data[key][i]
					fmap_set=set(fmap_current) #Para eliminar los elementos repetidos
					x2=sorted(list(fmap_set)) #Lista sin elementos repetidos
					y2=[]
					for j in x2:
						n_veces=self.contar_veces(j, fmap_current)
						y2.append(n_veces) #Por cada numero de pixeles te dice cuantas imagenes hay para ese fmap concreto
					
					plt.xlabel(y_axis)
					plt.ylabel(x_axis) #Ejes invertidos. 
					plt.title(title+'. L='+key+';S='+str(h_p)+'x'+str(w_p))
					name_image='Statistic_'+'Acc_'+str(accuracy)+'_Layer_'+key.replace("/", "-")+'_fmap_all_size_'+str(h_p)+'x'+str(w_p)+'_Inverted'+'.png'
					plt.plot(x2, y2, '.', markersize=point_size) #Vamos mostrando fmap a fmap
				plt.savefig(dir_str+'/'+name_image)
				print(dir_str+'/'+name_image+' Generated..')
				plt.clf()
			#Generamos la imagen de la media de toda slas imagenes y de todos los fmaps
			plt.plot(total_average_x, total_average, marker='o', linestyle='--', color='r') #Grafu
			print(total_average)
			plt.xlabel('N Layer')
			plt.ylabel(y_axis)
			plt.xlabel
			plt.xticks(rotation=90)
			plt.xticks(total_average_x)
                	plt.title(title+' . Average per Layer')
                	plt.savefig(dir_str+'/'+'Average_per_layer.png')
                	print((dir_str+'/'+'Average_per_layer.png Generated..'))
                	plt.clf()

			print('The process has finished')
	
	
	def generate_image_one_check(self, n_images, accuracy, layer, fmap, max_range_value):
		   #Check default values
                if(n_images==0):
                        n_images=10
                if(accuracy==0):
                        accuracy=5
                ok, blobs=self.initial_ok, self.initial_blob
		pixeles=blobs[layer].data[0][fmap]
		h_pixeles=pixeles.shape[0]
		w_pixeles=pixeles.shape[1]
		num_images=0
		y=[] #Lista vacia donde ir insertando los datos para cada imagen, de esa capa de ese fmap.
		while((num_images < n_images) and ok==True): # Foreach Image
			pixeles=blobs[layer].data[0][fmap]	
			img_custom, library=generate_segments(pixeles, accuracy)
                        data_to_insert=self.calculate_current_value(pixeles, library, self.statisticValue)
			if((max_range_value != 0) and (data_to_insert>max_range_value)): # Set a maximum limit
                        	data_to_insert=max_range_value

                        y.append(data_to_insert)
			num_images+=1
			ok, blobs, imname=self.controlador.get_next_image_online()
			self.initial_ok, self.initial_blob=ok, blobs #Podriamos hacerlo directamente pero asi queda mas claro en el resto del codigo
			
                        print('Image '+str(num_images)+' Finished')
		
		print('Creating graphs...')
                print('-------------------------------')
                now = datetime.datetime.now()
                dir_str='Graphs_Simulation_'+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)+'_'+str(now.second)
                os.mkdir(dir_str)
                x=np.arange(0, num_images)
		name_image='Statistic_'+'Acc_'+str(accuracy)+'_Layer_'+layer+'_fmap_'+str(fmap)+'_size_'+str(h_pixeles)+'x'+str(w_pixeles)+'.png'
		if(len(y)!=0):
			fig, ax = plt.subplots()
                        ax.xaxis.set_ticks(np.arange(0, len(x), 1))
                        ax.yaxis.set_ticks(np.arange(min(y)-1, max(y)+1, 1))
                        plt.plot(x, y, marker='o', linestyle='--', color='r')
                        x_axis, y_axis, title=self.get_axis_parameters(accuracy)
                        plt.xlabel(x_axis)
                        plt.ylabel(y_axis)
			plt.title(title+'. L='+layer+';S='+str(h_p)+'x'+str(w_p))
                        plt.savefig(dir_str+'/'+name_image)
                        plt.clf() #Clean the graph and axis
                        print(dir_str+'/'+name_image+' Generated..')
		print('The process has finished')
		self.controlador.restart_getting_data_online() #Colocamos el index a 0 por si queremos volver a ejecutar sobre otra layer o fmap.
							#De esta forma esos datos seran tambien sobre las mismas imagenes


	def execute(self):
		t1 = time.time()
		n_images = self.NumberOfImagesCB.value()
		accuracy = self.AccuracyCB.value()
		max_value= self.MaxValueRangeCB.value()
		if(self.OnlyOneCheck.isChecked()):
			layer=str(self.LayerCB.currentText())
			fmap=int(str(self.FmapCB.currentText()))
			if((layer != '') and (fmap!='')):
				print(layer)
				print(fmap)
				self.generate_image_one_check(n_images, accuracy, layer, fmap, max_value)
		else:
			n_layers = self.NumberOfLayersCB.value()
			fmaps_per_layer = self.FmapsPerLayerCB.value()
			self.generate_images(n_images, accuracy, n_layers, fmaps_per_layer, max_value)		
		
		t2=time.time()	
		tfinal=t2-t1
		print('Running Time: '+str(tfinal)+' seconds')
		
	#Con las siguientes 2 funciones vamos a hacer que solo sea posible tener activo uno de los dos checkbox
	def everythingCBchanged(self):
		if(self.GroupEverything.isChecked()): #Si se ha activado desactivamos el otro
			self.GroupByFmap.setChecked(False)  #Desactivamos el otro
	
	def fmapCBchanged(self):
		if(self.GroupByFmap.isChecked()):
			self.GroupEverything.setChecked(False) #Desactivamos el otro
	
		
	def onlyOneCheckChanged(self):
		if(self.OnlyOneCheck.isChecked()): #Ocultamos todo lo de la parte izquierda
			self.NumberOfLayersLabel.setVisible(False)
			self.FmapsPerLayerLabel.setVisible(False)
			self.NumberOfLayersCB.setVisible(False)
			self.FmapsPerLayerCB.setVisible(False)
			self.label_7.setVisible(False)
			self.label_8.setVisible(False)
			self.GroupEverything.setVisible(False)
			self.GroupByFmap.setVisible(False)
			#Inicializamos los ComboBox
			self.controlador.start_getting_general_statistics()
                	self.initial_ok, self.initial_blob, imname=self.controlador.get_next_image_online()
			layer_list=['']
			self.LayerCB.clear()
			if(self.initial_ok==True):
                		for key in self.initial_blob:
                        		layer_list.append(key)
			else:
				print('No hay imagenes en la ruta')

			self.LayerCB.addItems(layer_list)
			fmap_list=['']
			self.FmapCB.clear()
			self.FmapCB.addItems(fmap_list)
			

	
		else:
			self.NumberOfLayersLabel.setVisible(True)
                        self.FmapsPerLayerLabel.setVisible(True)
                        self.NumberOfLayersCB.setVisible(True)
                        self.FmapsPerLayerCB.setVisible(True)
                        self.label_7.setVisible(True)
                        self.label_8.setVisible(True)
                        self.GroupEverything.setVisible(True)
                        self.GroupByFmap.setVisible(True)

	def layerIndexChanged(self):
		self.FmapCB.clear()
                Fmap_list=['']
                if(self.LayerCB.currentText() != ''):
                	for i in range(0, self.initial_blob[str(self.LayerCB.currentText())].data.shape[1]): #la primera capa
                        	Fmap_list.append(str(i))
                        self.FmapCB.addItems(Fmap_list)

		
	def __init__(self, controlador, statisticValue):
                super(self.__class__, self).__init__()
                self.setupUi(self)
                self.controlador=controlador
		self.statisticValue=statisticValue
		self.GenerateButton.clicked.connect(self.execute)
		self.GroupByFmap.stateChanged.connect(self.fmapCBchanged)
		self.GroupEverything.stateChanged.connect(self.everythingCBchanged)
		self.OnlyOneCheck.stateChanged.connect(self.onlyOneCheckChanged)
		self.LayerCB.currentIndexChanged.connect(self.layerIndexChanged)
		self.NumberOfImagesCB.setMaximum(100000)
		
class StatisticPanel(QtGui.QMainWindow, StatisticPanel.Ui_StatisticsPanel):
	controlador=1
	def change_to_panel(self, controlador, statistic):
		 window=GeneralStatisticControlPanel(controlador, statistic)
                 window.show()
                 self.hiden()
		

	def PixelsPerClassFunction(self):
		self.change_to_panel(self.controlador, 0)
	def PercentPixelPerClassFunction(self):
		self.change_to_panel(self.controlador, 1)
	def MinValuesFunction(self):
		self.change_to_panel(self.controlador, 2)
	
	def MaxValuesFunction(self):
		self.change_to_panel(self.controlador, 3)
	def AverageValuesFunction(self):
		self.change_to_panel(self.controlador, 4)
	def StdValuesFunction(self):
		self.change_to_panel(self.controlador, 5)
	
	def ScanFmapsFunction(self):
		self.change_to_panel(self.controlador, 6)
	def ComprehensiveAnalysis(self):
		self.change_to_panel(self.controlador, 7)
	
	

	def __init__(self, controlador):
        	super(self.__class__, self).__init__()
                self.setupUi(self)
                self.controlador=controlador
		self.PixelsPerClass.clicked.connect(self.PixelsPerClassFunction)
                self.PercentPixelPerClass.clicked.connect(self.PercentPixelPerClassFunction)
		self.MinValues.clicked.connect(self.MinValuesFunction)
		self.MaxValues.clicked.connect(self.MaxValuesFunction)
		self.AverageValues.clicked.connect(self.AverageValuesFunction)
		self.StdValues.clicked.connect(self.StdValuesFunction)
		self.ScanFmaps.clicked.connect(self.ScanFmapsFunction)
		self.Comprehensive.clicked.connect(self.ComprehensiveAnalysis)


class StatisticsWindow(QtGui.QMainWindow, Statistics_Menu_Windows.Ui_StatisticsWindow):
	controlador=1	
	def Specific_Statistics(self):
		self.controlador.start_getting_data_online(self)		
	def General_Statistics(self):
		window=StatisticPanel(self.controlador)
		window.show()
		self.hiden()
			

	def __init__(self, controlador):
		super(self.__class__, self).__init__()
                self.setupUi(self)
		self.controlador=controlador	
		self.ButtonSpecificStatistics.clicked.connect(self.Specific_Statistics)
		self.ButtonGeneralStatistics.clicked.connect(self.General_Statistics)
		self.resize(600, 400)
	
	
class IWindow(QtGui.QMainWindow, Initial_Window.Ui_MainWindow):
	state=0
	network_file=''
	weights_file=''
	images_path=''
	load_file=''
	controlador=1
	def __init__(self, controlador, parent=None):
		super(IWindow, self).__init__(parent)
		self.setupUi(self)
		self.ButtonReadData.clicked.connect(self.change_window_to_read)
		self.ButtonWriteFile.clicked.connect(self.change_window_to_write_file)		
		self.resize(600, 400)
		self.controlador=controlador

	def change_window_to_write_file(self):
		if(self.state==0):
			#Seleccionamos lo ficheros y pasariamos a escribir el fichero usando la red neuronal
			selecting_paths=Select_Paths_Window(self.controlador, mode=1)
                        selecting_paths.show()
                        self.hiden()
		
		elif(self.state==1):
			#Abrimos la ventana que permite seleccionar el fichero desde donde cargar los datos
			selecting_path_file = Load_File_Path_Window(self.controlador)
			selecting_path_file.show()
			self.hiden() 

	def change_window_to_read(self):
		if(self.state==0):
			self.ButtonReadData.setText('Read Data Online')
			self.ButtonWriteFile.setText('Read Data From File')
			self.state=1
		elif (self.state == 1):
			#Pasariamos a otra ventana		
			selecting_paths=Select_Paths_Window(self.controlador, mode=0)
			selecting_paths.show()
			self.hiden()

def i_am_like(pixel1, pixel2, accuracy):
	difference=abs(pixel1-pixel2)
	if(difference<=accuracy):
		return True
	return False

def get_list_colors():
	colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
	list_colors=[]
	for i in colors.items():
		if(i[1][0]=='#'): #Es un color
			R=int(i[1][1:3],16)
			G=int(i[1][3:5],16)
			B=int(i[1][5:7],16)
			list_colors.append([R,G,B])

	return list_colors

def generate_segments(pixeles, accuracy):
	height=pixeles.shape[0]
	weight=pixeles.shape[1]
	img_custom=np.zeros((height,weight), np.uint32)
	img_custom[0,0]=0
	library = {}
	library[0]=[[0,0]]
	i=0
	j=1
	while(i<height):
		while(j<weight):
			pixel_actual = pixeles[i,j]
			if(i==0 and j>0): # Parte de arriba de la imagen sin contar esquina
				if(i_am_like(pixel_actual, pixeles[i,j-1], accuracy)):
					img_custom[i,j]=img_custom[i,j-1]
					library[img_custom[i,j]].append([i,j])
				else:
					library[max(library)+1]=[[i,j]] #create a new key
                                	img_custom[i,j]=max(library) #we use the previous key

			elif(i>0 and j==0):
				if(i_am_like(pixel_actual, pixeles[i-1,j], accuracy)):
                                        img_custom[i,j]=img_custom[i-1,j]
                                        library[img_custom[i,j]].append([i,j])
                                else:
                                        library[max(library)+1]=[[i,j]] #create a new key
                                        img_custom[i,j]=max(library) #we use the previous key

							
		 	elif(i>0 and  j>0): # Estoy en el medio
				pixel_izquierda = pixeles[i,j-1] # Miramos para la izquierda		
				pixel_arriba = pixeles[i-1, j] # Miramos para arriba
				clase_izquierda = img_custom[i,j-1]
				clase_arriba = img_custom[i-1, j]
				soy_como_izquierda = i_am_like(pixel_actual, pixel_izquierda, accuracy)
				soy_como_arriba = i_am_like(pixel_actual, pixel_arriba, accuracy)
				if(soy_como_izquierda and soy_como_arriba):
					if(clase_izquierda==clase_arriba): #este pixel se une a la clase
						library[clase_arriba].append([i,j]) # lo meto al diccionario de esa clase
						img_custom[i,j]=clase_arriba
					
					elif(clase_izquierda != clase_arriba): #Hay que unificar las clases
						library[clase_arriba].append([i,j]) #Yo me uno a la clase de arriba
						img_custom[i,j]=clase_arriba
						#Ahora todos los de la clase de la clase izquierda pasan a ser clase arriba
						for x in library[clase_izquierda]:
							img_custom[x[0], x[1]]=clase_arriba
							library[clase_arriba].append([x[0], x[1]])	
						#print('CLASE IZQUIERDA BORRADA:')
						#print(clase_izquierda)
						#print(library[clase_izquierda])
						del library[clase_izquierda] #Borramos el rastro de la clase izquierda
						clase_izquierda=clase_arriba

				elif(soy_como_izquierda and (not soy_como_arriba)): #Nos unimos a la clase izquierda
						library[clase_izquierda].append([i, j])
						img_custom[i,j]=clase_izquierda

				elif((not soy_como_izquierda) and soy_como_arriba): #nos unimos a la clase arriba
						library[clase_arriba].append([i,j])
						img_custom[i,j]=clase_arriba 
				elif((not soy_como_izquierda) and (not soy_como_arriba)): #Creamos una nueva clase
						library[max(library)+1]=[[i,j]] #create a new key
                	                        img_custom[i,j]=max(library) #we use the previous key
		
								
			j=j+1	
		i=i+1	
		j=0	
	return img_custom, library


def set_colors(dictionary):
	n_colors=len(dictionary)
	max_colors=255*255*255
	range_colors=max_colors/n_colors
	current_color=np.uint32(0)
	mask = 255 # 00000111
	for key in dictionary:
		current_B=np.uint8(current_color & mask) # Exctracting B 
		current_G=np.uint8((current_color >> 8) & mask) #Extracting G
		current_R=np.uint8((current_color >> 16) & mask) #Extracting R
		dictionary[key]=[current_R, current_G, current_B] #Allocating the generated color to that value
		current_color+=range_colors
	return dictionary
		
def generate_dictionary(pixeles):
	diccionario={}
	height=pixeles.shape[0]
        weight=pixeles.shape[1]
	for i in range(0, height):
		for j in range(0, weight):
			value = pixeles[i, j]
			diccionario[value]=1 #Enabling such a value
	return diccionario
def Draw_fmap(pixeles, imname, currentLayer, currentFmap_str, dir_str):
	print('Drawing Image')
	dic=generate_dictionary(pixeles)
	dic=set_colors(dic)
	height=pixeles.shape[0]
        weight=pixeles.shape[1]
        outimg=np.zeros((height,weight,3), np.uint8)
	for i in range(0, height):
		for j in range(0,weight):
			value=pixeles[i, j]
			outimg[i,j,0]=dic[value][0] #Red
			outimg[i,j,1]=dic[value][1] #Green
			outimg[i,j,2]=dic[value][2] #Blue
	#Ya esta el fmap coloreado y se puede mostrar
	if(height<227): #Tamano de imagen que queremos
		factorh=(227/height)+2 #Minimo la incrementamos el doble
	else:
		factorh=1
	if(weight<227):
		factorw=(227/weight)+2 #Minimo la incrementamos el doble
	else:
		factorw=1
	
	if(height<227 or weight<227):
		outimg=cv2.resize(outimg, (0,0), fx=factorw, fy=factorh) #Si la imagen es muy pequena 
	cv2.imwrite(dir_str+'/'+imname+'_L_'+currentLayer+'_fmap_'+currentFmap_str+'.png',outimg)
	cv2.imshow("img", outimg) # Lo mostramos
	
	return outimg
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	
def Draw_Histogram(imageClases, imname, currentLayer, currentFmap_str, dir_str):
	print('Dibujando el Histograma..')
	plt.close()
	result = plt.hist(imageClases)
	plt.title("Histogram of pixel classification")
	plt.xlabel("Class")
	plt.ylabel("Frequency")
	#plt.show(block=False)
	plt.savefig(dir_str+'/'+imname+'_L_'+currentLayer+'_fmap_'+currentFmap_str+'_histogram.png')
#	plt.show()
	print('El histograma se ha guardado')
