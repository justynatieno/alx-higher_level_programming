#!/usr/bin/python3
""" from JSON string to object"""

import json


def from_json_string(my_str):
    """returns object represented by json string"""
    return json.loads(my_str)
