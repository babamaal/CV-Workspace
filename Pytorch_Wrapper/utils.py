import zmq
import json


def make_pytorch_network_call(img_url):
    request_data = [{
            'img': img_url,
            'attributes': ['all']
        }]
    context = zmq.Context()
    socket = context.socket(zmq.DEALER)
    socket.connect(PYTORCH_SERVER)
    socket.send_unicode(json.dumps(request_data))
    t =  socket.recv()
    return t

def format_pytorch_results(resp):
    temp = {}
    return temp
