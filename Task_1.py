import json
import os
from pprint import pprint
from itertools import chain
from collections import Counter


def get_data_from_json(file_path):
    file_path = os.path.join(os.getcwd(), file_path)
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)


data = get_data_from_json('3.1.formats.json.xml/newsafr.json')
descriptions = chain.from_iterable(item['description'].split() for item in data['rss']['channel']['items'])
words = (word for word in descriptions if len(word) > 6)
most_common = Counter(words).most_common(10)
print(most_common)
