import json
import os
import re

def ipa_pinyin(ipa):
    error = 0
    consonant = '0'
    vowel = '0'
    if ipa == 'm̩': return 'm̩'
    if ipa == 'n̩': return 'n̩'
    # 声母
        # 帮
    if ipa.startswith('p') and not(ipa.startswith('pʰ')): consonant = 'p'
    elif ipa.startswith('pʰ'): consonant = 'pʰ'
    elif ipa.startswith('m'): consonant = 'm'
    elif ipa.startswith('ɸ') or ipa.startswith('f'): consonant = 'ɸ'
    elif ipa.startswith('v'): consonant = 'v'
        # 端
    elif ipa.startswith('t') and not(ipa.startswith('tʰ') or ipa.startswith('ts') or ipa.startswith('tʃ') or ipa.startswith('tɕ')): consonant = 't'
    elif ipa.startswith('tʰ'): consonant = 'tʰ'
    elif ipa.startswith('ȵ'): consonant = 'ȵ'
        # 知二庄精
    elif ipa.startswith('ts') and not(ipa.startswith('tsʰ')): consonant = 'ts'
    elif ipa.startswith('tsʰ'): consonant = 'tsʰ'
    elif ipa.startswith('s'): consonant = 's'
        # 知三章
    elif ipa.startswith('tʃ') and not(ipa.startswith('tʃʰ')): consonant = 'tʃ'
    elif ipa.startswith('tʃʰ'): consonant = 'tʃʰ'
    elif ipa.startswith('ʃ'): consonant = 'ʃ'
        # 见
    elif ipa.startswith('k') and not(ipa.startswith('kʰ')): consonant = 'k'
    elif ipa.startswith('kʰ'): consonant = 'kʰ'
    elif ipa.startswith('ŋ'): consonant = 'ŋ'
    elif ipa.startswith('x'): consonant = 'x'
        # jqx
    elif ipa.startswith('tɕ') and not(ipa.startswith('tɕʰ')): consonant = 'tɕ'
    elif ipa.startswith('tɕʰ'): consonant = 'tɕʰ'
    elif ipa.startswith('ɕ'): consonant = 'ɕ'
        # 来日
    elif ipa.startswith('l'): consonant = 'l'
    elif ipa.startswith('z') or ipa.startswith('ɹ̠'): consonant = 'z'
    elif ipa in [
        'i',
        'u',
        'y',

        'ɑ',
        'iɑ',
        'uɑ',
        'yɑ',

        'ə', 'ɘ',
        'ie',
        'ye',

        'o',
        'io',

        'ai', 'aɪ',
        'uai', 'uaɪ', 'uɐɛ',

        'ɘi', 'ɘɪ',
        'uɘi', 'uɘɪ',
        'yɘi', 'yɘɪ',

        'au', 'əu',
        'iau', 'iɐɔ', 'iɑʊ',

        'iəu', 'iɵʊ',

        'iã', 'iaŋ', 'iɑŋ',
        'uã', 'uan', 'uaŋ', 'uɑŋ',
        'iẽ', 'iɛn',
        'yẽ', 'yɛn',
        'õɹ̃', 'ɔn', 'on',
        'in', 'iȵ̍', 'uən', 'uəȵ̍', 'yn', 'yȵ̍',
        'iaŋ', 'iɑŋ',
        'oŋ',
        'ioŋ',
        'əŋ',
        'iəŋ'
    ]: consonant = ''
    else: error = 1

    # 韵母
    if ipa.endswith('ɿ') and not(ipa.endswith('ɿ˗')):      vowel = 'ɿ'
    elif ipa.endswith('ʅ') or ipa.endswith('ɿ˗'):   vowel = 'ʅ'
    elif ipa.endswith('i')     and not(ipa.endswith('ai') or ipa.endswith('ɘi')): vowel = 'i'
    elif ipa.endswith('u')     and not(ipa.endswith('au') or ipa.endswith('əu')): vowel = 'u'
    elif ipa.endswith('y'):    vowel = 'y'
    elif (ipa.endswith('a') or ipa.endswith('ɑ')) and not(ipa.endswith('ia') or ipa.endswith('iɑ') or ipa.endswith('ua') or ipa.endswith('uɑ') or ipa.endswith('ya') or ipa.endswith('yɑ')): vowel = 'ɑ'
    elif ipa.endswith('ia') or ipa.endswith('iɑ'):   vowel = 'iɑ'
    elif ipa.endswith('ua') or ipa.endswith('uɑ'):   vowel = 'uɑ'
    elif ipa.endswith('ya') or ipa.endswith('yɑ'):   vowel = 'yɑ'
    elif ipa.endswith('o')     and not(ipa.endswith('io')): vowel = 'o'
    elif ipa.endswith('io'):   vowel = 'io'
    elif ipa.endswith('ə') or ipa.endswith('ɘ') and not(ipa.endswith('uə') or ipa.endswith('uɘ')): vowel = 'ə'
    elif ipa.endswith('ie'):   vowel = 'ie'
    elif ipa.endswith('uə') or ipa.endswith('uɘ'): vowel = 'uə'    
    elif ipa.endswith('ye'):   vowel = 'ye'

    elif (ipa.endswith('ai') or ipa.endswith('aɪ') or ipa.endswith('ɐɛ')) and not(ipa.endswith('uai') or ipa.endswith('uaɪ') or ipa.endswith('uɐɛ') or ipa.endswith('yai') or ipa.endswith('yaɪ') or ipa.endswith('yɐɛ')): vowel = 'ai'
    elif ipa.endswith('uai') or ipa.endswith('uaɪ') or ipa.endswith('uɐɛ'):  vowel = 'uai'
    elif ipa.endswith('yai') or ipa.endswith('yaɪ') or ipa.endswith('yɐɛ'):  vowel = 'yai'
    elif (ipa.endswith('ɘi') or ipa.endswith('ɘɪ')) and not(ipa.endswith('uɘi') or ipa.endswith('uɘɪ') or ipa.endswith('uɘi') or ipa.endswith('yɘi') or ipa.endswith('yɘɪ') or ipa.endswith('yɘi')): vowel = 'ei'
    elif ipa.endswith('uɘi') or ipa.endswith('uɘɪ') or ipa.endswith('uɘi'): vowel = 'uei'
    elif ipa.endswith('yɘi') or ipa.endswith('yɘɪ') or ipa.endswith('yɘi'): vowel = 'yei'
    elif (ipa.endswith('au') or ipa.endswith('ɐɔ') or ipa.endswith('ɑʊ')) and not(ipa.endswith('iau') or ipa.endswith('iɐɔ') or ipa.endswith('iɑʊ')): vowel = 'au'
    elif ipa.endswith('iau') or ipa.endswith('iɐɔ') or ipa.endswith('iɑʊ'): vowel = 'iau'
    elif (ipa.endswith('əu') or ipa.endswith('ɵʊ')) and not(ipa.endswith('iəu') or ipa.endswith('iɵʊ')): vowel = 'əu'
    elif ipa.endswith('iəu') or ipa.endswith('iɵʊ'): vowel = 'iəu'

    elif (ipa.endswith('ã') or ipa.endswith('an'))     and not(ipa.endswith('iã') or ipa.endswith('ian') or ipa.endswith('uã') or ipa.endswith('uan') or ipa.endswith('yã') or ipa.endswith('yan')): vowel = 'ã'
    elif ipa.endswith('iã') or ipa.endswith('ian'):   vowel = 'iã'
    elif ipa.endswith('uã') or ipa.endswith('uan'):   vowel = 'uã'
    elif ipa.endswith('yã') or ipa.endswith('yan'):   vowel = 'yã'
    elif (ipa.endswith('ɘ̃') or ipa.endswith('ɛn')) and not(ipa.endswith('iẽ') or ipa.endswith('iɛn') or ipa.endswith('yẽ') or ipa.endswith('yɛn')): vowel = 'ə̃'
    elif ipa.endswith('iẽ') or ipa.endswith('iɛn'):   vowel = 'iẽ'
    elif ipa.endswith('yẽ') or ipa.endswith('yɛn'):   vowel = 'yẽ'
    elif ipa.endswith('õɹ̃') or ipa.endswith('ɔn') or ipa.endswith('on'): vowel = 'õ'

    elif (ipa.endswith('ən') or ipa.endswith('əȵ̍')) and not(ipa.endswith('uən') or ipa.endswith('uəȵ̍')): vowel = 'ən'
    elif ipa.endswith('uən') or ipa.endswith('uəȵ̍'):  vowel = 'uən'
    elif ipa.endswith('in')  or ipa.endswith('iȵ̍'):   vowel = 'in'
    elif ipa.endswith('yn')  or ipa.endswith('yȵ̍'):   vowel = 'yn'

    elif (ipa.endswith('aŋ') or ipa.endswith('ɑŋ')) and not(ipa.endswith('iaŋ') or ipa.endswith('iɑŋ') or ipa.endswith('uaŋ') or ipa.endswith('uɑŋ') or ipa.endswith('yaŋ') or ipa.endswith('yɑŋ')): vowel = 'aŋ'
    elif ipa.endswith('iaŋ') or ipa.endswith('iɑŋ'):  vowel = 'iaŋ'
    elif ipa.endswith('uaŋ') or ipa.endswith('uɑŋ'):  vowel = 'uaŋ'
    elif ipa.endswith('yaŋ') or ipa.endswith('yɑŋ'):  vowel = 'yaŋ'
    elif ipa.endswith('oŋ')    and not(ipa.endswith('ioŋ')): vowel = 'oŋ'
    elif ipa.endswith('ioŋ'):  vowel = 'ioŋ'
    elif (ipa.endswith('əŋ'))  and not(ipa.endswith('iəŋ') or ipa.endswith('uəŋ') or ipa.endswith('yəŋ')): vowel = 'əŋ'
    elif ipa.endswith('iəŋ'):  vowel = 'iŋ'
    
    else: error = 1

    syllable = consonant + vowel
    if syllable.startswith('zh') or syllable.startswith('ch') or syllable.startswith('sh'):
        syllable = syllable.replace('zh', 'z').replace('ch', 'c').replace('sh', 's')
    # if syllable.startswith('zii') or syllable.startswith('cii') or syllable.startswith('sii'):
    #     pass
    # elif syllable.startswith('zi') or syllable.startswith('ci') or syllable.startswith('si'):
    #     syllable = syllable.replace('zi', 'ji').replace('ci', 'qi').replace('si', 'xi')
    # if syllable.endswith('ng'):
    #     syllable = syllable.replace('ang', 'ann').replace('ong', 'en').replace('eng', 'en').replace('ing','in')
    if syllable == 'ien':
        syllable = 'in'
    if error == 1:
        print("ERROR: {} don't has a difined pinyin {}, {}".format(ipa, consonant, vowel))
        # quit()
    else:
        return syllable

