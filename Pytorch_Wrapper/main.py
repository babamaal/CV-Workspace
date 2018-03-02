from model_meta.meta_file import *
from settings.cv_settings import *
from utils import *
from common.utils import *
import urllib

class PYTObj(object):
    def __init__(self):
        # attributes stuffs
        self.check_server_running = False


    def classify_for_image(self, img_pth):
        # Input pre processing here :
        img_url = MACHINE_IP + img_pth
        print img_url
        t = urllib.quote_plus(img_url)
        # Make predictions here :
        response = make_pytorch_network_call(t)
        # predictions = STRING (predicted value) , temp = {STRING(tag1) : STRING(probability)}
        # Post processing logic here : (Ensemble scoreing , voting , elimination)
        #predictions = format_pytorch_results(response)
        return response


