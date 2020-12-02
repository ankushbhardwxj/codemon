import os
from clint.textui import colored
from codemon.CodemonMeta import template_cpp, write_to_file

def init(contestName,fileNames):
  # create a directory with contest name
  try:
    print(colored.green('Make some files and folders for ' + colored.magenta(contestName)))
    os.makedirs(os.path.join(os.getcwd(), contestName))
  except OSError: 
    print("Failed! This directory cannot be created.")
  else:
    print(colored.yellow('Directory is made'))
      # create files for contest (should be 6 cpp files)
    for files in range(len(fileNames)):
      write_to_file(fileNames[files], template_cpp(), contestName)
    # create input file
    write_to_file('input.txt', '', contestName)
    print(colored.cyan('Files have been created'))
