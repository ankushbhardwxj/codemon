import sys
import os
import ctypes
from clint.textui import colored

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def codemonReg():
    print(ROOT_DIR)
    path = os.path.join(ROOT_DIR, "codemon")
    if not os.path.exists(path):
        os.makedirs(path)
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN)
    meta = ""
    name = input("Name : ")
    cf_user = input("CF Username : ")
    cf_pass = input("CF Password : ")
    git_user = input("GitHub Username : ")
    git_pass = input("GitHub Password : ")
    meta += name + "\n" + cf_user + "\n" + cf_pass + "\n" + git_user + "\n" + git_pass
    full_filename = os.path.join(ROOT_DIR, "codemon", "meta.txt")
    with open(full_filename, 'w+') as f:
        f.write(meta)




