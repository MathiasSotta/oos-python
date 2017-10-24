#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os

def dir_rec(top):

    p = os.listdir(top)

    for f in p:
        fp = top+os.sep+f
        fs = top+os.sep


        print(f, os.path.relpath(fp))

        if (os.path.isdir(fp)):
            dir_rec(fp)



if __name__ == "__main__":
   dir_rec('D:\\temp\\src')

    # d = os.walk('D:\\temp\\src')
    # for fe in d:
    #     print(fe)