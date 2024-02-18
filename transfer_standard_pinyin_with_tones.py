import json
import os
import re

def ipa_pinyin(ipa):
    error = 0
    consonant = '0'
    vowel = '0'
    if ipa == 'm̩': return 'm'
    if ipa == 'n̩': return 'n'
    # 声母
        # 帮
    if ipa.startswith('p') and not(ipa.startswith('pʰ')): consonant = 'b'
    elif ipa.startswith('pʰ'): consonant = 'p'
    elif ipa.startswith('m'): consonant = 'm'
    elif ipa.startswith('ɸ') or ipa.startswith('f'): consonant = 'f'
    elif ipa.startswith('v'): consonant = 'v'
        # 端
    elif ipa.startswith('t') and not(ipa.startswith('tʰ') or ipa.startswith('ts') or ipa.startswith('tʃ') or ipa.startswith('tɕ')): consonant = 'd'
    elif ipa.startswith('tʰ'): consonant = 't'
    elif ipa.startswith('ȵ') or ipa.startswith('n'): consonant = 'n'
        # 知二庄精
    elif ipa.startswith('ts') and not(ipa.startswith('tsʰ')): consonant = 'z'
    elif ipa.startswith('tsʰ'): consonant = 'c'
    elif ipa.startswith('s'): consonant = 's'
        # 知三章
    elif ipa.startswith('tʃ') and not(ipa.startswith('tʃʰ')): consonant = 'zh'
    elif ipa.startswith('tʃʰ'): consonant = 'ch'
    elif ipa.startswith('ʃ'): consonant = 'sh'
        # 见
    elif ipa.startswith('k') and not(ipa.startswith('kʰ')): consonant = 'g'
    elif ipa.startswith('kʰ'): consonant = 'k'
    elif ipa.startswith('ŋ'): consonant = 'ng'
    elif ipa.startswith('x'): consonant = 'h'
        # jqx
    elif ipa.startswith('tɕ') and not(ipa.startswith('tɕʰ')): consonant = 'j'
    elif ipa.startswith('tɕʰ'): consonant = 'q'
    elif ipa.startswith('ɕ'): consonant = 'x'
        # 来日
    elif ipa.startswith('l'): consonant = 'l'
    elif ipa.startswith('z') or ipa.startswith('ɹ̠'): consonant = 'r'
    elif ipa[:-1] in [
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

        'ɘi', 'ei',
        'uei',
        'yei',

        'au', 'əu',
        'iau', 'iɐɔ', 'iɑʊ',

        'iəu', 'iɵʊ',

        'iã', 'iaŋ', 'iɑŋ',
        'uã', 'uan', 'uaŋ', 'uɑŋ',
        'iẽ', 'iɛn',
        'yẽ', 'yɛn',
        'õ', 'ɔn', 'on',
        'in', 'iŋ', 'uən', 'uəȵ̍', 'yn', 'yȵ̍',
        'iaŋ', 'iɑŋ',
        'oŋ',
        'ioŋ',
        'əŋ',
        'iəŋ'
    ]: consonant = ''
    else: error = 1

    # 韵母
    if ipa[:-1].endswith('ɿ') and not(ipa[:-1].endswith('ɿ˗')):      vowel = 'ii'
    elif ipa[:-1].endswith('ʅ') or ipa[:-1].endswith('ɿ˗'):   vowel = 'ii'
    elif ipa[:-1].endswith('i')     and not(ipa[:-1].endswith('ai') or ipa[:-1].endswith('ei')): vowel = 'i'
    elif ipa[:-1].endswith('u')     and not(ipa[:-1].endswith('au') or ipa[:-1].endswith('əu')): vowel = 'u'
    elif ipa[:-1].endswith('y'):    vowel = 'yu'
    elif (ipa[:-1].endswith('a') or ipa[:-1].endswith('ɑ')) and not(ipa[:-1].endswith('ia') or ipa[:-1].endswith('iɑ') or ipa[:-1].endswith('ua') or ipa[:-1].endswith('uɑ') or ipa[:-1].endswith('ya') or ipa[:-1].endswith('yɑ')): vowel = 'a'
    elif ipa[:-1].endswith('ia') or ipa[:-1].endswith('iɑ'):   vowel = 'ia'
    elif ipa[:-1].endswith('ua') or ipa[:-1].endswith('uɑ'):   vowel = 'ua'
    elif ipa[:-1].endswith('ya') or ipa[:-1].endswith('yɑ'):   vowel = 'yua'
    elif ipa[:-1].endswith('o')     and not(ipa[:-1].endswith('io')): vowel = 'o'
    elif ipa[:-1].endswith('io'):   vowel = 'io'
    elif ipa[:-1].endswith('ə') or ipa[:-1].endswith('ɘ') and not(ipa[:-1].endswith('uə') or ipa[:-1].endswith('uɘ')): vowel = 'e'
    elif ipa[:-1].endswith('ie'):   vowel = 'ie'
    elif ipa[:-1].endswith('uə') or ipa[:-1].endswith('uɘ'): vowel = 'ue'    
    elif ipa[:-1].endswith('ye'):   vowel = 'yue'

    elif (ipa[:-1].endswith('ai') or ipa[:-1].endswith('aɪ') or ipa[:-1].endswith('ɐɛ')) and not(ipa[:-1].endswith('uai') or ipa[:-1].endswith('uaɪ') or ipa[:-1].endswith('uɐɛ') or ipa[:-1].endswith('yai') or ipa[:-1].endswith('yaɪ') or ipa[:-1].endswith('yɐɛ')): vowel = 'ai'
    elif ipa[:-1].endswith('uai') or ipa[:-1].endswith('uaɪ') or ipa[:-1].endswith('uɐɛ'):  vowel = 'uai'
    elif ipa[:-1].endswith('yai') or ipa[:-1].endswith('yaɪ') or ipa[:-1].endswith('yɐɛ'):  vowel = 'yuai'
    elif ipa[:-1].endswith('ei') and not(ipa[:-1].endswith('uei') or ipa[:-1].endswith('yei')): vowel = 'ei'
    elif ipa[:-1].endswith('uei'): vowel = 'uei'
    elif ipa[:-1].endswith('yei'): vowel = 'yuei'
    elif (ipa[:-1].endswith('au') or ipa[:-1].endswith('ɐɔ') or ipa[:-1].endswith('ɑʊ')) and not(ipa[:-1].endswith('iau') or ipa[:-1].endswith('iɐɔ') or ipa[:-1].endswith('iɑʊ')): vowel = 'ao'
    elif ipa[:-1].endswith('iau') or ipa[:-1].endswith('iɐɔ') or ipa[:-1].endswith('iɑʊ'): vowel = 'iao'
    elif (ipa[:-1].endswith('əu') or ipa[:-1].endswith('ɵʊ')) and not(ipa[:-1].endswith('iəu') or ipa[:-1].endswith('iɵʊ')): vowel = 'ou'
    elif ipa[:-1].endswith('iəu') or ipa[:-1].endswith('iɵʊ'): vowel = 'iou'

    elif (ipa[:-1].endswith('ã') or ipa[:-1].endswith('aŋ'))     and not(ipa[:-1].endswith('iã') or ipa[:-1].endswith('iaŋ') or ipa[:-1].endswith('uã') or ipa[:-1].endswith('uan') or ipa[:-1].endswith('uaŋ') or ipa[:-1].endswith('yã') or ipa[:-1].endswith('yan') or ipa[:-1].endswith('yaŋ')): vowel = 'ann'
    elif ipa[:-1].endswith('iã') or ipa[:-1].endswith('iaŋ'):   vowel = 'iann'
    elif ipa[:-1].endswith('uã') or ipa[:-1].endswith('uaŋ'):   vowel = 'uann'
    elif ipa[:-1].endswith('yã') or ipa[:-1].endswith('yaŋ'):   vowel = 'yuann'
    elif (ipa[:-1].endswith('ə̃') or ipa[:-1].endswith('ɛn')) and not(ipa[:-1].endswith('iẽ') or ipa[:-1].endswith('iɛn') or ipa[:-1].endswith('yẽ') or ipa[:-1].endswith('yɛn')): vowel = 'enn'
    elif ipa[:-1].endswith('iẽ') or ipa[:-1].endswith('iɛn'):   vowel = 'ienn'
    elif ipa[:-1].endswith('yẽ') or ipa[:-1].endswith('yɛn'):   vowel = 'yuenn'
    elif ipa[:-1].endswith('õ') or ipa[:-1].endswith('ɔn') or ipa[:-1].endswith('on'): vowel = 'onn'

    elif ipa[:-1].endswith('ən') and not(ipa[:-1].endswith('uən')): vowel = 'en'
    elif ipa[:-1].endswith('uən') or ipa[:-1].endswith('uəŋ'):  vowel = 'uen'
    elif ipa[:-1].endswith('in'):   vowel = 'in'
    elif ipa[:-1].endswith('yn'):   vowel = 'yun'

    elif ipa[:-1].endswith('əŋ') and not(ipa[:-1].endswith('iəŋ')): vowel = 'ong'
    elif ipa[:-1].endswith('iəŋ'):  vowel = 'iong'
    elif ipa[:-1] in [
            'm̩', 'n̩'
    ]: vowel = ''
    else: error = 1

    if int(ipa[-1]) < 4:
        tone = int(ipa[-1])
    else:
        tone = int(ipa[-1]) -1
    syllable = consonant + vowel + str(tone)
    # if syllable.startswith('zh') or syllable.startswith('ch') or syllable.startswith('sh'):
    #     syllable = syllable.replace('zh', 'z').replace('ch', 'c').replace('sh', 's')
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

with open('standard_tones/total.json', encoding='utf-8') as f:
    lst = json.load(f)
for i in range(len(lst)):
    if lst[i][0] == '行': print(lst[i][1])
    lst[i][1] = ipa_pinyin(lst[i][1])
    if lst[i][0] == '行': print(lst[i][1])
    # print(lst[i])
with open('standard_tones/pinyin.json', 'w+', encoding='utf-8') as wf:
    json.dump(lst, wf, ensure_ascii=False)