import xml.etree.ElementTree as et
import os
from collections import Counter


def get_data_from_xml(file_path):
    file_path = os.path.join(os.getcwd(), file_path)
    parser = et.XMLParser(encoding='utf-8')
    root = et.parse(file_path, parser).getroot()

    text = root.findall('channel/item/description')
    return text


def get_words(texts, length):
    for t in texts:
        for word in t.text.split():
            if len(word) > length:
                yield word


def top_words(text, word_length=6, top=10):
    words = get_words(text, word_length)
    return Counter(words).most_common(top)


data = get_data_from_xml('3.1.formats.json.xml/newsafr.xml')
print(top_words(data))
