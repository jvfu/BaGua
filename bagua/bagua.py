#coding:utf-8
# from utils import *
import random
from docs import *

def shake_yao():
    return [random.randint(2, 3) for x in xrange(3)]

def shake_gua64():
    return [shake_yao() for x in xrange(6)]

def get_symbol(index):
    utest = """
---
---
---
---
---
---
    """
    return utest

def get_url(index):
    return "http://baike.fututa.com/a57{}/".format(37 + index)

def show(index):
    # print get_symbol(index)
    print get_info(index)
    print get_url(index)

# show(20)
# print shake_gua64()