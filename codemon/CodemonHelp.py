from clint.textui import colored

def showHelp():
  print(colored.green("           ---CODEMON---          "))
  print("A CLI tool to ace competitive programming contests")
  print(colored.cyan("\nCOMMANDS: \n"))
  print("codemon - - - - - - - - - - - - - - -  displays this message")
  print("codemon --help - - - - - - - - - - - - shows help")
  print("codemon init <contestName> - - - - - - initialises a contest")
  print("codemon init -n <file> - - - - - - - - creates file with given name")
  print("codemon listen - - - - - - - - - - - - compiles and gives output")
  print("codemon reg - - - - - - - - - - - - -  Register user details")
  print("codemon practice <dirName> - - - - - - Starts a practice session")