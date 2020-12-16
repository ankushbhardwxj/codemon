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
  print("codemon - - - - - - - - - - - - - - - -  Shows help")
  print("codemon --help - - - - - - - - - - - - - Shows help")
  print("codemon init <contestName> - - - - - - - Initialises a contest")
  print("codemon fetch <contestName> - - - - - -  Fetches sample TC from CF for <contestName> round")
  print("codemon fetch  - - - - - - - - - - - - - Extracts round name from directory. Also, fetches sample TC from CF")
  print("codemon init -n <file> - - - - - - - - - Creates file with given name")
  print("codemon listen - - - - - - - - - - - - - Listens for changes in code. Also, compiles and gives output")
  print("codemon reg - - - - - - - - - - - - - -  Register user details")
  print("codemon practice <dirName> - - - - - - - Starts a practice session")
