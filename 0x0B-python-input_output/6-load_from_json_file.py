#!/usr/bin/python3
"""define a json file reading function"""

import json


def load_from_json_file(filename):
    """creates a python object from json"""
    with open(filename) as f:
        return json.load(f)
