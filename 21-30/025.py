import mywiki
import re

def main():
    lines = mywiki.extrac_text_from_title(u'イギリス').split('\n')
    for text in lines:
        media_file = re.search('(File|ファイル):(.*?)\|', text)
        if media_file is not None:
            print(media_file.group(2))

if __name__=='__main__':
    main()
