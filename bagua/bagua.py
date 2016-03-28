#coding:utf-8
import random
import os
from utils import *

def docs_dir():
    return os.path.split(__file__)

def get_info(index):
    """
    type index: Int     64卦序号(1..64)
    rtype:      List    readlines
    """
    path = docs_dir()[0]
    name = "{path}/docs/{index}.txt".format(path=path, index=index)
    try:
        f = open(name)
        lines = f.readlines()
        f.close()
        return lines
    except Exception, e:
        return None
        
def shake_yao():
    return [random.randint(2, 3) for x in xrange(3)]

def shake_gua64():
    return [shake_yao() for x in xrange(6)]

def get_yao_info(index):
    def has_yao_index(line):
        for i, v in enumerate(YAO_INDEX):
            if v[YIN] in line: return i, YIN
            if v[YANG] in line: return i, YANG
                
        return -1, None

    original = ''
    rlist = [[0, original] for x in range(6)]
    lines = get_info(index)
    if lines is None: return rlist

    for line in lines:
        yao_index, yao_type = has_yao_index(line)
        if yao_index >= 0 and rlist[yao_index][1] is original:
            rlist[yao_index][0] = yao_type
            rlist[yao_index][1] = line

    return rlist

def get_url(index):
    return "http://baike.fututa.com/a57{}/".format(37 + index)

def get_symbol(ctype):
    return YAO_SYMBOL[ctype]

def show(index):
    info_list = get_yao_info(index)
    for x in range(6):
        c = info_list[5 - x]
        symbol = get_symbol(c[0])
        info = c[1].decode('utf-8').encode('utf-8')
        info = info.replace('\n', '')
        print symbol, '\t' * 2, info

    print get_url(index)

# def main():
#     import split
#     split.main()

# if __name__ == '__main__':
#     main()

