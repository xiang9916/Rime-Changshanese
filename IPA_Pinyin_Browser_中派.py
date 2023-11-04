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
                middle_i = i[1].replace('si', 'ɕi').replace('sʰi', 'ɕʰi').replace('ʃ', 's').replace('ʅ', 'ɿ').replace('oŋ', 'ən')
                if in_list == 0:
                    res += (' ' + middle_i)
                    res_ipas += (' ' + middle_i)
                    in_list = 1
                else:
                    res += ('/' + middle_i)
                    res_ipas += ('/' + middle_i)
        in_list = 0
        for i in pinyins:
            if word == i[0]:
                middle_i = i[1].replace('zi', 'ji').replace('ci', 'qi').replace('si', 'xi').replace('jii', 'zii').replace('qii', 'cii').replace('xii', 'sii').replace('zh', 'z').replace('ch', 'c').replace('sh', 's').replace('ong', 'en')
                if in_list == 0:
                    res += (' ' + middle_i)
                    res_pinyins += (' ' + middle_i)
                    in_list = 1
                else:
                    res += ('/' + middle_i)
                    res_pinyins += ('/' + middle_i)
        #print(res, end=' ')

    print('\n'+res_ipas+'\n'+res_pinyins+'\n')