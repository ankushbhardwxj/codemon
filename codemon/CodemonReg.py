import sys
import os
import ctypes
from clint.textui import colored

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def codemonReg():
    #print(ROOT_DIR)
    prefix = '.' if os.name != 'nt' else ''
    file_name = prefix + "codemon"
    path = os.path.join(ROOT_DIR, file_name)
    if not os.path.exists(path):
        os.makedirs(path)
        if os.name == 'nt':
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ret = ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN)

    print("Codemon User Registration")
    print("\nPlease enter the following data. Your sensitive information is collected for making your life easier while using Codemon and will be stored on your local machine. It won't be stored or used by Codemon developers for any purpose. ")
    name = input("\nEnter Name : ")
    codeforces_username = input("Codeforces username (without @) : ")
    codeforces_password = input("Codeforces password: ")
    github_username = input("Github username: ")
    github_password = input("GitHub Password : ")
    meta = ('{\n', '  "name": "', name, '",\n', '  "codeforces username": "', codeforces_username, '",\n',
            '  "codeforces password": "', codeforces_password, '",\n',
            '  "github username": "', github_username, '",\n',
            '  "github password": "', github_password, '",\n', '}\n')
    jsondata = ''.join(meta)
    full_filename = os.path.join(ROOT_DIR, file_name, "meta.txt")
    with open(full_filename, 'w+') as f:
        f.write(jsondata)




