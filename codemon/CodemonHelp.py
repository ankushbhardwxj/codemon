from clint.textui import colored

def showHelp():
  print(colored.green("           ---CODEMON---          "))
  print("A CLI tool to ace competitive programming contests")
  print(colored.cyan("\nCOMMANDS: \n"))
  print("codemon - - - - - - - - - - - - - - -  displays this message")
  print("codemon --help - - - - - - - - - - - - shows help")
  print("codemon init <contestName> - - - - - - initialises a contest")
  print("codemon fetch <contestName> - - - - fetches all the sample test cases for the contest name provided")
  print("codemon fetch  - - - - - - - - - - - extracts contest name from contest directory name and fetches all sample test cases ")
  print("codemon init -n <file> - - - - - - - - creates file with given name")
  print("codemon listen - - - - - - - - - - - - compiles and gives output")
  print("codemon practice <dirName> - - - - - - Starts a practice session")
