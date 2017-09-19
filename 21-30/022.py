import mywiki

def main():
    lines = mywiki.extrac_text_from_title(u'イギリス').split('\n')
    for text in lines:
        if 'Category' in text:
            print(text)

if __name__=='__main__':
    main()