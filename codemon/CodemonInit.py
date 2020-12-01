import os
from clint.textui import colored
from codemon.CodemonMeta import template_cpp

def init(contestName,fileNames):
  # create a directory with contest name
  try:
    print(colored.green('Make some files and folders for ' + colored.magenta(contestName)))
    path = os.getcwd()
    os.mkdir(path + '/' + contestName)
  except OSError:
    print("Failed! This directory already exists.")
  else:
    print(colored.yellow('Directory is made'))
    # create files for contest (should be 6 cpp files)
    for files in range(len(fileNames)):
      f = open(path + '/' + contestName + '/' + fileNames[files],"w+")
      template = template_cpp()
      f.write(template)
      f.close()
    # create input file
    f = open(path + '/' + contestName + '/' + "input.txt","w+")
    f.close()
    print(colored.cyan('Files have been created'))
