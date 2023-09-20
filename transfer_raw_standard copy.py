import re

with open('raw/訓詁諧音.csv', encoding='utf-8') as f:
    import pandas as pd
    res = []
    xunguxieyin = pd.read_csv('raw/訓詁諧音.csv', header=None)
    for r in xunguxieyin.index:
        r = r
    with open('standard/训诂谐音.json', 'w+', encoding='utf-8') as wf:
        json.dump(res, wf, ensure_ascii=False)

with open('raw/湘音檢字.csv', encoding='utf-8') as f:
    import pandas as pd
    res = []
    xunguxieyin = pd.read_csv('raw/湘音檢字.csv', header=None)
    for r in xunguxieyin.index:
        pinyin = ipa_pinyin(xunguxieyin.loc[r, 0])
        # print(xunguxieyin.loc[r, 2])
        for w in xunguxieyin.loc[r, 2]:
            res.append((w, pinyin))
    with open('standard/湘音檢字.json', 'w+', encoding='utf-8') as wf:
        json.dump(res, wf, ensure_ascii=False)

with open('raw/長沙.csv', encoding='utf-8') as f:
    import pandas as pd
    res = []
    xunguxieyin = pd.read_csv('raw/長沙.csv', header=None)
    for r in xunguxieyin.index:
        pinyin = ipa_pinyin(xunguxieyin.loc[r, 0])
        # print(xunguxieyin.loc[r, 2])
        for w in xunguxieyin.loc[r, 2]:
            res.append((w, pinyin))
    with open('standard/长沙.json', 'w+', encoding='utf-8') as wf:
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

