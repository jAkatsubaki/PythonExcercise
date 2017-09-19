
import mywiki
import re

def main():
    lines = re.split(r'\n[\|}]', mywiki.extrac_text_from_title(u'イギリス'))
    var_dict = {}
    for text in lines:
        line = re.search("^(.*?)\s=\s(.*)", text, re.S)
        if line is not None:
            var_dict[line.group(1)] = line.group(2)
    for k,v in sorted(var_dict.items(), key=lambda x: x[1]):
        print(k,v)

if __name__=='__main__':
    main()