with open('raw/訓詁諧音.csv', encoding='utf-8') as f:
    import pandas as pd
    res = []
    xunguxieyin = pd.read_csv('raw/訓詁諧音.csv', header=None)
    for r in xunguxieyin.index:
        pinyin = ipa_pinyin(xunguxieyin.loc[r, 0].split('/')[-1])
        # print(xunguxieyin.loc[r, 2])
        for w in re.sub(u'\(.*?\)|\{.*?\}|\[.*?\]|.*?\/', '',xunguxieyin.loc[r, 2]):
            if not(w in '-=□'): res.append((w, pinyin))
    with open('standard/訓詁諧音.json', 'w+', encoding='utf-8') as wf:
        json.dump(res, wf, ensure_ascii=False)

with open('raw/湘音檢字.csv', encoding='utf-8') as f:
    import pandas as pd
    res = []
    xunguxieyin = pd.read_csv('raw/湘音檢字.csv', header=None)
    for r in xunguxieyin.index:
        pinyin = ipa_pinyin(xunguxieyin.loc[r, 0].split('/')[-1])
        # print(xunguxieyin.loc[r, 2])
        for w in re.sub(u'\(.*?\)|\{.*?\}|\[.*?\]', '',xunguxieyin.loc[r, 2]):
            if not(w in '-=□'): res.append((w, pinyin))
    with open('standard/湘音檢字.json', 'w+', encoding='utf-8') as wf:
        json.dump(res, wf, ensure_ascii=False)

