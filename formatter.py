from settings.cv_settings import *
import os
import json


def run():
    t = OUTPUT_JSON_PATH
    temp = json.load(open(t, 'r'))
    with open(OUTPUT_CSV, 'w') as outfile:
        for k in temp.keys():
            bv = ''
            bv = bv + 'http://' + MACHINE_IP + k + ';;'
            for tc in temp[k].keys():
                bv = bv + tc + ';' + temp[k][tc] + ';'
            bv = bv + '/n'
    return OUTPUT_CSV
