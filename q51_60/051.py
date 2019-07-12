import re


def main():
    inputfile = open('nlp.txt', 'r', encoding='utf-8')
    for line in inputfile:
        # print(line)
        print(re.sub(r"(?P<group1>[\.|;|:|\?|!])(\s+)(?P<group3>[A-Z])", r"\1\2\n\3", line))        


if __name__=='__main__':
    main()