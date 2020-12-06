import os
from clint.textui import colored
from codemon.CodemonMeta import template_cpp

def createFile(filename, text, contestName=None):
  full_filename = os.path.join(os.getcwd(), filename)
  if contestName is not None:
    full_filename = os.path.join(os.getcwd(), contestName, filename)

    os.makedirs(full_filename)
    file_extension = ['.cpp','.in','.op', 'Test.cpp', 'Test.in', 'Test.op']
    for extension in file_extension:
      filepath = os.path.join(full_filename, filename + extension)
      file = open(filepath,"w+")
      if extension == '.cpp':
        template = template_cpp()
        file.write(template)

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
    for file in fileNames:
      createFile(file, template_cpp(), contestName)
    # create input file
    print(colored.cyan('Files have been created'))
