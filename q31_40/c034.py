import nekoanalyzer
import MeCab
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import io, sys

def convertTabbedString2Dictionary(tabstr) -> dict:
    ele = tabstr.split()
    if 0 < len(ele) < 4:
        return {'surface': ele[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': ele[0], 'base': ele[1], 'pos': ele[2], 'pos1': ele[3]}


def morphemes2sentence(morps) -> list:
    sentences = []
    sentence = []

    for morp in morps:
        sentence.append(morp)
        if morp['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []

    return sentences

def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,
                                encoding=sys.stdout.encoding, 
                                errors='backslashreplace', 
                                line_buffering=sys.stdout.line_buffering)

    with open('neko.txt.mecab', encoding='utf-8') as f:
        morphems = [convertTabbedString2Dictionary(line) for line in f]

    verbSurface = []
    for m in morphems:
        if '名詞' in m['pos1'] and 'サ変接続' in m['pos1']:
            verbSurface.append(m['surface'])

    print(verbSurface)

if __name__=='__main__':
    main()
