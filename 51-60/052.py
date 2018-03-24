import re


def getBlockSeparatedIntoSentence():
    inputfile = open('nlp.txt', 'r', encoding='utf-8')
    for line in inputfile:
        ret = re.sub(r"(?P<group1>[\.|;|:|\?|!])(\s+)(?P<group3>[A-Z])", r"\1\2\n\3", line)
        ret = ret.split('\n')
        yield ret


def main():
    for line in getBlockSeparatedIntoSentence():
        for sentence in line:
            if sentence == '':
                continue
            else:
                word = sentence.split(' ')
                for w in word:
                    if w != '':
                        print(w.rstrip('.,;:?!'))
                print('\n', end='')


if __name__=='__main__':
    main()
