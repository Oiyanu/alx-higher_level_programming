#!/usr/bin/python3
"""Defines load_from_json_file() function"""
import json


def load_from_json_file(filename):
    """
    Deserializes JSON string

    Args:
        filename: path to JSON file

    Return:
        python object
    """
    with open(filename, encoding="UTF-8") as f:
        data = json.load(f)
        return data
