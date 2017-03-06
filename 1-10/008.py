#-*- coding: utf-8 -*-
def sentence_generater(x,y,z):
    str = unicode(x) + u"時の" + unicode(y) + u"は" + unicode(z)
    print str

if __name__ == "__main__":
    x=12
    y=u"気温"
    z=22.4
    sentence_generater(x, y, z)
