from clint.textui import colored

def showHelp():
	print("           ---CODEMON---          ")
	print(colored.cyan("  a CLI tool for competitive coders"))
	print("\nCOMMANDS: \n")
	print("codemon - - - - - - - - - - - - - - - shows help")
	print("codemon init <contestName>  - - - - - initialises a contest")
	print("codemon init -n <file>  - - - - - - - creates file with given name")
	print("codemon listen  - - - - - - - - - - - compiles and gives output")
	print("codemon practice <dirName>  - - - - - starts a practice session")