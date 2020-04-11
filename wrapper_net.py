import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import caffe
#This module control the data of the net
class wrapper_net: 
    
    net = []    
    transformer = []    
    images_list = []
    images_path = []
    current_index=0
    mean_file='/home/paco/Caffe/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy'
    def __init__(self, proto_file, model_file, images_list, images_path):
        self.net = caffe.Net(proto_file, model_file, caffe.TEST) 
        # Esta ejecucion no afecta al resto del programa pero sirve para quantizar los pesos al vuelo cuando se usa ristretto modificado
   	#Esta modificacion se debe a la naturaleza de ristretto de cuantizar los pesos al vuelo en lugar de con la carga de la red. 
 	#Esta modificacion no afecta a si se usa o no ristretto
  	out_garbage=self.net.forward() #
        #Empieza el codigo para leer las imagenes
        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        #self.transformer.set_mean('data', np.load(self.mean_file).mean(1).mean(1)) #Poner esta
	img_mean = np.array([103.94, 116.78, 123.68], dtype=np.float32)
	self.transformer.set_mean('data', img_mean)
        self.transformer.set_transpose('data', (2,0,1))
        self.transformer.set_channel_swap('data', (2,1,0))
        self.transformer.set_raw_scale('data', 255.0)
        self.net.blobs['data'].reshape(1,3,227,227)
#	self.transformer.set_input_scale('data', 0.017) #comment for squeezenet
        self.images_list = images_list
        self.images_path = images_path
	self.current_index=0 
        
    def get_next_data(self):
        blobs = []
        if (self.current_index>=len(self.images_list)):
            return False, blobs, "", [], [], []
        image_name = self.images_list[self.current_index] # Puede generar una excepcion ! Manejar en la funcion que la llame 
	self.current_index+=1
        im = caffe.io.load_image(self.images_path+'/'+image_name)
	print len(im)
	print image_name
        self.net.blobs['data'].data[...] = self.transformer.preprocess('data', im)
        out = self.net.forward()
	#predicted predicted class
	#print out['prob'].argmax()

#print predicted labels
	labels = np.loadtxt("/home/paco/Caffe/caffe/data/ilsvrc12/synset_words.txt", str, delimiter='\t')
	top_k = self.net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
	print labels[top_k]
        #Ver como recorrer todos los blobs
        return True, self.net.blobs, image_name, self.net.params, self.net.layers, self.net._layer_names

    def restart_index(self):
	self.current_index=0
