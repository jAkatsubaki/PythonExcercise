import codecs
import json

def main():
    for row in codecs.open("jawiki-country.json", "r", "utf-8"):
        article = json.loads(row)
        if article["title"] == 'イギリス':
            print(article["text"])

if __name__=='__main__':
    main()