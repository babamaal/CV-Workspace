import os
from model_meta.meta_file import *

def load_keras_models(model_path):
	return model


def load_pytorch_models(model_path):
	return model


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