import zmq
import json
from settings import cv_settings

def make_pytorch_network_call(img, models=['all']):
    request_data = [{'img': img, 'attributes': models }]
    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    socket.connect(cv_settings.PYTORCH_SERVER)
    socket.send_unicode(json.dumps(request_data))
    return socket.recv()


def format_pytorch_results(resp):
    temp = {}
    t = json.loads(resp)[0]
    tclass = t.keys()
    for tc in tclass:
        if tc != 'img':
            temp[tc] = t[tc]['pred']
    return temp
