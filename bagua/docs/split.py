#!coding=utf-8
import os

def docs_dir():
    return os.path.split(__file__)

def create_file(index, content):
    path, _ = docs_dir()
    file_name = "{}/info/{}".format(path, index)
    f = open(file_name, "w")
    f.write(str(content))
    f.close()

def main():
    content = ""
    index = 0
    path, _ = docs_dir()
    os.system('rm -fr {}/info'.format(path))
    os.mkdir("{}/info".format(path))
    for line in open(path + "/zhouyi"):
        if "《易經》" in line:
            if not content is "":
                index += 1
                create_file(index, content)
                
            content = ""
        # else:
        content += line

    create_file(64, content)

if __name__ == '__main__':
    main()
    
