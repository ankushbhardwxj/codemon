<<<<<<< HEAD
from clint.textui import colored

def showHelp():
  print("           ---CODEMON---          ")
  print(colored.cyan("  a CLI tool for competitive coders"))
  print("\nCOMMANDS: \n")
  print(colored.yellow("codemon - - - - - - - - - - - - - - - shows help"))
  print(colored.yellow("codemon init <args>  - - - - - initialises a contest directory using format given in options"))
  print(colored.yellow("codemon init <args> -n  - - - - - - - creates file using format given in options"))
  print(colored.yellow("codemon listen  - - - - - - - - - - - compiles and gives output"))
  print(colored.yellow("codemon practice <args>  - - - - - starts a practice session"))
=======
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
>>>>>>> be25714d84b88b0bc96c1b795ecc5782d155730c
