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


def ngramed_list(lst: list, n: int = 3) -> list:
    """
        This function create N-gram model
    """
    index = ngram.NGram(N=n)
    return [term for term in index.ngrams(lst)]


def isNounOfNoun(words: list) -> bool:
    """
        Evaluate whether a list consisted of three words is matched "NOUN of NOUN"
    """
    return (type(words) == list) and (len(words) == 3) and \
        (words[0]['pos'].find('名詞') == 0) and \
        (words[1]['face'] == 'の') and \
        (words[2]['pos1'].find('名詞') == 0)


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,
                                  encoding=sys.stdout.encoding,
                                  errors='backslashreplace',
                                  line_buffering=sys.stdout.line_buffering)

    with open('neko.txt.mecab', encoding='utf-8') as f:
        morphems = [tabbed_str_to_dict(line) for line in f]

    noun_no_noun = [ngrams for ngrams in ngramed_list(morphems)
                    if isNounOfNoun(ngrams)]
    noun_no_noun = [''.join([word['surface'] for word in ngr])
                    for ngr in noun_no_noun]
    print(noun_no_noun[::100])
