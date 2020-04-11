import wrapper_net
import my_custom_io

class read_values_online:
        network_file=''
        weights_file=''
        image_path=''
        recovery_file=''
	wnet=0	
	images_list=None
	def __init__(self):
		pass	

        def init_net(self, network_file, weights_file, image_path):
                self.network_file=network_file
                self.weights_file=weights_file
                self.image_path=image_path
		self.images_list = my_custom_io.get_list_images(image_path)
		self.wnet  = wrapper_net.wrapper_net(self.network_file, self.weights_file, self.images_list, self.image_path)
        def get_next_data(self):
                ok, blobs, image_name, params, layers, layer_names = self.wnet.get_next_data()
		
#                if ok==True:
 #                       for key in blobs:
  #                              print key

		return ok, blobs, image_name, params, layers, layer_names
	
	def restart_net(self):	
		self.wnet.restart_index()
