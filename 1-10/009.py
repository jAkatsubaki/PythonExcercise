#-*- coding: utf-8 -*-
def cipher(input):
    ret = ""
    for char in input:
        ret += chr(219-ord(char)) if char.islower() else char
    return ret

if __name__ == "__main__":
    str = "Tohoku University is greate association"
    str = cipher(str)
    print(str)
    str = cipher(str)
    print(str)
