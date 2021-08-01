from clint.textui import colored

def showHelp():

  print("\n")
  #Logo font used is ANSI Shadow
  print(colored.green(""" ██████╗ ██████╗ ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║
██║     ██║   ██║██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
██║     ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
╚██████╗╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                               """))
  
  print("A CLI tool to ace competitive programming contests")
  print(colored.cyan("\nCOMMANDS: \n"))
  print("codemon - - - - - - - - - - - - - - -  displays this message.")
  print("codemon --help | -h - - - - - - - - -  shows help.")
  print("codemon init <contestName> - - - - - - initialises a contest.")
  print("codemon init -f <contest> - - - - -  - runs init and fetch at the same time.")
  print("codemon init -n <file> - - - - - - - - creates file with given name.")
  print("codemon fetch  - - - - - - - - - - - - fetches testcases from CodeForces.")
  print("codemon listen - - - - - - - - - - - - compiles and gives output.")
  print("codemon clean - - - - - - - - - - - -  cleans a contest directory.")
  print("codemon reg - - - - - - - - - - - - -  Register user details.")
