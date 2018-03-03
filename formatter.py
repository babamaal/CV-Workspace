from settings.cv_settings import *
import os
import json

output = ['hemline','placement','Kurta Length','sleeve_style','Neckline','shape','sleeve_length','Slits','print','Design Styling']

def run():
    t = OUTPUT_JSON_PATH
    temp = json.load(open(t, 'r'))
    print temp
    with open(OUTPUT_CSV, 'w') as outfile:
        for k in temp.keys():
            bv = ''
            bv = bv + 'http://' + MACHINE_IP + k + ';;'
            for tc in output:
                if tc in temp[k]:
                    bv = bv + ';' + temp[k][tc]
                else:
                    bv = bv + ';' + '   '
            bv = bv + '\n'
            print bv
            outfile.write(bv)
    return OUTPUT_CSV
