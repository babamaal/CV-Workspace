# imports here
import os
os.environ['PATH'] = "/home/ubuntu/bin:/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/cuda-8.0/bin:/snap/bin:/usr/local/cuda-8.0/bin:/home/ubuntu/codes/caffe/build/tools:/usr/local/cuda-8.0/bin:/usr/local/cuda-8.0/lib64"
from Pytorch_Wrapper.main import PYTObj
from Keras_Wrapper.Neckline.main import NeckCVObj
from Keras_Wrapper.Design_Styling.main import DSCVObj
#from Hemline import HemCVObj
from common.utils import *
from Keras_Wrapper.Kurta_Length.main import KLCVObj
#from Keras_Wrapper.Kurta_Shape.main import KSCVObj
from Keras_Wrapper.Pattern_Coverage.main import PCCVObj
from Keras_Wrapper.Patterns.main import PatCVObj
from Keras_Wrapper.Prints.main import PrintCVObj
#from Sleeve_Length import SLCVObj
#from Sleeve_Styling import SSCVObj
from Keras_Wrapper.Slits.main import SlitCVObj


class GlobalCVObj(object):
    def __init__(self):
        # Add your objects here.. repalce the ones coming from pytorch with PYTObj
        self.neckline = NeckCVObj()
        self.design_styling = DSCVObj()
        #self.hemline = HemCVObj()
        #self.kurta_length = KLCVObj()
        #self.pattern_coverage = PCCVObj()
        #self.patterns = PatCVObj()
        self.prints = PrintCVObj()
        #self.sleeve_length = SLCVObj()
        #self.sleeve_styling = SSCVObj()
        self.slits = SlitCVObj()
        self.pytorch = PYTObj()

    def make_prediction_for_one_image(self, img_pth):
        final_pred = {}
        #### Specific to neckline########
        neck_roi_pth = get_neck_roi(img_pth)
        print neck_roi_pth
        pred, debug = self.neckline.classify_for_image(neck_roi_pth)
        final_pred['Neckline'] = pred
        #####Add more objects here#######
        pred, debug = self.design_styling.classify_for_image(img_pth)
        final_pred['Design Styling'] = pred

        #pred, debug = self.kurta_length.classify_for_image(img_pth)
        #final_pred['Kurta Length'] = pred

        #pred, debug = self.pattern_coverage.classify_for_image(img_pth)
        #final_pred['Pattern Coverage'] = pred

        #pred, debug = self.patterns.classify_for_image(img_pth)
        #final_pred['Patterns'] = pred

        pred, debug = self.prints.classify_for_image(img_pth)
        final_pred['Prints'] = pred

        #pred , debug = self.sleeve_length.classify_for_image(img_pth)
        #final_pred['Sleeve Length'] = pred

        #pred , debug = self.sleeve_styling.classify_for_image(img_pth)
        #final_pred['Sleeve Styling'] = pred

        pred, debug = self.slits.classify_for_image(img_pth)
        final_pred['Slits'] = pred

        pred = self.PYTObj.classify_for_image(img_pth)
        for i in pred.keys():
            final_pred[i] = pred[i]

        return final_pred
