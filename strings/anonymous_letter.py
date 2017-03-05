# coding: utf-8
# anonymous_letter.py
from collections import defaultdict


def anonymous_letter(letter_text, magazine_text):
    coll = defaultdict(int)
    for c in letter_text:
        coll[c] += 1

    for c in magazine_text:
        if c in coll:
            coll[c] -= 1
        if coll[c] == 0:
            del coll[c]
        if not coll:
            return True
    return len(coll) == 0


if __name__ == '__main__':
    letters = 'apple'
    magazine = 'asda adsef faepbdsaf faafaf flasafd pen'
    ret = anonymous_letter(letters, magazine)
    assert ret

