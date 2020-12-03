#!/usr/local/bin
import sys
import os
from clint.textui import colored
from codemon.CodemonHelp import showHelp
from codemon.CodemonListen import listen
from codemon.CodemonInit import init, initjava
from codemon.CodemonMeta import template_cpp, get_filename, get_practice_files, template_java, get_filename_java, get_practice_files_java


def main():

  if len(sys.argv) < 2:
    showHelp()

  else:
    countArg = 0;
    isCppFile = False
    isJavaFile = False
    isSingleFile = False
    toInit = False
    toListen = False
    toPractice = False
    targetFile = ""
    # get all arguments and flags
    for arg in sys.argv:
      countArg+=1;
      if arg == "init":
        toInit = True
      elif arg == "-cpp":
        isCppFile = True
      elif arg == "-java":
        isJavaFile = True
      elif arg == "-n":
        isSingleFile = True
      elif arg == "listen":
        isListen = True
      elif arg == "practice":
        toPractice = True
      else:
        targetFile = arg

    # based on booleans perform action
    if toListen == True:
      listen()
      
    elif toInit == True:
      if isJavaFile == True and isSingleFile == False:
        extension = ".java" # we can also pass it directly in function
        path = "."
        # create that directory with that given name (targetFile)
        createTargetDirectory(path, template_java, targetFile, extension)

      elif isJavaFile == True and isSingleFile == True:
        # extension & path passed directly here
        createTargetFile('.', template_cpp, targetFile, 'java') 
      
      elif isCppFile == True and isSingleFile == False:
        createTargetFile('.', template_cpp, targetFile, 'cpp')
      
      elif isCppFile == True and isSingleFile == False:
        extension = ".cpp" # for c++
        path = "."
        createTargetDirectory(path, template_cpp, targetFile, extension)

    print(colored.green("Option processed and complete!"))