import nekoanalyzer
import MeCab
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def convertTabbedString2Dictionary(tabstr) -> dict:
    """
        This function create the dictionary by reading .mecab file
    """
    ele = tabstr.split()
    if 0 < len(ele) < 4:
        return {'suraface': ele[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'suraface': ele[0], 'base': ele[1], 'pos': ele[2], 'pos1': ele[3]}


def morphemes2sentence(morps) -> list:
    sentences = []
    sentence = []

    for morp in morps:
        sentence.append(morp)
        if morp['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []

    return sentences


with open('neko.txt.mecab', encoding='utf-8') as f:
    morphems = [convertTabbedString2Dictionary(line) for line in f]

sentences = morphemes2sentence(morphems)

outfile = open('031.output.dat', 'w', encoding='UTF-8')
outfile.write(str(morphems[::100]))
outfile.write(str(sentences[::100]))
