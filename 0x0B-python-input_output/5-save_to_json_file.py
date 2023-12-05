#!/usr/bin/python3
"""defines a JSON file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """
    write obj to a txt file using JSON representation
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
