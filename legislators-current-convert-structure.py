#!/usr/bin/python3

import json
from urllib.request import urlopen

input = urlopen('https://theunitedstates.io/congress-legislators/legislators-current.json')
input_array = json.loads(input.read())
output_dict = {'current_legislators': {}}

for legislator_dict in input_array:
    official_name = legislator_dict['name']['official_full']
    official_name = official_name.translate({ord('.'): None})
    output_dict['current_legislators'][official_name] = legislator_dict

output_file = open('legislators-by-name.json', 'w')
json.dump(output_dict, output_file)
