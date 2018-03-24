#-*- coding: utf-8 -*-


class c003:
    def solver(self):
        str1 = u'パトカー'
        str2 = u'タクシー'
        str3 = u''

        for x, y in zip(str1, str2):
            str3 = str3 + x + y

        print(str3)
