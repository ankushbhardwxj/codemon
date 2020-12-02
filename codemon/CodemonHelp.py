from clint.textui import colored
import os

def showHelp():
  print(colored.green("           ---CODEMON---          "))
  print("A CLI tool for competitive coders")
  print("Get faster and more accurate during a coding contest.")
  print(colored.cyan("\nCOMMANDS: \n"))
  print(colored.yellow("codemon") + " - - - - - - - - - - - - - - -  shows help")
  print(colored.yellow("codemon --help") + " - - - - - - - - - - - - shows help")
  print(colored.yellow("codemon init <contestName>") + " - - - - - - initialises a contest")
  print(colored.yellow("codemon init -n <file>") + " - - - - - - - - creates file with given name")
  print(colored.yellow("codemon listen") + " - - - - - - - - - - - - compiles and gives output")
  print(colored.yellow("codemon practice <dirName>") + " - - - - - - Starts a practice session")
  print(colored.cyan("\nIf you find any issues, you can report it to our GitHub repository. https://github.com/ankingcodes/codemon"))