import nekoanalyzer
import MeCab
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


'''
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''
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
