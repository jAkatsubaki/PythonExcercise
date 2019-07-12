#-*- coding: utf-8 -*-

'''
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
 ・英小文字ならば(219 - 文字コード)の文字に置換
 ・その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''
class c009:
    def cipher(self, input):
        ret = ""
        for char in input:
            ret += chr(219-ord(char)) if char.islower() else char
        return ret

    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        str1 = "Tohoku University is greate association"
        str1 = self.cipher(str1)
        print(str1)
        str1 = self.cipher(str1)
        print(str1)
