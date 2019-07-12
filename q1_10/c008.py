#-*- coding: utf-8 -*-

'''
07. テンプレートによる文生成
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
'''
class c008:
    def sentence_generater(self,x,y,z):
        str1 = str(x) + u"時の" + str(y) + u"は" + str(z)
        print(str1)

    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        x=12
        y=u"気温"
        z=22.4
        self.sentence_generater(x, y, z)
