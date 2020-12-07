import sys
import os
import ctypes
import json
from clint.textui import colored
from os.path import expanduser
from getpass import getpass
import stdiomask

home = expanduser("~")

def codemonReg():
    file_name = ".codemon"
    path = os.path.join(home, file_name)
    if not os.path.exists(path):
        os.makedirs(path)
        if os.name == 'nt':
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ret = ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN)

    print("Codemon User Registration")
    print("\nPlease enter the following data.\nYour sensitive information is collected for making your life easier while using Codemon.\nIt will be stored on your local machine.\nIt won't be stored or used by Codemon developers for any purpose. ")
    name = input("\nEnter Name : ")
    codeforces_username = input("Codeforces username (without @) : ")
    codeforces_password = stdiomask.getpass(prompt="Codeforces password (not shown): ")
    github_username = input("Github username (without @) : ")
    github_password = stdiomask.getpass(prompt="GitHub Password (not shown): ")
    dataDict = {}
    dataDict["name"] = name
    dataDict["codeforces_username"] = codeforces_username
    dataDict["codeforces_password"] = codeforces_password
    dataDict["github_username"] = github_username
    dataDict["github_password"] = github_password
    dataJson = json.dumps(dataDict, indent=4)
    full_filename = os.path.join(home, file_name, "meta.json")
    with open(full_filename, 'w+') as f:
        f.write(dataJson)




