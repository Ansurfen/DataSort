import json
import re

from core import data


def getData():
    reg_map = {}
    with open(data.read_filename, 'r', encoding='utf-8') as fp:
        stream = fp.read()
        url = re.findall("(?<=A HREF=\").*(?=\" )", stream)
        title = re.findall("(?<= >).*(?=</A>)", stream)
        for i in range(0, len(url)):
            reg_map[url[i]] = title[i]
    return reg_map


def writeData(src):
    with open(data.write_filename, 'w', encoding='utf-8') as fp:
        json.dump(src, fp, ensure_ascii=False)
        fp.close()
