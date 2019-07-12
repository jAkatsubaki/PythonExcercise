import mywiki
import re
import requests

def json_search(json_data):
    ret = {}
    for k,v in json_data.items():
        if isinstance(v, list):
            for element in v:
                ret.update(json_search(element))
        elif isinstance(v, dict):
            ret.update(json_search(v))
        else:
            ret[k] = v
    return ret

def removeInnerLinkMarkup(str):
    str = re.sub(r"'{2,5}", r"", str)
    str = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    str = re.sub(r"\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", str)
    str = re.sub(r"<.*?>", r"", str)
    str = re.sub(r"\[.*?\]", r"", str)
    return str

def main():
    lines = mywiki.extrac_text_from_title(u'イギリス').split('\n')
    var_dict = {}
    for text in lines:
        line = re.search("^\|(.*?)\s=\s(.*)", text)
        if line is not None:
            var_dict[line.group(1)] = removeInnerLinkMarkup(line.group(2))

    url = "https://en.wikipedia.org/w/api.php"
    payload = {"action" : "query",
               "titles" : "File:{}".format(var_dict[u'国旗画像']),
               "prop" : "imageinfo",
               "format" : "json",
               "iiprop" : "url"}
    json_data = requests.get(url, params=payload).json()
    print(json_search(json_data)["url"])

if __name__=='__main__':
    main()
