import os
import json

with open('standard/pinyin.json', encoding='utf-8') as f:
    total_dictionary = json.load(f)

with open('yamls/Changshanese.dict.yaml', 'w+', encoding='utf-8') as f:
    f.writelines('# Rime dictionary\n')
    f.writelines('# encoding: utf-8\n')
    f.writelines('# auto-generated, do not edit directly\n')    
    f.writelines('---\n')
    f.writelines('name: "Changshanese"\n')
    f.writelines('version: "0.3"\n')
    f.writelines('sort: by_weight\n')
    f.writelines('use_preset_vocabulary: true\n')
    f.writelines('max_phrase_length: 7\n')
    f.writelines('min_phrase_weight: 100\n')
    f.writelines('...\n')
    for r in total_dictionary:
        f.writelines(r[0] + '\t' + r[1] + '\n')
        print(r[0], r[1])
print('done')

