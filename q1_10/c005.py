#-*- coding: utf-8 -*-
from operator import itemgetter

'''
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から
単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''
class c005:
    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        str1 = str1.split(' ')

        dictionary = {}
        num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

        for elem in str1:
            if str1.index(elem)+1 in num:
                dictionary[elem[:1]] = str1.index(elem)+1
            else:
                dictionary[elem[:2]] = str1.index(elem)+1

        for k, v in sorted(dictionary.items(), key=itemgetter(1)):
            print("{0},{1}".format(k, v))
