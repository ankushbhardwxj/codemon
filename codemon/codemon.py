#!/usr/bin/python3
import sys
import os
from clint.textui import colored
from codemon.CodemonHelp import showHelp
from codemon.CodemonListen import listen
from codemon.CodemonInit import init, initjava, write_to_file_single
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
    if isListen == True:
      listen()

    elif toInit == True:
      if isJavaFile == True and isSingleFile == False:
        name = input("Enter Contest Name: ")
        files = get_filename_java()
        initjava(name, files)

      elif isJavaFile == True and isSingleFile == True:
        file = targetFile + '.java'
        text = template_java()
        write_to_file_single(file, text)
      
      elif isCppFile == True and isSingleFile == False:
        name = input("Enter Contest Name: ")
        files = get_filename()
        init(name, files)

      elif isCppFile == True and isSingleFile == True:
        file = targetFile + '.cpp'
        text = template_cpp()
        write_to_file_single(file, text)

    elif isCppFile == True and toPractice == True:
        name = input("Enter Contest Name: ")
        practiceFiles = get_practice_files()
        init(name, practiceFiles)
      
    elif isJavaFile == True and toPractice == True:
      name = input("Enter Contest Name: ")
      practiceFiles = get_practice_files_java()
      initjava(name, practiceFiles)