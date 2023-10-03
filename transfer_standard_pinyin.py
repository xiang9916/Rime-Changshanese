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
    elif ipa.startswith('ȵ'): consonant = 'n'
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

        'ɘi', 'ei',
        'uɘi', 'uei',
        'yɘi', 'yɘɪ',

        'au', 'əu',
        'iau', 'iɐɔ', 'iɑʊ',

        'iəu', 'iɵʊ',

        'iã', 'iaŋ', 'iɑŋ',
        'uã', 'uan', 'uaŋ', 'uɑŋ',
        'iẽ', 'iɛn',
        'yẽ', 'yɛn',
        'õ', 'ɔn', 'on',
        'in', 'iȵ̍', 'uən', 'uəȵ̍', 'yn', 'yȵ̍',
        'iaŋ', 'iɑŋ',
        'oŋ',
        'ioŋ',
        'əŋ',
        'iəŋ'
    ]: consonant = ''
    else: error = 1

    # 韵母
    if ipa.endswith('ɿ') and not(ipa.endswith('ɿ˗')):      vowel = 'ii'
    elif ipa.endswith('ʅ') or ipa.endswith('ɿ˗'):   vowel = 'ii'
    elif ipa.endswith('i')     and not(ipa.endswith('ai') or ipa.endswith('ɘi')): vowel = 'i'
    elif ipa.endswith('u')     and not(ipa.endswith('au') or ipa.endswith('əu')): vowel = 'u'
    elif ipa.endswith('y'):    vowel = 'yu'
    elif (ipa.endswith('a') or ipa.endswith('ɑ')) and not(ipa.endswith('ia') or ipa.endswith('iɑ') or ipa.endswith('ua') or ipa.endswith('uɑ') or ipa.endswith('ya') or ipa.endswith('yɑ')): vowel = 'a'
    elif ipa.endswith('ia') or ipa.endswith('iɑ'):   vowel = 'ia'
    elif ipa.endswith('ua') or ipa.endswith('uɑ'):   vowel = 'ua'
    elif ipa.endswith('ya') or ipa.endswith('yɑ'):   vowel = 'yua'
    elif ipa.endswith('o')     and not(ipa.endswith('io')): vowel = 'o'
    elif ipa.endswith('io'):   vowel = 'io'
    elif ipa.endswith('ə') or ipa.endswith('ɘ') and not(ipa.endswith('uə') or ipa.endswith('uɘ')): vowel = 'e'
    elif ipa.endswith('ie'):   vowel = 'ie'
    elif ipa.endswith('uə') or ipa.endswith('uɘ'): vowel = 'ue'    
    elif ipa.endswith('ye'):   vowel = 'yue'

    elif (ipa.endswith('ai') or ipa.endswith('aɪ') or ipa.endswith('ɐɛ')) and not(ipa.endswith('uai') or ipa.endswith('uaɪ') or ipa.endswith('uɐɛ') or ipa.endswith('yai') or ipa.endswith('yaɪ') or ipa.endswith('yɐɛ')): vowel = 'ai'
    elif ipa.endswith('uai') or ipa.endswith('uaɪ') or ipa.endswith('uɐɛ'):  vowel = 'uai'
    elif ipa.endswith('yai') or ipa.endswith('yaɪ') or ipa.endswith('yɐɛ'):  vowel = 'yuai'
    elif (ipa.endswith('ɘi') or ipa.endswith('ɘɪ')) and not(ipa.endswith('uɘi') or ipa.endswith('uɘɪ') or ipa.endswith('uɘi') or ipa.endswith('yɘi')): vowel = 'ei'
    elif ipa.endswith('uɘi') or ipa.endswith('uɘɪ'): vowel = 'uei'
    elif ipa.endswith('yɘi') or ipa.endswith('yɘɪ'): vowel = 'yuei'
    elif (ipa.endswith('au') or ipa.endswith('ɐɔ') or ipa.endswith('ɑʊ')) and not(ipa.endswith('iau') or ipa.endswith('iɐɔ') or ipa.endswith('iɑʊ')): vowel = 'au'
    elif ipa.endswith('iau') or ipa.endswith('iɐɔ') or ipa.endswith('iɑʊ'): vowel = 'iau'
    elif (ipa.endswith('əu') or ipa.endswith('ɵʊ')) and not(ipa.endswith('iəu') or ipa.endswith('iɵʊ')): vowel = 'ou'
    elif ipa.endswith('iəu') or ipa.endswith('iɵʊ'): vowel = 'iou'

    elif (ipa.endswith('ã') or ipa.endswith('an'))     and not(ipa.endswith('iã') or ipa.endswith('ian') or ipa.endswith('uã') or ipa.endswith('uan') or ipa.endswith('yã') or ipa.endswith('yan')): vowel = 'ann'
    elif ipa.endswith('iã') or ipa.endswith('ian'):   vowel = 'iann'
    elif ipa.endswith('uã') or ipa.endswith('uan'):   vowel = 'uann'
    elif ipa.endswith('yã') or ipa.endswith('yan'):   vowel = 'yuann'
    elif (ipa.endswith('ə̃') or ipa.endswith('ɛn')) and not(ipa.endswith('iẽ') or ipa.endswith('iɛn') or ipa.endswith('yẽ') or ipa.endswith('yɛn')): vowel = 'enn'
    elif ipa.endswith('iẽ') or ipa.endswith('iɛn'):   vowel = 'ienn'
    elif ipa.endswith('yẽ') or ipa.endswith('yɛn'):   vowel = 'yuenn'
    elif ipa.endswith('õ') or ipa.endswith('ɔn') or ipa.endswith('on'): vowel = 'onn'

    elif (ipa.endswith('ən') or ipa.endswith('əȵ̍')) and not(ipa.endswith('uən') or ipa.endswith('uəȵ̍')): vowel = 'en'
    elif ipa.endswith('uən') or ipa.endswith('uəȵ̍'):  vowel = 'uen'
    elif ipa.endswith('in')  or ipa.endswith('iȵ̍'):   vowel = 'in'
    elif ipa.endswith('yn')  or ipa.endswith('yȵ̍'):   vowel = 'yun'

    elif (ipa.endswith('aŋ') or ipa.endswith('ɑŋ')) and not(ipa.endswith('iaŋ') or ipa.endswith('iɑŋ') or ipa.endswith('uaŋ') or ipa.endswith('uɑŋ') or ipa.endswith('yaŋ') or ipa.endswith('yɑŋ')): vowel = 'aŋ'
    elif ipa.endswith('iaŋ') or ipa.endswith('iɑŋ'):  vowel = 'iang'
    elif ipa.endswith('uaŋ') or ipa.endswith('uɑŋ'):  vowel = 'uang'
    elif ipa.endswith('yaŋ') or ipa.endswith('yɑŋ'):  vowel = 'yuang'
    elif ipa.endswith('oŋ')    and not(ipa.endswith('ioŋ')): vowel = 'ong'
    elif ipa.endswith('ioŋ'):  vowel = 'iong'
    elif (ipa.endswith('əŋ'))  and not(ipa.endswith('iəŋ') or ipa.endswith('uəŋ') or ipa.endswith('yəŋ')): vowel = 'eng'
    elif ipa.endswith('iəŋ'):  vowel = 'ing'
    elif ipa in [
            'm', 'n'
    ]: vowel = ''
    else: error = 1

    syllable = consonant + vowel
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

with open('standard/total.json', encoding='utf-8') as f:
    lst = json.load(f)
for i in range(len(lst)):
    lst[i][1] = ipa_pinyin(lst[i][1])
    # print(lst[i])
with open('standard/pinyin.json', 'w+', encoding='utf-8') as wf:
    json.dump(lst, wf, ensure_ascii=False)