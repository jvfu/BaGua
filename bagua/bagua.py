#coding:utf-8
# from utils import *
import random
from docs import *
from utils import *

def shake_yao():
    return [random.randint(2, 3) for x in xrange(3)]

def shake_gua64():
    return [shake_yao() for x in xrange(6)]

def get_symbol(index):
    utest = ["---"] * 6
    return utest

def get_yao_info(index):
    def has_yao_index(line):
        for i, v in enumerate(YAO_INDEX):
            if v[0] in line or v[1] in line:
                return i
        return -1

    original = ''
    rlist = [original] * 6
    lines = get_info(index)
    if lines is None: return rlist

    for line in lines:
        yao_index = has_yao_index(line)
        if yao_index >= 0 and rlist[yao_index] is original:
            rlist[yao_index] = line

    return rlist

def get_url(index):
    return "http://baike.fututa.com/a57{}/".format(37 + index)

def show(index):
    symbol = get_symbol(index)
    info = get_yao_info(index)
    for x in range(6):
        s = info[5 - x].replace('\n', '')
        print symbol[x], s.decode('utf-8').encode('utf-8')

    print get_url(index)

