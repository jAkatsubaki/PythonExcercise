import xml.etree.ElementTree as et

def main():
    root = et.parse('nlp.txt.xml')

    for token in root.iterfind('./document/sentences/sentence/tokens/token[NER="PERSON"]'):
        print(token.findtext('word'))

if __name__ == '__main__':
    main()