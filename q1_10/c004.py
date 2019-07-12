# -*- coding: utf-8 -*-

'''
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
'''
class c004:
    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        s = s.replace('.', "")
        s = s.replace(',', "")
        s = s.split()

        list1 = []

        for word in s:
            list1.append(len(word))

        print(list1)
