import os

def docs_dir():
    return os.path.split(__file__)

def get_info(index):
    path = docs_dir()[0]
    name = "{path}/info/{index}.txt".format(path=path, index=index)
    try:
        f = open(name)
        info = f.read()
        f.close()
        return info
    except Exception, e:
        return "..."
