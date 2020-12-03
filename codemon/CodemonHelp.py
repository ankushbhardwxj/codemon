from clint.textui import colored
import os

def showHelp():
  print("           ---CODEMON---          ")
  print(colored.cyan("  a CLI tool for competitive coders"))
  print("\nCOMMANDS: \n")
  print(colored.red("NOTE: Use the options -cpp and -java correctly in place of <args> to work \n"))
  print(colored.yellow("codemon - - - - - - - - - - - - - - - shows help"))
  print(colored.yellow("codemon init <args> <contestName>  - - - - - initialises a contest in CPP/Java format"))
  print(colored.yellow("codemon init <args> -n <file>  - - - - - - - creates file with given name in CPP/Java format"))
  print(colored.yellow("codemon listen  - - - - - - - - - - - compiles and gives output"))
  print(colored.yellow("codemon practice <args> <dirName>  - - - - - starts a practice session"))
  print(colored.green("           ---CODEMON---          "))