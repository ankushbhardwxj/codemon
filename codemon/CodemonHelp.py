from clint.textui import colored
import os

def showHelp():
  os.system('cls sys')
  print(colored.green("           ---CODEMON---          "))
  print("A CLI tool for competitive coders")
  print("Get faster and more accurate during a coding contest.")
  print("No more compile the code everytime you make a change. Just save the code and we will do the rest for you.")
  print("Test your code with different inputs easily. Compile them locally. And, save those code files to your desired directory.")
  print("Generate test cases and test those test cases with your code automatically.")
  print(colored.cyan("\nQuick COMMANDS: \n"))
  print(colored.yellow("codemon") + " - - - - - - - - - - - - - - -  - - A Overview of the program")
  print(colored.yellow("codemon help") + " - - - - - - - - - - - - - - - Get answers to your common queries and list of all commands & features supported.")

def showHelpDetailed():
  print(colored.cyan("\nList of all COMMANDS: \n"))
  print(colored.yellow("codemon") + " - - - - - - - - - - - - - - -  A Overview of the program")
  print(colored.yellow("codemon help") + " - - - - - - - - - - - - - Get answers to your common queries and list of all commands & features supported.")
  print(colored.yellow("codemon init <contestName>") + " - - - - - - Initialises a directory with the given contest name. directory includes all necessary files.")
  print(colored.yellow("codemon init -n <file>") + " - - - - - - - - Creates a file with given name in the current working directory.")
  print(colored.yellow("codemon listen") + " - - - - - - - - - - - - Compiles and gives output as soon as you save a file.")
  print(colored.yellow("codemon practice <dirName>") + " - - - - - - Starts a practice session")
  print(colored.cyan("\nSome other things to keep in mind: \n"))
  print("You dont need to compile the program each time. It will keep listening for changes and as soon as you save the code. It will compile the changed file automatically and save the outputs to corresponding files.")
  print("While listening for changes, if you want to stop listening for changes, press ctrl+c")
  print(colored.cyan("\nIf you find any issues, you can report it to our GitHub repository. https://github.com/ankingcodes/codemon"))


