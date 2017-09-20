import mywiki
import re

def removeInnerLinkMarkup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    return str

def main():
    lines = mywiki.extrac_text_from_title(u'イギリス').split('\n')
    var_dict = {}
    for text in lines:
        line = re.search("^\|(.*?)\s=\s(.*)", text)
        if line is not None:
            var_dict[line.group(1)] = removeInnerLinkMarkup(line.group(2))     
    for k,v in sorted(var_dict.items(), key=lambda x: x[0]):
        print(k,v)

if __name__=='__main__':
    main()
