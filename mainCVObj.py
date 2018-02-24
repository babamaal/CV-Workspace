#imports here
from common.utils import *
from Neckline.main import NeckCVObj

class GlobalCVObj(Object):
	def __init__(self):
		#Add your objects here
		self.neckline = NeckCVObj()


	def make_prediction_for_one_image(self,img_pth):
		final_pred  = {}
		#### Specific to neckline########
		neck_roi_pth = get_neck_roi(img_pth)
		pred , debug = self.neckline.classify_for_image(neck_roi_pth)
		final_pred['Neckline'] = pred
		#####Add more objects here#######
		return final_pred
