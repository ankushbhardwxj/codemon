from clint.textui import colored

def showHelp():
  print(colored.green("""  _________  ___  ______  _______  _  __
 / ___/ __ \/ _ \/ __/  |/  / __ \/ |/ /
/ /__/ /_/ / // / _// /|_/ / /_/ /    / 
\___/\____/____/___/_/  /_/\____/_/|_/  
                                        """))
  print("A CLI tool to ace competitive programming contests")
  print(colored.cyan("\nCOMMANDS: \n"))
  print("codemon - - - - - - - - - - - - - - -  displays this message")
  print("codemon --help - - - - - - - - - - - - shows help")
  print("codemon init <contestName> - - - - - - initialises a contest")
  print("codemon init -n <file> - - - - - - - - creates file with given name")
  print("codemon listen - - - - - - - - - - - - compiles and gives output")
  print("codemon practice <dirName> - - - - - - Starts a practice session")