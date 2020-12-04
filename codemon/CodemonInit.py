import os
from clint.textui import colored
from codemon.CodemonMeta import template_cpp

def write_to_file(filename, text, contestName=None):
  full_filename = os.path.join(os.getcwd(), filename)
  if contestName is not None:
    full_filename = os.path.join(os.getcwd(), contestName, filename)

    os.makedirs(full_filename)
    
    cppFile = full_filename + '/' + filename + '.cpp'
    f = open(cppFile,"w+")
    template = template_cpp()
    f.write(template)

    inpFile = full_filename + '/' + filename + '.in'
    f = open(inpFile,"w+")
    outFile = full_filename + '/' + filename + '.op'
    f = open(outFile,"w+")

    cppTest = full_filename + '/' + 'test_case.cpp'
    f = open(cppTest,"w+")
    inpTest = full_filename + '/' + 'test_case.in'
    f = open(inpTest,"w+")
    outTest = full_filename + '/' + 'test_case.out'
    f = open(outTest,"w+")


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
    print(colored.cyan('Files have been created'))
