#imports here
from common.utils import *
from Neckline.main import NeckCVObj
from Design_Styling import DSCVObj
from Hemline import HemCVObj
from Kurta_Length import KLCVObj
from Kurta_Shape import KSCVObj
from Pattern_Coverage import PCCVObj
from Patterns import PatCVObj
from Prints import PrintCVObj
from Sleeve_Length import SLCVObj
from Sleeve_Styling import SSCVObj
from Slits import SlitCVObj

class GlobalCVObj(Object):
	def __init__(self):
		#Add your objects here.. repalce the ones coming from pytorch with PYTObj
		self.neckline = NeckCVObj()
		self.design_styling = DSCVObj()
		#self.hemline = HemCVObj()
		self.kurta_length = KLCVObj()
		self.kurta_shape = KSCVObj()
		self.pattern_coverage = PCCVObj()
		self.patterns = PatCVObj()
		self.prints = PrintCVObj()
		#self.sleeve_length = SLCVObj()
		#self.sleeve_styling = SSCVObj()
		self.slits = SlitCVObj()
		self.pytorch = PYTObj()



	def make_prediction_for_one_image(self,img_pth):
		final_pred  = {}
		#### Specific to neckline########
		neck_roi_pth = get_neck_roi(img_pth)
		pred , debug = self.neckline.classify_for_image(neck_roi_pth)
		final_pred['Neckline'] = pred
		#####Add more objects here#######
		pred , debug = self.design_styling.classify_for_image(img_pth)
		final_pred['Design Styling'] = pred

		pred , debug = self.hemline.classify_for_image(img_pth)
		final_pred['Hemline'] = pred
		
		pred , debug = self.kurta_length.classify_for_image(img_pth)
		final_pred['Kurta Length'] = pred
		
		pred , debug = self.kurta_shape.classify_for_image(img_pth)
		final_pred['Kurta Shape'] = pred
		
		pred , debug = self.pattern_coverage.classify_for_image(img_pth)
		final_pred['Pattern Coverage'] = pred
		
		pred , debug = self.patterns.classify_for_image(img_pth)
		final_pred['Patterns'] = pred
		
		pred , debug = self.prints.classify_for_image(img_pth)
		final_pred['Prints'] = pred
		
		pred , debug = self.sleeve_length.classify_for_image(img_pth)
		final_pred['Sleeve Length'] = pred

		pred , debug = self.sleeve_styling.classify_for_image(img_pth)
		final_pred['Sleeve Styling'] = pred

		pred , debug = self.slits.classify_for_image(img_pth)
		final_pred['Slits'] = pred

		return final_pred

