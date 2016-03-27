#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

VERSION = '0.0.2'

setup(
    name         = 'BaGua',
    version      = VERSION,
    author       = 'Floyda',
    author_email = 'floyda@163.com',
    license      = 'MIT',
    description  = '八卦是中国文化的基本哲学概念',
    long_description = '八卦是中国文化的基本哲学概念...',
    keywords='bagua chinese',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    url          = 'https://github.com/FloydaGithub/BaGua',
    packages=find_packages(),
    package_data = {
    },
    include_package_data=True,
    zip_safe=True,
    install_requires = [
        'docopt >= 0.6.1',
        'pygments >= 1.6.0',
    ],
    scripts          = ['bin/bagua'],
)
