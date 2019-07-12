# -*- coding: utf-8 -*-
import random


'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
'''
class c010:
    def word_typoglycemia(self, word):
        if len(word) <= 4:
            return word

        mid_list = list(word[1:-1])
        while mid_list == list(word[1:-1]):
            random.shuffle(mid_list)
        return word[0] + "".join(mid_list) + word[-1]

    def str_typoglycemia(self, str):
        shuffled_list = []
        for word in str.split():
            shuffled_list.append(self.word_typoglycemia(word))
        return " ".join(shuffled_list)

    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        print(self.str_typoglycemia(str1))
