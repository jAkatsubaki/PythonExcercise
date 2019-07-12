#-*- coding: utf-8 -*-

'''
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''
class c006:
    def ngram(self, input, n):
        last = len(input) -n + 1
        ret = []
        for i in range(0, last):
            ret.append(input[i:i+n])
        return ret

    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        original = "I am an NLPer"
        char_bigram = self.ngram(original, 2)
        print(char_bigram)
        original = original.split()
        word_bigram = self.ngram(original, 2)
        print(word_bigram)
