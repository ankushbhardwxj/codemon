#!/usr/bin/python3
import sys
import os
from codemon.CodemonHelp import showHelp
from codemon.CodemonListen import listen
from codemon.CodemonInit import init, init_single_file
from codemon.CodemonReg import codemonReg
from codemon.CodemonMeta import get_filename
from codemon.CodemonFetch import fetchTestcases
from codemon.CodemonParse import Parser
from codemon.CodemonClean import codemonClean

def main():
  arg = Parser()
  arg.parse(sys.argv[1:])

  # !Error while parsing 
  if len(arg.error) > 0:
    print(arg.error)
    return
  # help command
  if arg.help: showHelp()
  # register an user and create `~/.codemon`
  if arg.register:
    codemonReg()
  # init single file
  if arg.init and arg.initFlags["single"]:
    fileName = arg.name
    if len(fileName) > 0: init_single_file(f'{fileName}', arg.initFlags)
    else:
      print('Cannot create file since no filename has been specified.')
      print("Try 'codemon init -n <filename>'.")
  # init contest directory
  if arg.init and not arg.initFlags["single"]:
    contestName = arg.name
    if len(contestName) > 0:
        fileNames = get_filename(contestName)
        init(contestName, fileNames, arg.initFlags)
        if arg.initFlags["fetch"]:
          fetchTestcases(fileNames, contestName)
    else:
      print('Cannot create contest directory since no directory name has been specified.')
      print("Try 'codemon init <dirName>'.")
  # fetch inside contest directory
  if arg.fetch:
    cwd = os.getcwd()
    contestName = os.path.basename(cwd)
    fileNames = get_filename(contestName)
    fetchTestcases(fileNames, contestName)
  # listen to a contest directory or file
  if arg.listen: listen()
  # clean contest directory
  if arg.clean:
    dirName = arg.name
    if len(dirName) > 0: codemonClean(dirName)
    else: print('Cannot clean since no directory name has been specified')

