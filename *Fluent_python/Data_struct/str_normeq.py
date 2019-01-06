#字符串和字节序列


from unicodedata import normalize

def nfc_equal(str1,str2):
    return normalize('NFC',str1) == normalize('NFC',str2)
def fold_equal(str1,str2):
    return normalize('NFC',str1).casefold() == \
    normalize('NFC',str2).casefold()

print(nfc_equal('a','A'))

print(fold_equal('a','A'))


# 去掉所有变音符号
def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD',txt)
    # 把所有字符分解成基字符和组合记号, 'NFC' 把所有字符变成最短字节
    shaved = ''.join(c for c in norm_txt
    if not unicodedata.combining(c))
    # 过滤掉所有组合记号
    return unicodedata.normalize('NFC',shaved)
    # 重组所有字符.

def shave_marks_latin(txt):
    '删除拉丁基字符中所有变音符号删除'
    norm_txt = unicodedata.normalize('NFD',txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
            #检测基字符是不是拉丁字符


        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)

    return unicodedata.normalize('NFC',shaved)
