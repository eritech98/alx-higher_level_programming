#!/usr/bin/python3

"""
Adds all arguments to a Python list, and then save them to a file.
"""
import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if os.path.exists('add_item.json'):
    lis = list(load_from_json_file('add_item.json'))
else:
    lis = []

for i in sys.argv[1:]:
    lis.append(i)

save_to_json_file(lis, 'add_item.json')
