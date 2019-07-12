import mywiki
import re

def main():
    lines = mywiki.extrac_text_from_title(u'イギリス').split('\n')
    for text in lines:
        section_in_lines = re.search('^(=+)\s*(.*?)\s*(=+)$', text)
        if section_in_lines is not None:
            print(section_in_lines.group(2), len(section_in_lines.group(1)) - 1)

if __name__=='__main__':
    main()