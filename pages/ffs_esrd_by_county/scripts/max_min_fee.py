import json
from pprint import pprint

with open('./pages/ffs_esrd_by_county/data/2015_ffs.json') as json_data:
    d = json.load(json_data)
    json_data.close()

pc_exp_esrds = [float(item['per_capita_exp_esrd']) for item in d if 'per_capita_exp_esrd' in item]

min(pc_exp_esrds)
max(pc_exp_esrds)
