from settings.cv_settings import *
import os
import json

output = ['hemline', 'placement', 'Kurta Length', 'sleeve_style', 'Neckline','shape', 'sleeve_length', 'Slits', 'print', 'design_style', 'yoke']
keys = {
    'hemline': 'Hemline',
    'placement': 'Pattern Coverage',
    'Kurta Length': 'Length',
    'sleeve_style': 'Sleeve Styling',
    'Neckline': 'Neck',
    'shape': 'Shape',
    'sleeve_length': 'Sleeve Length',
    'Slits': 'Slit Details',
    'print': 'Print/Pattern Type',
    'design_style': 'Design Styling',
    'yoke': 'Pattern'
}

tag_map = {
    'Print/Pattern Type': {
        "Striped": "Striped",
        "Solid": "Solid",
        "Checked": "Checked",
        "Woven Design": "Woven Design",
        "Animal": "Animal",
        "Tribal": "Tribal",
        "Bandhani": "Bandhani",
        "Floral": "Floral",
        "Geometric": "Geometric",
        "Paisley": "Paisley",
        "Abstract": "Abstract",
        "Leheriya": "Leheriya",
        "Chevron": "Chevron",
        "Colourblocked": "Colourblocked",
        "Quirky": "Quirky",
        "Ethnic Motifs": "Ethnic Motifs",
        "Embellished": "Embellished",
        "Shibori" : 'Dyed'
    },
    'Slit Details': {
        "front_slit": "Front Slit",
        "multiple_slits": "Multiple Slits",
        "no_slit": ''
    },
    'Sleeve Length': {
        "long-sleeves": "Long Sleeves",
        "short-sleeves": "Short Sleeves",
        "sleeveless": "Sleeveless",
        "three-fourth-sleeves": "Three-Quarter Sleeves",
    },
    'Neck': {
        'v-neck': "V-Neck",
        'round neck': "Round Neck",
        'boat neck': "Boat Neck",
        'halter neck': "Halter Neck",
        'mandarin collar': "Mandarin Collar",
        'shirt collar': "Shirt Collar",
        'square neck': "Square Neck",
        'cowl neck': "Cowl Neck",
        'key hole neckline': "Keyhole Neck",
        'sweetheart neck': "Sweetheart Neck",
    },
    'Sleeve Styling': {
        "cap-sleeves": "Cap Sleeves",
        "puff-sleeves": "Puff Sleeves",
        "flared-sleeves": "Flared Sleeves",
        "regular-sleeves": "Regular Sleeves",
        "cold-shoulder-sleeves": "Cold-Shoulder Sleeves",
        "no-sleeves": "No Sleeves",
        "strap": "Shoulder Straps",
        "roll-up-sleeves": "Roll-Up Sleeves"
    },
    'Shape': {
        "Anarkali": "Anarkali",
        "Straight": "Straight",
        "A_Line": "A-Line",
        "KAftan": "Kaftan",
    },
    'Length': {
        "knee_length": "Knee Length",
        "calf_length": "Calf Length",
        "ankle_length": "Ankle Length",
        "Short Length": "Above Knee",
    },
    'Hemline': {
        "high-low": "High-Low",
        "straight": "Straight",
        "curved": "Curved",
        "asymmetric": "Asymmetric",
        "flared": "Flared",
    },
    'Design Styling': {
        "angrakha": "Angrakha",
        "empire": "Empire",
        "tiered": "Tiered",
        "regular": "Regular",
        "panelled": "Panelled",
        "pleated": "Pleated",
        "high Slit": "High Slit",
        "layered": "Layered",
    },
    'Pattern Coverage': {
        "placement-print": "Placement Print",
        "all-over-print": "All Over Print",
        "solid": "No Prints"
    },
    'Pattern': {
        'Yoke': 'Yoke Design',
        'No Yoke': 'none'
    }
}


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
                    bv = bv + ';' + tag_map[keys[tc]][temp[k][tc]]
                else:
                    bv = bv + ';' + '   '
            bv = bv + '\n'
            print bv
            outfile.write(bv)
    return OUTPUT_CSV
