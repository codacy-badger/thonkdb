import json
import random
import os

class JSON():
    def _read_json(self, filename):
        with open(filename, encoding='utf-8', mode="r") as f:
            data = json.load(f)
        return data

def get_value(path, value):
    #####
