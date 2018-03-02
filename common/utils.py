import os
import json
import keras
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
from keras.applications.imagenet_utils import preprocess_input
import time
from model_meta.meta_file import *
from settings.cv_settings import *

def convert_keras_models_to_json(model_dir):
	model_paths =  os.listdir(model_dir)
	for mp in model_paths:
		model = keras.models.load_model(os.path.join(model_dir,mp))
		mpf = mp.split('.')[0]
		json_model_arch = model.to_json()
		f = open(os.path.join(MODEL_JSON_PATH,mpf+'.json'), 'w')
		f.write(json_model_arch)
		f.close()
	tt = os.listdir(MODEL_JSON_PATH)
	if len(tt) == len(model_paths):
		print 'DONE WITH CONVERSION'
	else:
		print "Something went wrong!!"

#Json based load
def load_keras_models(model_path):
	t_begin = time.time()
	model_name = model_path.split('/')[-1].split('.')[0]
	json_file = os.path.join(MODEL_JSON_PATH,model_name+'.json')
	f = open(json_file,'r')
	json_model_arch = f.read()
	jmodel = model_from_json(json_model_arch)
	jmodel.load_weights(model_path)
	t_end = time.time()
	print (t_end - t_begin)
	f.close()
	return jmodel



def load_models_per_backend(info):
	if info['TYPE'] == 'keras':
		return load_keras_models(info['PATH'])
	else:
		return load_pytorch_models(info['PATH'])


def get_model_from_meta(model_name):
	info = META_INFO[model_name] if model_name in META_INFO else None
	if info:
		model = load_models_per_backend(info)
		return model
	return False


def get_tags_from_meta(model_name):
	info = META_INFO[model_name] if model_name in META_INFO else None
	if info:
		tags = info['TAGS']
		return tags
	return False


def get_neck_roi(img_pth):
	fn = img_pth.split('/')[-1]
	return os.path.join(ROI_SAVE_PATH_NECK,fn)