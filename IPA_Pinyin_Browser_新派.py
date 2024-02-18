import json
from zhconv import convert

with open('standard/total.json', encoding='utf-8') as f:
    ipas = json.load(f)
with open('standard_tones/pinyin.json', encoding='utf-8') as f:
    pinyins = json.load(f)

while 1:
    sentence = convert(input(), 'zh-cn')
    if sentence == '':
        break
    
    res_ipas = ''
    res_pinyins = ''

    for word in sentence:
        res = word
        in_list = 0
        exists = []
        for i in ipas:
            if word == convert(i[0], 'zh-cn'):
                middle_i = i[1].replace('si', 'ɕi').replace('sʰi', 'ɕʰi').replace('ʃ', 's').replace('ʅ', 'ɿ').replace('əŋ', 'ən').replace('iən', 'in')
                new_i = middle_i.replace('uã','ʷã')\
                    .replace('yẽ', 'yĩ').replace('õ', 'ʊ̠̃').replace('iẽ', 'ĩ').replace('ə̃', 'ɤ̃')\
                    .replace('ie','iɪ')\
                    .replace('ai','ɐɛ')\
                    .replace('au','ɐɔ')\
                    .replace('əu','əʊ')\
                    .replace('yɑ', 'yɔ').replace('uɑ', 'ʷɑ').replace('iɑ', 'i̹ɔ').replace('ɑ', 'ɔ').replace('i̹ɔʊ','iɑʊ').replace('ɔʊ','ɑʊ')\
                    .replace('o', 'ʊ̠')\
                    .replace('uə', 'ʷɤ').replace('ə', 'ɤ').replace('ɤn', 'ən').replace('ɤʊ', 'əʊ')\
                    .replace('ɸ', 'f')
                if new_i[0] == 'ʷ' or new_i[0] == 'u': new_i = 'w' + new_i[1:]
                if new_i in exists:
                    pass
                elif in_list == 0:
                    res += (' ' + new_i)
                    res_ipas += (' ' + new_i)
                    in_list = 1
                    exists.append(new_i)
                else:
                    res += ('/' + new_i)
                    res_ipas += ('/' + new_i)
                    exists.append(new_i)
        in_list = 0
        exists = []
        for i in pinyins:
            if word == convert(i[0], 'zh-cn'):
                middle_i = i[1].replace('zi', 'ji').replace('ci', 'qi').replace('si', 'xi').replace('jii', 'zii').replace('qii', 'cii').replace('xii', 'sii').replace('zh', 'z').replace('ch', 'c').replace('sh', 's').replace('iong', 'in').replace('ong', 'en')
                new_i = middle_i
                if new_i in exists:
                    pass
                elif in_list == 0:
                    res += (' ' + new_i)
                    res_pinyins += (' ' + new_i)
                    in_list = 1
                    exists.append(new_i)
                else:
                    res += ('/' + new_i)
                    res_pinyins += ('/' + new_i)
                    exists.append(new_i)
        #print(res, end=' ')

    print('\n'+sentence+'\n'+res_ipas+'\n'+res_pinyins+'\n')