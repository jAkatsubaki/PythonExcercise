import re
from stemming.porter2 import stem


def getBlockSeparatedIntoSentence():
    inputfile = open('nlp.txt', 'r', encoding='utf-8')
    for line in inputfile:
        ret = re.sub(r"(?P<group1>[\.|;|:|\?|!])(\s+)(?P<group3>[A-Z])", r"\1\2\n\3", line)
        ret = ret.split('\n')
        yield ret


def getEachWordInOneLineFromSentence():
    for line in getBlockSeparatedIntoSentence():
        for sentence in line:
            if sentence == '':
                continue
            else:
                word = sentence.split(' ')
                for w in word:
                    if w != '':
                        # print(w.rstrip('.,;:?!'))
                        yield w.rstrip('.,;:?!')
                print('\n', end='')


def main():
    for w in getEachWordInOneLineFromSentence():
        print(w + '\t' + stem(w))


if __name__=='__main__':
    main()