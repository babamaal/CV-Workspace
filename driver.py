import os
os.environ['PATH'] = "/home/ubuntu/bin:/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/cuda-8.0/bin:/snap/bin:/usr/local/cuda-8.0/bin:/home/ubuntu/codes/caffe/build/tools:/usr/local/cuda-8.0/bin:/usr/local/cuda-8.0/lib64"
from mainCVObj import GlobalCVObj
import json
import urllib
from settings.cv_settings import *
from tqdm import tqdm


def download_images_from_csv(csv_path):
    shutil.rmtree(IMAGE_DATA_SAVE_PATH)
    os.mkdir(IMAGE_DATA_SAVE_PATH)
    with open(csv_path, 'r') as infile:
        for url in infile:
            fname = url.split('/')[-1]
            try:
                urllib.urlretrieve(url, os.path.join(
                    IMAGE_DATA_SAVE_PATH, fname))
            except:
                print "Failed for url : ", url
    return True


def main(skip=0):
    # datetime
    out = {}
    if skip != 0:
        out = json.load(open(OUTPUT_JSON_PATH, 'r'))
    # Initialize GLOBAL CV OBJ
    gco = GlobalCVObj()
    try:
        inp_file = os.listdir(INPUT_CSV_PATH)[0]
    except:
        print "CSV NOT IN PATH || DATA ALREADY THERE!!"
    if len(os.listdir(IMAGE_DATA_SAVE_PATH)) == 0:
        dwn_flag = download_images_from_csv(inp_file)
        if not dwn_flag:
            return "SOMETHING WENT WRONG WHILE DOWNLOADING IMAGES, PLEASE RESTART!"
    files = [os.path.join(IMAGE_DATA_SAVE_PATH, i)
             for i in os.listdir(IMAGE_DATA_SAVE_PATH)]
    if skip == 0:
        count = 0
    else:
        count = skip
    for l in tqdm(range(len(files)), ncols=70):
        f = files[l]
        if l > count:
            pred = gco.make_prediction_for_one_image(f)
            out[f] = pred
            count += 1
            #print "Done with : ", count
    json.dump(out, open(OUTPUT_JSON_PATH, 'w'))
    return "DONE WITH THE CSV!!!"
