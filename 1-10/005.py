#-*- coding: utf-8 -*-
from operator import itemgetter


class c005:
    def solver(self):
        str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        str1 = str1.split()

        dictionary = {}
        num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

        for elem in str1:
            if str.index(elem)+1 in num:
                dictionary[elem[:1]] = str.index(elem)+1
            else:
                dictionary[elem[:2]] = str.index(elem)+1

        for k, v in sorted(dictionary.items(), key=itemgetter(1)):
            print("{0],{1}".format(k, v))

#for k, v in sorted(dictionary.items(), key=lamda x:x[1]):
#    print k,v
