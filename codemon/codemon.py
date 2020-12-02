#!/usr/local/bin
import sys
import os
from clint.textui import colored
from codemon.CodemonHelp import showHelp
from codemon.CodemonListen import listen
from codemon.CodemonInit import init
from codemon.CodemonMeta import template_cpp,get_filename,get_practice_files

def main():
  if len(sys.argv) < 2:
    showHelp()

  else:
    countArg = 0
    for arg in sys.argv:
      countArg+=1

      if arg == "init":
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
          fileNames = get_filename(contestName)
          init(contestName, fileNames)

      elif arg == "listen":
        listen()

      elif arg == "practice":
        contestName = sys.argv[countArg]
        practiceFiles = get_practice_files()
        init(contestName, practiceFiles)

      elif arg == "--help":
        showHelp()
        break
