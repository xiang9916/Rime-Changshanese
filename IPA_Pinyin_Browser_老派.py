import json
from zhconv import convert

with open('standard_tones/total.json', encoding='utf-8') as f:
    ipas = json.load(f)
with open('standard_tones/pinyin.json', encoding='utf-8') as f:
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
        exists = []
        for i in ipas:
            if word == i[0]:
                middle_i = i[1]
                if middle_i in exists:
                    pass
                elif in_list == 0:
                    res += (' ' + middle_i)
                    res_ipas += (' ' + middle_i)
                    in_list = 1
                    exists.append(middle_i)
                else:
                    res += ('/' + middle_i)
                    res_ipas += ('/' + middle_i)
                    exists.append(middle_i)
        in_list = 0
        exists = []
        for i in pinyins:
            if word == i[0]:
                middle_i = i[1]
                if middle_i in exists:
                    pass
                elif in_list == 0:
                    res += (' ' + middle_i)
                    res_pinyins += (' ' + middle_i)
                    in_list = 1
                    exists.append(middle_i)
                else:
                    res += ('/' + middle_i)
                    res_pinyins += ('/' + middle_i)
                    exists.append(middle_i)
        #print(res, end=' ')

    print('\n'+res_ipas+'\n'+res_pinyins+'\n')