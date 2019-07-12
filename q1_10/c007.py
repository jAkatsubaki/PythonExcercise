#-*- coding: utf-8 -*-

'''
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''
class c007:
    def ngram(self, input, n):
        last = len(input) -n + 1
        ret = []
        for i in range(0, last):
            ret.append(input[i:i+n])
        return ret

    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        str1 = "paraparaparadise"
        str2 = "paragraph"

        X = set(self.ngram(str1, 2))
        Y = set(self.ngram(str2, 2))

        print(X.union(Y))
        print(X.intersection(Y))
        print(X.difference(Y))
        print("se" in X)
        print("se" in Y)
