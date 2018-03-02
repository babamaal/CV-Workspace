from mainCVObj import GlobalCVObj
import json ,urllib, os 
from settings.cv_settings import *

def download_images_from_csv(csv_path):
	shutil.rmtree(IMAGE_DATA_SAVE_PATH)
	os.mkdir(IMAGE_DATA_SAVE_PATH)
	with open(csv_path,'r') as infile:
		for url in infile:
			fname = url.split('/')[-1]
			try:
				urllib.urlretrieve(url,os.path.join(IMAGE_DATA_SAVE_PATH,fname))
			except:
				print "Failed for url : " ,url
	return True



def main(skip=0):
	out = {}
	if skip!=0:
		out = json.load(open(OUTPUT_JSON_PATH,'r'))
	## Initialize GLOBAL CV OBJ 
	gco = GlobalCVObj()
	inp_file = os.listdir(INPUT_CSV_PATH)[0]
	dwn_flag = download_images_from_csv(inp_file)
	if not dwn_flag:
		return "SOMETHING WENT WRONG WHILE DOWNLOADING IMAGES, PLEASE RESTART!"
	files = [os.path.join(IMAGE_DATA_SAVE_PATH,i) for i in os.listdir(IMAGE_DATA_SAVE_PATH)]
	if skip ==0:
		count = 0
	else:
		count = skip
	for f in files:
		pred = gco.make_prediction_for_one_image(f)
		out[f] = pred
		count+=1
		print "Done with : " ,count
	json.dump(out,open(OUTPUT_JSON_PATH,'w'))
	return "DONE WITH THE CSV!!!"