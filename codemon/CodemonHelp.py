from clint.textui import colored

def showHelp():
  print("           ---CODEMON---          ")
  print(colored.cyan("  a CLI tool for competitive coders"))
  print("\nCOMMANDS: \n")
  print(colored.yellow("codemon - - - - - - - - - - - - - - - shows help"))
  print(colored.yellow("codemon init <contestName> <args>  - - - - - initialises a contest directory using format given in options"))
  print(colored.yellow("codemon init <args> -n <file>  - - - - - - - creates file using format given in options"))
  print(colored.yellow("codemon listen  - - - - - - - - - - - compiles and gives output"))
  print(colored.yellow("codemon practice <args> <dirName>  - - - - - starts a practice session"))
