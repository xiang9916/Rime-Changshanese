import json

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
    elif ipa.startswith('ɸ'): consonant = 'f'
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
    elif ipa.startswith('tɕ'): consonant = 'j'
    elif ipa.startswith('tɕʰ'): consonant = 'q'
    elif ipa.startswith('ɕ'): consonant = 'x'
        # 来日
    elif ipa.startswith('l'): consonant = 'l'
    elif ipa.startswith('z'): consonant = 'r'
    elif ipa in [
        'i', 'u', 'y',
        'ɑ', 'iɑ', 'uɑ', 'yɑ',
        'ɘ', 'ie', 'ye',
        'o', 'io',
        'ai', 'uai', 'uɘi', 'yɘi',
        'au', 'əu', 'iau', 'iəu',
        'iã', 'uã',
        'iẽ', 'yẽ',
        'on',
        'iȵ̍', 'uəȵ̍', 'yȵ̍',
        'iaŋ', 'uaŋ', 'oŋ', 'ioŋ'
    ]: consonant = ''
    else: error = 1

    # 韵母
    if ipa.endswith('ɿ'): vowel = 'ii'
    elif ipa.endswith('i') and not(ipa.endswith('ai') or ipa.endswith('ɘi')): vowel = 'i'
    elif ipa.endswith('u') and not(ipa.endswith('au') or ipa.endswith('əu')): vowel = 'u'
    elif ipa.endswith('y'): vowel = 'yu'
    elif ipa.endswith('ɑ') and not(ipa.endswith('iɑ') or ipa.endswith('uɑ') or ipa.endswith('yɑ')): vowel = 'a'
    elif ipa.endswith('iɑ'): vowel = 'ia'
    elif ipa.endswith('uɑ'): vowel = 'ua'
    elif ipa.endswith('yɑ'): vowel = 'yua'
    elif ipa.endswith('o') and not(ipa.endswith('io')): vowel = 'o'
    elif ipa.endswith('io'): vowel = 'io'
    elif ipa.endswith('ɘ') and not(ipa.endswith('iɘ')): vowel = 'e'
    elif ipa.endswith('ie'): vowel = 'ie'
    elif ipa.endswith('ye'): vowel = 'yue'

    elif ipa.endswith('ai') and not(ipa.endswith('uai') or ipa.endswith('yai')): vowel = 'ai'
    elif ipa.endswith('uai'): vowel = 'uai'
    elif ipa.endswith('yai'): vowel = 'yuai'
    elif ipa.endswith('ɘi') and not(ipa.endswith('uɘi') or ipa.endswith('yɘi')): vowel = 'ei'
    elif ipa.endswith('uɘi'): vowel = 'uei'
    elif ipa.endswith('yɘi'): vowel = 'yuei'
    elif ipa.endswith('au') and not(ipa.endswith('iau')): vowel = 'ao'
    elif ipa.endswith('iau'): vowel = 'iao'
    elif ipa.endswith('əu') and not(ipa.endswith('iəu')): vowel = 'ou'
    elif ipa.endswith('iəu'): vowel = 'iou'

    elif ipa.endswith('ã') and not(ipa.endswith('iã') or ipa.endswith('uã') or ipa.endswith('yã')): vowel = 'ann'
    elif ipa.endswith('iã'): vowel = 'iann'
    elif ipa.endswith('uã'): vowel = 'uann'
    elif ipa.endswith('yã'): vowel = 'yuann'
    elif ipa.endswith('ẽ') and not(ipa.endswith('iẽ') or ipa.endswith('yẽ')): vowel = 'enn'
    elif ipa.endswith('iẽ'): vowel = 'ienn'
    elif ipa.endswith('yẽ'): vowel = 'yuenn'
    elif ipa.endswith('on'): vowel = 'onn'

    elif ipa.endswith('əȵ̍') and not(ipa.endswith('uəȵ̍')): vowel = 'en'
    elif ipa.endswith('uəȵ̍'): vowel = 'uen'
    elif ipa.endswith('iȵ̍'): vowel = 'in'
    elif ipa.endswith('yȵ̍'): vowel = 'yn'

    elif ipa.endswith('aŋ') and not(ipa.endswith('iaŋ') or ipa.endswith('uaŋ') or ipa.endswith('yaŋ')): vowel = 'ang'
    elif ipa.endswith('iaŋ'): vowel = 'iang'
    elif ipa.endswith('uaŋ'): vowel = 'uang'
    elif ipa.endswith('yaŋ'): vowel = 'yuang'
    elif ipa.endswith('oŋ') and not(ipa.endswith('ioŋ')): vowel = 'ong'
    elif ipa.endswith('ioŋ'): vowel = 'iong'
    else: error = 1

    syllable = consonant + vowel
    if syllable.startswith('zh') or syllable.startswith('ch') or syllable.startswith('sh'):
        syllable = syllable.replace('zh', 'z').replace('ch', 'c').replace('sh', 's')
    # if syllable.startswith('zii') or syllable.startswith('cii') or syllable.startswith('sii'):
    #     pass
    # elif syllable.startswith('zi') or syllable.startswith('ci') or syllable.startswith('si'):
    #     syllable = syllable.replace('zi', 'ji').replace('ci', 'qi').replace('si', 'xi')
    if syllable.endswith('ang') or syllable.endswith('ong'):
        syllable = syllable.replace('ang', 'ann').replace('ong', 'en')
    if syllable == 'ien':
        syllable = 'in'
    if error == 1:
        raise "ERROR: {} don't has a difined pinyin".format(ipa)
    else:
        return syllable


with open('raw/湘音检字.json') as f:
    xiangyinjianzi = json.load(f)
    res = []
    for r in xiangyinjianzi:
        print((r[3], ipa_pinyin(r[1])))
        if r[3] != '':
            res.append((r[3], ipa_pinyin(r[1])))
    with open('data/湘音检字.json', 'w+', encoding='utf-8') as wf:
        json.dump(res, wf, ensure_ascii=False)
