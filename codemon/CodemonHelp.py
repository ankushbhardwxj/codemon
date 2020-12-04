from clint.textui import colored

def showHelp():
  print(colored.green("           ---CODEMON---          "))
  print("A CLI tool to ace competitive programming contests")
  print(colored.cyan("\nCOMMANDS: \n"))
  print("codemon - - - - - - - - - - - - - - -  displays this message")
  print("codemon --help - - - - - - - - - - - - shows help")
  print("codemon init <args> - - - - - - initialises a contest with required format")
  print("codemon init -n <args> <file> - - - - - - - - creates file with given name")
  print("codemon listen - - - - - - - - - - - - compiles and gives output")
  print("codemon practice <args> - - - - - - Starts a practice session")
  print(colored.cyan("\nSupported args: -cpp, -java"))