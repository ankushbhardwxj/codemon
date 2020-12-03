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
        name = input("Enter Contest Name:")
        files = ['A.java', 'B.java', 'C.java', 'D.java', 'E.java', 'F.java']
        initjava(name, files)

      elif isJavaFile == True and isSingleFile == True:
        # extension & path passed directly here
        fileName = input("Enter filename:")
        dirName = input("Enter directory: ")
        initjava(dirName, fileName+'.java')
      
      elif isCppFile == True and isSingleFile == False:
        name = input("Enter Contest Name:")
        files = ['A.cpp', 'B.cpp', 'C.cpp', 'D.cpp', 'E.cpp', 'F.cpp']
        init(name, files)

      elif isCppFile == True and isSingleFile == True:
        # extension & path passed directly here
        fileName = input("Enter filename:")
        dirName = input("Enter directory: ")
        init(dirName, fileName+'.cpp')

      elif isCppFile == True and toPractice == True:
        name = input("Enter Contest Name:")
        practiceFiles = ['A.cpp', 'B.cpp', 'C.cpp']
        init(name, practiceFiles)

      elif isJavaFile == True and toPractice == True:
        name = input("Enter Contest Name:")
        practiceFiles = ['A.java', 'B.java', 'C.java']
        initjava(name, practiceFiles)
