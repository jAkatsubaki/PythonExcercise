#-*- coding: utf-8 -*-
str1 = u'パトカー'
str2 = u'タクシー'
str = u''

for x,y in zip(str1,str2):
    str = str + x + y

print(str)