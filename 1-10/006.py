#-*- coding: utf-8 -*-
def ngram(input, n):
    last = len(input) -n + 1
    ret = []
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret

if __name__ == "__main__":
    original = "I am an NLPer"
    char_bigram = ngram(original, 2)
    print char_bigram
    original = original.split()
    word_bigram = ngram(original, 2)
    print word_bigram
