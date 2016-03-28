import os
from bagua import *

f = open('{}/version.txt'.format(os.path.split(__file__)[0]))
VERSION = f.read()
f.close()
