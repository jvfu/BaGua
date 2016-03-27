#coding:utf-8
import os

def docs_dir():
    return os.path.split(__file__)

def get_info(index):
    """
    type index: Int     64卦序号(1..64)
    rtype:      List    readlines
    """
    path = docs_dir()[0]
    name = "{path}/info/{index}".format(path=path, index=index)
    try:
        f = open(name)
        lines = f.readlines()
        f.close()
        return lines
    except Exception, e:
        return None

