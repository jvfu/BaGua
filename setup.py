from distutils.core import setup
import os

setup(
    name         = 'BaGua',
    version      = '0.01',
    author       = 'Floyda',
    author_email = 'floyda@163.com',
    license      = 'GPL3',
    description  = '八卦是中国文化的基本哲学概念',
    url          = '',
    packages     = [
        # 'cheat',
        # 'cheat.cheatsheets',
        # 'cheat.test',
    ],
    package_data = {
        # 'cheat.cheatsheets': [f for f in os.listdir('cheat/cheatsheets') if '.' not in f]
    },
    scripts          = ['bin/bagua'],
    install_requires = [
        'docopt >= 0.6.1',
        'pygments >= 1.6.0',
    ]
)
