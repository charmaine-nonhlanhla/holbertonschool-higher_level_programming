#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

templist = []
filename = 'add_item.json'
if os.path.exists(filename) is True:
    templist = load_from_json_file(filename)
for i in sys.argv[1:]:
    templist.append(i)

save_to_json_file(templist, filename)
