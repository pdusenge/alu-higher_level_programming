#!/usr/bin/python3
import sys
import importlib.util
from os.path import exists

filename = "add_item.json"

# Dynamically load the modules using importlib
def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Paths to your modules
save_to_json_file_path = './5-save_to_json_file.py'
load_from_json_file_path = './6-load_from_json_file.py'

# Dynamically load the modules
save_to_json_file = load_module('save_to_json_file', save_to_json_file_path)
load_from_json_file = load_module('load_from_json_file', load_from_json_file_path)

if exists(filename):
    my_list = load_from_json_file.load_from_json_file(filename)
    print("Loaded list:", my_list)  # Debugging print
else:
    my_list = []
    print("File not found, starting with empty list")  # Debugging print

my_list.extend(sys.argv[1:])
print("Updated list:", my_list)  # Debugging print

save_to_json_file.save_to_json_file(my_list, filename)
