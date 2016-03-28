#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

import bagua
VERSION = bagua.VERSION

setup(
    name         = 'BaGua',
    version      = VERSION,
    author       = 'Floyda',
    author_email = 'floyda@163.com',
    license      = 'MIT',
    description  = '科学占卜, 计算机算命.',
    long_description = '科学占卜, 计算机算命...',
    keywords='chinese bagua yijing zhouyi',
    url          = 'https://github.com/FloydaGithub/BaGua',
    # packages=find_packages(),
    packages=[
        'bagua',
        'bagua.docs',
    ],
    package_data = {
        'bagua.docs': ['*.txt'],
        'bagua': ['*.txt'],
    },
    # include_package_data=True,
    # zip_safe=True,
    install_requires = [
        'docopt >= 0.6.1',
    ],
    scripts          = ['bin/bagua'],
    # entry_points={
    #     'console_scripts':[
    #     ]
    #   },
)
