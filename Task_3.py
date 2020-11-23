import os
import os.path as op
from collections import namedtuple

files_dir = op.join(os.getcwd(), '2.4.files/sorted/')
data = []
File = namedtuple('File', ['name', 'text'])


for file_name in os.listdir(files_dir):
    path = op.join(files_dir, file_name)
    if op.isfile(path):
        with open(path, encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f]
            data.append(File(name=file_name, text=lines))


data_sorted = sorted(data, key=lambda i: len(i.text))

with open('task_3_result.txt', mode='w', encoding='utf-8') as f:
    for file in data_sorted:
        f.write(f'{file.name}\n')
        f.write(f'{str(len(file.text))}\n')
        for line in file.text:
            f.write(line + '\n')

