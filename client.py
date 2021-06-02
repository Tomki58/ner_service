#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

import requests

from common.vercreader import read_verc

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[error] Need file path as argument.")
        exit(1)

    filename = sys.argv[1]
    with open(filename, "r") as source:
        wm = json.load(source)
        map_ = read_verc(wm)

    payload = json.dumps({"data": map_})
    response = requests.post("http://localhost:10000/api/v1/tag_sentence", data=payload)
    try:
        result = response.json()
        print(json.dumps(result, indent=2))
    except:
        print(response.text)
