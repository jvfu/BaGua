#!coding=utf-8
import os

os.mkdir("info")

def create_file(index, content):
    file_name = "info/{}.txt".format(index)
    f = open(file_name, "w")
    f.write(str(content))
    f.close()

content = ""
index = 0
for line in open("zhouyi.txt"):
    if "《易經》" in line:
        if not content is "":
            index += 1
            create_file(index, content)
            
        content = ""
    # else:
    content += line
    
create_file(64, content)