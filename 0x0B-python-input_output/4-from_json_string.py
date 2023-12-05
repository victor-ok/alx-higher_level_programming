#!/usr/bin/python3
"""defines a JSON-to-object function"""


import json


def from_json_string(my_obj):
    """Returns the python obj representation of a json string"""
    return json.loads(my_obj)
