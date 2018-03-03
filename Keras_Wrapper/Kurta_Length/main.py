from model_meta.meta_file import *
from settings.cv_settings import *
from utils import *
from common.utils import *


class KLCVObj(object):
    def __init__(self):
        # attributes stuffs
        self.model = get_model_from_meta('KURTA_LENGTH')
        self.tags = get_tags_from_meta('KURTA_LENGTH')



    def classify_for_image(self,img_pth):
        # Input pre processing here :
        ankle_present = check_if_ankle_joint_present(img_pth)
        #print "ROI_FLAG" , ankle_present
        if not ankle_present:
            predictions = 'Short Length'
            temp = {}
            return predictions, temp
        d = prepare_input_for_model(img_pth)
        # Make predictions here :
        predictions, temp = make_prediction(self.model, self.tags, d)
        # predictions = STRING (predicted value) , temp = {STRING(tag1) : STRING(probability)}
        # Post processing logic here : (Ensemble scoreing , voting , elimination)
        return predictions, temp


