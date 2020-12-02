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
    # create folders for each problem and in each folder 3 files: (fileName.cpp, input.txt, output.txt)
    for file in fileNames:
      folderPath = path + '/' + contestName + '/' + file
      os.mkdir(folderPath)
      # create .cpp file
      f = open(folderPath + '/' + file + '.cpp', "w+")
      template = template_cpp()
      f.write(template)
      f.close()
      # create input file
      f = open(folderPath + '/' + 'input.txt', "w+")
      f.close()
      # create output file
      f = open(folderPath + '/' + 'output.txt', "w+")
    print(colored.cyan('Files have been created'))
