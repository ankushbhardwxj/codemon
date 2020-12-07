
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
from codemon.CodemonParse import Commands

def main():
  arg = Commands()
  arg.parse(sys.argv[1:])

  if arg.help:
    showHelp()

  elif arg.to_listen:
    listen()

  elif arg.to_practice:
    contestName = sys.argv[countArg]
    practiceFiles = get_practice_files()
    init(contestName, practiceFiles)

  elif arg.to_init:
    if arg.init_flags["is_single"]:
      fileName = arg.single_file_name
      template = template_cpp()
      init_single_file(f'{fileName}.cpp', template)
      print(colored.yellow(f'Created {fileName}.cpp'))
    else:
      contestName = arg.contest_name
      fileNames = get_filename(contestName)
      init(contestName, fileNames)
  else:
    showHelp()

def init_single_file(filename, template='\n'):
  full_filename = os.path.join(os.getcwd(), filename)
  with open(full_filename, 'w+') as f:
    f.write(template)
