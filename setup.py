#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

setup(
    name         = 'BaGua',
    version      = '0.01',
    author       = 'Floyda',
    author_email = 'floyda@163.com',
    license      = 'MIT',
    description  = '八卦是中国文化的基本哲学概念',
    long_description = '八卦是中国文化的基本哲学概念...',
    keywords='bagua chinese',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    url          = '',
    packages=find_packages(),
    package_data = {
        # 'cheat.cheatsheets': [f for f in os.listdir('cheat/cheatsheets') if '.' not in f]
    },
    include_package_data=True,
    zip_safe=True,
    install_requires = [
        'docopt >= 0.6.1',
        'pygments >= 1.6.0',
    ],
    scripts          = ['bin/cheat'],
)
