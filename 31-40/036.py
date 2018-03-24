import MeCab
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import ngram
import sys
import io


def tabbed_str_to_dict(tabbed_str: str) -> dict:
    elements = tabbed_str.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1], 'pos': elements[2], 'pos1': elements[3]}


def morphemes_to_sentence(morphemes: list) -> list:
    sentences = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []

    return sentences

def get_frequency(words: list) -> dict:
    """
    単語のリストを受け取って、単語をキーとして、頻度をバリューとする辞書を返す.
    :param words 単語のリスト
    :return dict 単語をキーとして、頻度をバリューとする辞書
    """
    frequency = {}
    for word in words:
        if frequency.get(word):
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def main():
    with open('neko.txt.mecab', encoding='utf-8') as file_wrapper:
        morphemes = [tabbed_str_to_dict(line) for line in file_wrapper]

    sentences = morphemes_to_sentence(morphemes)

    # describe your code below
    # 36. 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
    frequency = get_frequency([morpheme['surface'] for morpheme in morphemes])
    frequency = [(k, v) for k, v in sorted(frequency.items(), key=lambda x: x[1], reverse=True)]

    fig = plt.figure(figsize=(20, 6))

    # 37. 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
    words = [f[0] for f in frequency[0:10]]
    x_pos = np.arange(len(words))
    fp = FontProperties(fname='C:\Windows\Fonts\ipaexg.ttf', size=14)

    ax1 = fig.add_subplot(131)
    ax1.bar(x_pos, [f[1] for f in frequency[0:10]], align='center', alpha=0.4)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(words, fontproperties=fp)
    ax1.set_ylabel('Frequency')
    ax1.set_title('Top 10 frequent words')

    # 38. 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
    freq = list(dict(frequency).values())
    freq.sort(reverse=True)

    ax2 = fig.add_subplot(132)
    ax2.hist(freq, bins=50, range=(0, 50))
    ax2.set_title('Histogram of word count')
    ax2.set_xlabel('Word count')
    ax2.set_ylabel('Frequency')

    # 39. 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
    rank = list(range(1, len(freq) + 1))

    ax3 = fig.add_subplot(133)
    ax3.plot(freq, rank)
    ax3.set_xlabel('Rank')
    ax3.set_ylabel('Frequency')
    ax3.set_title('Zipf low')
    ax3.set_xscale('log')
    ax3.set_yscale('log')

    fig.savefig('morphological_analysis.png')


if __name__=='__main__':
    main()