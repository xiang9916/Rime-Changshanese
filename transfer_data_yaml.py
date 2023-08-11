import os
import json

filelist = os.listdir('data')
if '.DS_store' in filelist:
    del filelist['.DS_store']

total_dictionary_list = []
for filename in filelist:
    if filename == '.DS_Store':
        continue
    print(filename)
    with open('data/{}'.format(filename)) as f:
        dictionary = json.load(f)
        total_dictionary_list.extend(dictionary)
total_dictionary = []
for r in total_dictionary_list:
    total_dictionary.append((r[0], r[1]))
total_dictionary = list({}.fromkeys(total_dictionary).keys())

with open('yamls/Changshanese.dict.yaml', 'w+') as f:
    f.writelines('# Rime dictionary\n')
    f.writelines('# encoding: utf-8\n')
    f.writelines('# auto-generated, do not edit directly\n')    
    f.writelines('---\n')
    f.writelines('name: "Changsha"\n')
    f.writelines('version: "0.10"\n')
    f.writelines('sort: by_weight\n')
    f.writelines('use_preset_vocabulary: true\n')
    f.writelines('max_phrase_length: 7\n')
    f.writelines('min_phrase_weight: 100\n')
    f.writelines('...\n')
    for r in total_dictionary:
        f.writelines(r[0] + '\t' + r[1] + '\n')
print('done')

