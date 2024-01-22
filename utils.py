# -*- coding: utf-8 -*-
# @Author: Axel Bento da Silva
# @Date:   2024-01-22 13:30:54
# @Last Modified by:   Axel Bento da Silva
# @Last Modified time: 2024-01-22 13:41:53
import json

def load_json(path):
    with open(path, "r", encoding='utf-8') as f:
        return json.load(f)

def write_json(path, data):
    with open(path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_txt(path):
    with open(path, "r") as f:
        return f.readlines()
