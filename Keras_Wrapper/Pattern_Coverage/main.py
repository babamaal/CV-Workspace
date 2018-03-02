from model_meta.meta_file import *
from settings.cv_settings import *
from utils import *
from common.utils import *


class PCCVObj(object):
    def __init__(self):
        # attributes stuffs
        self.model = get_model_from_meta('PATTERN_COVERAGE')
        self.tags = get_tags_from_meta('PATTERN_COVERAGE')



    def classify_for_image(img_pth):
        # Input pre processing here :
        d = prepare_input_for_model(img_pth)
        # Make predictions here :
        predictions , temp = make_prediction(self.model , self.tags, d)
        # predictions = STRING (predicted value) , temp = {STRING(tag1) : STRING(probability)}
        # Post processing logic here : (Ensemble scoreing , voting , elimination)
        return predictions ,temp


