#!/usr/local/bin
import sys
import os
from clint.textui import colored
from codemon.CodemonHelp import showHelp
from codemon.CodemonListen import listen
from codemon.CodemonInit import init
from codemon.CodemonFetch import fetch_tests, make_structure
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
          fileNames = get_filename()
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

      elif arg == "fetch":
        # In case user provided the contest name.
        try:
          fetch_tests(sys.argv[countArg])
        # if not check if in contest directory
        # then extract the contest name and fetch sample tests.
        except IndexError:
          # Directory after init should have 6 source files and one input file.

          # check is a list that has the expected state of contest directory
          check = ['A', 'B', 'C', 'D', 'E', 'F', 'input']

          # current is a list that has the state of the current directory.
          current = sorted(list(map(lambda x: x.split('.')[0], os.listdir())))
          if current != check:
            print(colored.red("Not in contest directory !!\nPlease navigate to the contest directory"))
          else:
            fetch_tests(os.getcwd().split('/')[-1])
