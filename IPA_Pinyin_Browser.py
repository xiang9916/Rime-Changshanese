import json
from zhconv import convert

with open('standard/total.json', encoding='utf-8') as f:
    ipas = json.load(f)
with open('standard/pinyin.json', encoding='utf-8') as f:
    pinyins = json.load(f)

while 1:
    sentence = convert(input(), 'zh-tw')

    if sentence == '':
        break
    
    res_ipas = ''
    res_pinyins = ''

    for word in sentence:
        res = word
        in_list = 0
        for i in ipas:
            if word == i[0]:
                if in_list == 0:
                    res += (' ' + i[1])
                    res_ipas += (' ' + i[1])
                    in_list = 1
                else:
                    res += ('/' + i[1])
                    res_ipas += ('/' + i[1])
        in_list = 0
        for i in pinyins:
            if word == i[0]:
                if in_list == 0:
                    res += (' ' + i[1])
                    res_pinyins += (' ' + i[1])
                    in_list = 1
                else:
                    res += ('/' + i[1])
                    res_pinyins += ('/' + i[1])
        print(res, end=' ')

    print('\n'+res_ipas+'\n'+res_pinyins)