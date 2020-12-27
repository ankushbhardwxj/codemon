#!/usr/bin/python3
import sys
import os
from clint.textui import colored
from codemon.CodemonHelp import showHelp
from codemon.CodemonListen import listen
from codemon.CodemonInit import init, init_single_file
from codemon.CodemonReg import codemonReg
from codemon.CodemonMeta import get_filename, get_practice_files
from codemon.CodemonFetch import fetch_tests
from codemon.CodemonParse import Parser

def main():
  arg = Parser()
  arg.parse(sys.argv[1:])

  if arg.help:
    showHelp()

  elif arg.to_listen:
    listen()

  elif arg.to_practice:
    contestName = arg.name
    practiceFiles = get_practice_files()
    init(contestName, practiceFiles, arg.init_flags)

  elif arg.to_init:
    if arg.init_flags["is_single"]:
      fileName = arg.name
      init_single_file(f'{fileName}', arg.init_flags)

    else:
      contestName = arg.name
      fileNames = get_filename(contestName)
      init(contestName, fileNames, arg.init_flags)
      if arg.init_flags["to_fetch"]:
        fetch_tests(fileNames, contestName)

  elif arg.to_fetch:
    contestName = os.path.basename(os.getcwd())
    fileNames = get_filename(contestName)
    fetch_tests(fileNames, contestName)

  elif arg.Reg:
    codemonReg()

  else:
    showHelp()

