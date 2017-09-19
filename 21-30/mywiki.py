import codecs
import json

def extrac_text_from_title(title):
    for row in codecs.open("jawiki-country.json", "r", "utf-8"):
        article = json.loads(row)
        if article["title"] == title:
            return article["text"]
    return ""