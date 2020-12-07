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
        writeMeta(path)
    else:
        if os.path.exists(os.path.join(path, "meta.json")):
            print("Meta file already exists.")
            overwrite = input("Do you want to overwrite it (y/n)? ")
            if overwrite == 'y':
                writeMeta(path)
        else:
            writeMeta(path)

def writeMeta(path):
    print("Codemon User Registration")
    print("\nPlease enter the following data.\nYour sensitive information is collected for making your life easier while using Codemon.\nIt will be stored on your local machine.\nIt won't be stored or used by Codemon developers for any purpose. ")
    name = input("\nEnter Name : ")
    while (name == ''):
        print("No Input Detected")
        name = input("Enter Name : ")
    codeforces_username = input("\nCodeforces username (without @) : ")
    while (codeforces_username == ''):
        print("No Input Detected")
        codeforces_username = input("Codeforces username (without @) : ")
    codeforces_password = stdiomask.getpass(prompt="\nCodeforces password : ")
    while (codeforces_password == ''):
        print("No Input Detected")
        codeforces_password = stdiomask.getpass(prompt="Codeforces password : ")
    github_username = input("\nGithub username (without @) : ")
    while (github_username == ''):
        print("No Input Detected")
        github_username = input("Github username (without @) : ")
    github_password = stdiomask.getpass(prompt="\nGitHub Password : ")
    while (github_password == ''):
        print("No Input Detected")
        github_password = stdiomask.getpass(prompt="GitHub Password : ")
    dataDict = {}
    dataDict["name"] = name
    dataDict["codeforces_username"] = codeforces_username
    dataDict["codeforces_password"] = codeforces_password
    dataDict["github_username"] = github_username
    dataDict["github_password"] = github_password
    dataJson = json.dumps(dataDict, indent=4)
    full_filename = os.path.join(path, "meta.json")
    with open(full_filename, 'w+') as f:
        f.write(dataJson)




