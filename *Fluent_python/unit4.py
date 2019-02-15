import unicodedata
import string



def shave_marks_latin(txt):
    norm_txt = unicodedata.normalize('NFD',txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        kepper.append(c)

        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaves = ''.join(keepers)
    return unicodedata.normalize('NFC',shaves)
