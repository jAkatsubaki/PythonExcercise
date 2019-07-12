#-*- coding: utf-8 -*-

'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''
class c003:
    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        str1 = u'パトカー'
        str2 = u'タクシー'
        str3 = u''

        for x, y in zip(str1, str2):
            str3 = str3 + x + y

        print(str3)
