from os import listdir

def get_image(path, images_list):
    if len(images_list)>0:
        return path + images_list.pop(0)
        
def get_list_images(path):
    images_list = [fi for fi in listdir(path)]
    return images_list
        
def get_netfile_paths():
    print('Please, Introduce prototxt path file')
    proto_file = input()
    print('Please, Introduce modeltxt path file')
    model_file = input()
    print('Please, Introduce path images folder')
    images_path = input()
    return proto_file, model_file, images_path 
