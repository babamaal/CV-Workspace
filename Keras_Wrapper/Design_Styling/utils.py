import cv2, os
desired_size = 224
from model_meta.meta_file import *
from model_meta.meta_file import *
import os
os.environ['PATH'] = "/home/ubuntu/bin:/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/cuda-8.0/bin:/snap/bin:/usr/local/cuda-8.0/bin:/home/ubuntu/codes/caffe/build/tools:/usr/local/cuda-8.0/bin:/usr/local/cuda-8.0/lib64"
from keras.preprocessing import image
from keras.models import Sequential, Model
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import numpy as np
from keras.layers import Dense, Dropout, Flatten, Input, GlobalAveragePooling2D
import keras, os, shutil, json, requests, urllib, cv2
from keras import backend as K
from datetime import datetime

def prepare_input_for_model(path_to_image):
	if not os.path.isfile(path_to_image):
		return "Incorrect file path"
	temp = create_square(path_to_image)
	cv2.imwrite('neck.jpg',temp)
	d = image.load_img('neck.jpg', target_size=(224, 224))
	d = image.img_to_array(d)
	d = np.expand_dims(d, axis=0)
	d = preprocess_input(d)
	return d
	

def create_square(im_pth):
    #tt = im_pth.replace('test','test11')
    #save_path = tt
    im = cv2.imread(im_pth)
    old_size = im.shape[:2] # old_size is in (height, width) format
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    
    # new_size should be in (width, height) format
    im = cv2.resize(im, (new_size[1], new_size[0]))
    
    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    
    color = [0, 0, 0]
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)   
    return new_im

def make_prediction(model,tags,d):
	temp = {}
	pr = model.predict(d.reshape((1,3,224,224)))
	t = 0
	for p in pr[0]:
		temp[tags[t]] = str(p)
		t+=1
	prediction = tags_to_be[np.argmax(pr)]
	return prediction , temp


