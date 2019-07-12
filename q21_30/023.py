import re
import mywiki

def main():
    lines = mywiki.extrac_text_from_title(u'イギリス').split('\n')
    for text in lines:
        category_in_line = re.search('^\[\[Category:(.*?)(|\|.*)\]\]$', text)
        if category_in_line is not None:
            print(category_in_line.group(1))

if __name__=='__main__':
    main()