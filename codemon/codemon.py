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
<<<<<<< HEAD
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
=======
    countArg = 0
    for arg in sys.argv:
      countArg+=1

>>>>>>> be25714d84b88b0bc96c1b795ecc5782d155730c
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

<<<<<<< HEAD
    elif toInit == True:
      if isJavaFile == True and isSingleFile == False:
        name = input("Enter Contest Name: ")
        files = get_filename_java()
        initjava(name, files)
=======
        elif sys.argv[countArg] == '-java':
          
          if sys.argv[countArg] == '-n':
            file = sys.argv[countArg+1]
            path = '.'
            f = open(path + '/' + file + '.java',"w+")
            template = template_java()
            f.write(template)
            f.close()
            print(colored.yellow("Created "+file+'.java'))
            break;
          else:
            contestName = sys.argv[countArg]
            fileNames = get_filename_java()
            initjava(contestName, fileNames)
        if sys.argv[countArg] == '-n':
          file = sys.argv[countArg+1]
          path = '.'
          f = open(path + '/' + file + '.cpp',"w+")
          template = template_cpp()
          f.write(template)
          f.close()
          print(colored.yellow("Created "+file+'.cpp'))
          break

        else:
          contestName = sys.argv[countArg]
          fileNames = get_filename()
          init(contestName, fileNames)
>>>>>>> be25714d84b88b0bc96c1b795ecc5782d155730c

      elif isJavaFile == True and isSingleFile == True:
        # extension & path passed directly here
        fileName = input("Enter filename: ")
        dirName = input("Enter directory: ")
        file = [fileName + '.java']
        initjava(dirName, file)
      
      elif isCppFile == True and isSingleFile == False:
        name = input("Enter Contest Name: ")
        files = get_filename()
        init(name, files)

<<<<<<< HEAD
      elif isCppFile == True and isSingleFile == True:
        # extension & path passed directly here
        fileName = input("Enter filename: ")
        dirName = input("Enter directory: ")
        file = [fileName + '.cpp']
        init(dirName, file)

      elif isCppFile == True and toPractice == True:
        name = input("Enter Contest Name: ")
        practiceFiles = get_practice_files()
        init(name, practiceFiles)

      elif isJavaFile == True and toPractice == True:
        name = input("Enter Contest Name: ")
        practiceFiles = get_practice_files_java()
        initjava(name, practiceFiles)
=======
      elif arg == "practice":
        if sys.argv[countArg] == '-cpp':
          contestName = sys.argv[countArg]
          practiceFiles = get_practice_files()
          init(contestName, practiceFiles)
        elif sys.argv[countArg] == '-java':
          contestName = sys.argv[countArg]
          practiceFiles = get_practice_files_java()
          initjava(contestName, practiceFiles)
        contestName = sys.argv[countArg]
        practiceFiles = get_practice_files()
        init(contestName, practiceFiles)

      elif arg == "--help":
        showHelp()
        break
>>>>>>> be25714d84b88b0bc96c1b795ecc5782d155730c
