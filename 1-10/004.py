# -*- coding: utf-8 -*-


class c004:
    def solver(self):
        s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        s = s.replace('.', "")
        s = s.replace(',', "")
        s = s.split()

        list = []

        for word in s:
            list.append(len(word))

        print(list)
