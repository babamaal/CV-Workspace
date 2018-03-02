from model_meta.meta_file import *
from settings.cv_settings import *
from utils import *
from common.utils import *


class PYTObj(object):
    def __init__(self):
        # attributes stuffs
        self.check_server_running = False



    def classify_for_image(self, img_pth):
        # Input pre processing here :
        img_url = 'http://' +  MACHINE_IP +  img_pth
        # Make predictions here :
        response = make_pytorch_network_call(img_url)
        # predictions = STRING (predicted value) , temp = {STRING(tag1) : STRING(probability)}
        # Post processing logic here : (Ensemble scoreing , voting , elimination)
        predictions = format_pytorch_results(response)
        return predictions