with open('raw/長沙.csv', encoding='utf-8') as f:
    import pandas as pd
    res = []
    xunguxieyin = pd.read_csv('raw/長沙.csv', header=None)
    for r in xunguxieyin.index:
        pinyin = ipa_pinyin(xunguxieyin.loc[r, 0].split('/')[-1])
        # print(xunguxieyin.loc[r, 2])
        for w in re.sub(u'|\(.*?\)|\{.*?\}|\[.*?\]', '',xunguxieyin.loc[r, 2]):
            if not(w in '-=□'): res.append((w, pinyin))
    with open('standard/長沙.json', 'w+', encoding='utf-8') as wf:
        json.dump(res, wf, ensure_ascii=False)

# with open('raw/湘音检字.json', encoding='utf-8') as f:
#     xiangyinjianzi = json.load(f)
#     res = []
#     for r in xiangyinjianzi:
#         # print((r[3], ipa_pinyin(r[1])))
#         if r[3] != '':
#             res.append((r[3], ipa_pinyin(r[1])))
#     with open('standard/湘音检字.json', 'w+', encoding='utf-8') as wf:
#         json.dump(res, wf, ensure_ascii=False)

filelist = os.listdir('standard')
if '.DS_store' in filelist:
    del filelist['.DS_store']

total_dictionary_list = []
for filename in filelist:
    if filename == '.DS_Store':
        continue
    print(filename)
    with open('standard/{}'.format(filename), encoding='utf-8') as f:
        dictionary = json.load(f)
        total_dictionary_list.extend(dictionary)
total_dictionary = []
for r in total_dictionary_list:
    total_dictionary.append((r[0], r[1]))
total_dictionary = list({}.fromkeys(total_dictionary).keys())
with open('standard/total.json', 'w+', encoding='utf-8') as wf:
    json.dump(total_dictionary, wf, ensure_ascii=False)