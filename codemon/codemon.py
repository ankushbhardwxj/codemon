#!/usr/bin/python3
import sys
import os
import re
from clint.textui import colored
from codemon.CodemonHelp import showHelp
from codemon.CodemonListen import listen
from codemon.CodemonInit import init
from codemon.CodemonMeta import template_cpp,get_filename, get_practice_files
from codemon.CodemonFetch import fetch_tests, make_structure

def main():
  if len(sys.argv) < 2:
    showHelp()

  else:
    countArg = 0
    for arg in sys.argv:
      countArg+=1

      if arg == "init":
        if sys.argv[countArg] == '-n':
          fileName = sys.argv[countArg+1]
          template = template_cpp()
          init_single_file(f'{fileName}.cpp', template)
          print(colored.yellow(f'Created {fileName}.cpp'))
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
      elif arg == "fetch":
        try:
          # if User provides contest number as arguement.
          fetch_tests(sys.argv[countArg])
        except IndexError:
          # Extract all numbers from current directory name.
          contest_number = ''.join(re.findall(r'\d+', os.getcwd().split('/')[-1]))
          fetch_tests(contest_number)


def init_single_file(filename, template='\n'):
  full_filename = os.path.join(os.getcwd(), filename)
  with open(full_filename, 'w+') as f:
    f.write(template)
