from settings.cv_settings import *
import os
import json


def run():
    t = OUTPUT_JSON_PATH
    temp = json.load(open(t, 'r'))
    print temp
    with open(OUTPUT_CSV, 'w') as outfile:
        for k in temp.keys():
            bv = ''
            bv = bv + 'http://' + MACHINE_IP + k + ';;'
            for tc in temp[k].keys():
                bv = bv + ';' + temp[k][tc] + ';'
            bv = bv + '\n'
            print bv
            outfile.write(bv)
    return OUTPUT_CSV
