#!/usr/bin/python
# -*- encoding: utf-8 -*-

''' Return contents of a given directory on std-out

    Output:
    - type FILE or DIR for each entity
    - entity name
    - relative path from given directory
    - MD5-Sum is provided for type FILE
'''

import os
import hashlib

def dir_rec(pt):
    try:

        p = os.listdir(pt)
        for f in p:
            # concat full path
            fp = pt + os.sep + f
            # print entity
            print("type:" + type(fp), f, "[" + os.path.relpath(fp, os.path.dirname(pt)) + "]", md5(fp))
            # scan dirs recursively
            if(os.path.isdir(fp)):
                dir_rec(fp)
    # handle some errors
    except (FileNotFoundError, PermissionError) as e:
        print("Error:", e)
        return None

def md5(fil):
    if(os.path.isfile(fil)):
        hash_md5 = hashlib.md5(fil.encode('utf-8'))
        return "md5:" + hash_md5.hexdigest()
    else:
        return ''

def type(pth):
    if os.path.isdir(pth):
        return "DIR"
    elif os.path.isfile(pth):
        return "FILE"


if __name__ == "__main__":

    dir_rec('D:\\temp\\src\\')
    #dir_rec('C:\\ProgramData\\')