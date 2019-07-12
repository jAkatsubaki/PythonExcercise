
'''
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
'''
class c001:
    def solver(self):
        print('[RUN ... ' + self.__class__.__name__ + ']')
        str1 = 'stressed'
        print(str1[-1::-1])