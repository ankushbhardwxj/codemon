import os
from clint.textui import colored
from codemon.CodemonMeta import template_cpp, template_java

def write_to_file(filename, text, contestName=None):
  full_filename = os.path.join(os.getcwd(), filename)
  if contestName is not None:
    full_filename = os.path.join(os.getcwd(), contestName, filename)
  with open(full_filename, 'w+') as f:
    f.write(text)

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

def initjava(contestName,fileNames):
  # create a directory with contest name
  try:
    print(colored.green('Make some files and folders for ' + colored.magenta(contestName)))
    path = os.getcwd()
    os.mkdir(path + '/' + contestName)
  except OSError:
    print("Failed! This directory already exists.")
  else:
    print(colored.yellow('Directory is made'))
    # create files for contest (should be 6 java files)
    for files in range(len(fileNames)):
      f = open(path + '/' + contestName + '/' + fileNames[files],"w+")
      template = template_java()
      f.write(template)
      f.close()
    # create input file
    f = open(path + '/' + contestName + '/' + "input.txt","w+")
    f.close()
    print(colored.cyan('Files have been created'))
