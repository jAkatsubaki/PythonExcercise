#-*- coding: utf-8 -*-
def ngram(input, n):
    last = len(input) -n + 1
    ret = []
    for i in range(0, last):
        ret.append(input[i:i+n])
    return ret

if __name__ == "__main__":
    str1 = "paraparaparadise"
    str2 = "paragraph"

    X = set(ngram(str1, 2))
    Y = set(ngram(str2, 2))

    print X.union(Y)
    print X.intersection(Y)
    print X.difference(Y)

    print "se" in X
    print "se" in Y
