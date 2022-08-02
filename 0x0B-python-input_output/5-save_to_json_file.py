#!/usr/bin/python3
"""sve object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file using the json representation"""
    with open(filename, "w", encoding="utf-8) as f:
    json.dump(my_obj, f)
