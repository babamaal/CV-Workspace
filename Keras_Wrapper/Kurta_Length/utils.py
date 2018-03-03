import cv2
desired_size = 224
from model_meta.meta_file import *
import os
os.environ['PATH'] = "/home/ubuntu/bin:/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/cuda-8.0/bin:/snap/bin:/usr/local/cuda-8.0/bin:/home/ubuntu/codes/caffe/build/tools:/usr/local/cuda-8.0/bin:/usr/local/cuda-8.0/lib64"
from keras.preprocessing import image
from keras.models import Sequential, Model
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import numpy as np
from keras.layers import Dense, Dropout, Flatten, Input, GlobalAveragePooling2D
import keras
import os
import shutil
import json
import requests
import urllib
import cv2
from keras import backend as K
from datetime import datetime
from settings.cv_settings import *


def prepare_input_for_model(path_to_image):
    if not os.path.isfile(path_to_image):
        return "Incorrect file path"
    temp = create_square(path_to_image)
    cv2.imwrite('neck.jpg', temp)
    d = image.load_img('neck.jpg', target_size=(224, 224))
    d = image.img_to_array(d)
    d = np.expand_dims(d, axis=0)
    d = preprocess_input(d)
    return d


def create_square(im_pth):
    # tt = im_pth.replace('test','test11')
    # save_path = tt
    im = cv2.imread(im_pth)
    old_size = im.shape[:2]  # old_size is in (height, width) format
    ratio = float(desired_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])

    # new_size should be in (width, height) format
    im = cv2.resize(im, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    color = [0, 0, 0]
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
                                value=color)
    return new_im


def make_prediction(model, tags, d):
    temp = {}
    pr = model.predict(d.reshape((1, 3, 224, 224)))
    t = 0
    for p in pr[0]:
        temp[tags[t]] = str(p)
        t += 1
    prediction = tags[np.argmax(pr)]
    return prediction, temp


def check_if_ankle_joint_present(img_pth):
    t_r = os.listdir(POSE_NETWORK_OUTPUT)
    fname = img_pth.split('/')[-1].split('.')[0]
    json_name = fname + '_keypoints.json'
    t = json.load(open(os.path.join(POSE_NETWORK_OUTPUT, json_name), 'r'))
    ############# check if ankle join present in response obj ###############
    g = convert_pose_network_output(t)
    if not g:
        return check_ankle(g)
    return False


BODY_PART_DICT = {
    0: "Nose",
    1: "Neck",
    2: "RShoulder",
    3: "RElbow",
    4: "RWrist",
    5: "LShoulder",
    6: "LElbow",
    7: "LWrist",
    8: "RHip",
    9: "RKnee",
    10: "RAnkle",
    11: "LHip",
    12: "LKnee",
    13: "LAnkle",
    14: "REye",
    15: "LEye",
    16: "REar",
    17: "LEar",
    18: "Bkg"
}

POSE_COCO_PAIRS = [('Neck', 'RShoulder'), ('Neck', 'LShoulder'), ('RShoulder', 'RElbow'),
                   ('RElbow', 'RWrist'), ('LShoulder', 'LElbow'), ('LElbow',
                                                                   'LWrist'), ('Neck', 'RHip'), ('RHip', 'RKnee'),
                   ('RKnee', 'RAnkle'), ('Neck', 'LHip'), ('LHip',
                                                           'LKnee'), ('LKnee', 'LAnkle'), ('Neck', 'Nose'),
                   ('Nose', 'REye'), ('REye', 'REar'), ('Nose', 'LEye'), ('LEye', 'LEar'), ('RShoulder', 'REar'), ('LShouder', 'LEar')]

DEFINED_ROI = {
    'right_arm': ('RShoulder', 'RElbow', 'RWrist'),
    'left_arm': ('LShoulder', 'LElbow', 'LWrist'),
    'shoulder_area': ('RShoulder', 'Neck', 'LShoulder'),
    'torso': ('RShoulder', 'Neck', 'LShoulder', 'LHip', 'RHip'),
    'bottom': ('RHip', 'LHip', 'LAnkle', 'RAnkle'),
    'bust_area': ('RShoulder', 'Neck', 'LShoulder')
}


def convert_pose_network_output(json_path):
    temp = json_path
    if len(temp['people']) < 1:
        return False
    key_points = temp['people'][0]['pose_keypoints']
    fmt_key_points = []
    count = 0
    for i in range(54):
        if count + 2 < 54:
            temp = [key_points[count],
                    key_points[count + 1], key_points[count + 2]]
            # print temp
            fmt_key_points.append(temp)
        count += 3
    final_ret = {}
    for i in range(18):
        final_ret[BODY_PART_DICT[i]] = fmt_key_points[i]
    return final_ret


def check_ankle(final_ret):
    if final_ret['LAnkle'][0] != 0.0:
        return True
    return False
