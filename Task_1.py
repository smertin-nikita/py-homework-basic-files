import json
import os
from collections import Counter


def get_data_from_json(file_path):
    file_path = os.path.join(os.getcwd(), file_path)
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)


def get_words(texts, length):
    for text in texts:
        for word in text.split():
            if len(word) > length:
                yield word


def top_words(text, word_length=6, top=10):
    words = get_words(text, word_length)
    return Counter(words).most_common(top)


data = get_data_from_json('3.1.formats.json.xml/newsafr.json')
texts = (item['description'] for item in data['rss']['channel']['items'])


print(top_words(texts))
