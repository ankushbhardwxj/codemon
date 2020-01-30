#!/usr/bin/python
import sys
import os
import time
import logging
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from clint.textui import colored



# init takes an input contest name and creates a directory
# with that name and creates 5 files. Also it copies content 
# from a template doc to each of the files.
template = '#include<iostream>\nusing namespace std;\n\nint main(){ \n\n	return 0; \n}'

def init(contestName):
	# create a directory with contest name
	try:
		print(colored.green('Make some files and folders for ' + colored.magenta(contestName)));
		path = os.getcwd()
		os.mkdir(path + '/' + contestName)
	except OSError: 
		print("Failed! This directory already exists.")
	else:
		print(colored.yellow('Directory is made'))
			# create files for contest (should be 6 cpp files)
		fileNames = ['A.cpp','B.cpp','C.cpp','D.cpp','E.cpp','F.cpp']
		for files in range(len(fileNames)):
			f = open(path + '/' + contestName + '/' + fileNames[files],"w+")
			f.write(template)
			f.close()
		#create input file
		f = open(path + '/' + contestName + '/' + "input.txt","w+")
		f.close()
		print(colored.cyan('Files have been created'))

	

# when listen is used along with a filename, we listen for changes to that file 
# whenever someone saves a file, we need to take inputs from an input.txt for the 
# particular file, and then, 
# g++ filename.cpp -o filename
# ./filename < input 
# time ./filename
# show output on terminal 
# keep listening continuously till ctrl + z is used on terminal
# output should be : test case outputs, time for program , error in red.
def isModified(event):
	filename = os.path.basename(event.src_path)
	foldername = os.path.basename(os.getcwd())
	if filename != foldername and filename != "prog" and filename != "input.txt": 
		print(colored.yellow('\nChange made at '+ filename))
		print(colored.cyan('\nCompiling '+ filename))
		os.system('g++ ' + filename + ' -o ' + 'prog')
		print('Running')	
		print(colored.yellow('Taking inputs from input.txt'))
		os.system('./prog < input.txt')
	

	

def listen():
	print(colored.yellow("Getting files in directory"))
	path = os.getcwd()
	dircontents = os.listdir(path)
	if len(dircontents) != 0: 
		print(colored.magenta("Currently listening for file changes"))
		patterns = "*"
		ignore_patterns = ""
		ignore_directories = False
		case_sensitive = True
		event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
		event_handler.on_modified = isModified 
		observer = Observer()
		observer.schedule(event_handler,path,recursive=True)
		observer.start()
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			observer.stop()
		observer.join()
	else:
		print(colored.red("No files exist, check filename/path"))
	
def showHelp():
	print("           ---CODEMON---          ")
	print(colored.cyan("  a CLI tool for competitive coders"))
	print("\nCOMMANDS: \n")
	print("codemon - - - - - - - - - - - - - - - shows help")
	print("codemon init <contestName>  - - - - - initialises a contest")
	print("codemon listen - - - - - - - - - - -  compiles and gives output")

def main():
	if len(sys.argv) < 2:
		showHelp()
	else:	
		command = sys.argv[0]
		argument = sys.argv[1]
		if argument == "init":
			contestName = sys.argv[2]
			init(contestName)
		elif argument == "listen":
			listen()