import json
import os
from pprint import pprint
from itertools import chain


def get_data_from_json(file_path):
    file_path = os.path.join(os.getcwd(), file_path)
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)


data = get_data_from_json('3.1.formats.json.xml/newsafr.json')
# pprint(chain( for description in data['rss']['channel']['items'])
