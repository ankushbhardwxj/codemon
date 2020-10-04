#!/usr/bin/python
import sys
import os
import time
import logging
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from clint.textui import colored
from datetime import datetime
# get the current time
now = datetime.now()
# the template for initial code
template = """/*
  author: @ankingcodes
  created: %s
*/
#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

#define ll long long
#define MOD 1000000000

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll t;
  return 0;
}
""" % (now)

fileNames = ['A.cpp','B.cpp','C.cpp','D.cpp','E.cpp','F.cpp']
practiceFiles = ['A.cpp','B.cpp','C.cpp']

def showHelp():
	print("           ---CODEMON---          ")
	print(colored.cyan("  a CLI tool for competitive coders"))
	print("\nCOMMANDS: \n")
	print("codemon - - - - - - - - - - - - - - - shows help")
	print("codemon init <contestName>  - - - - - initialises a contest")
	print("codemon init -n <file>  - - - - - - - creates file with given name")
	print("codemon listen  - - - - - - - - - - - compiles and gives output")
	print("codemon practice <dirName>  - - - - - starts a practice session")

def init(contestName,fileNames):
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
		for files in range(len(fileNames)):
			f = open(path + '/' + contestName + '/' + fileNames[files],"w+")
			f.write(template)
			f.close()
		# create input file
		f = open(path + '/' + contestName + '/' + "input.txt","w+")
		f.close()
		print(colored.cyan('Files have been created'))

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
	
def main():
	if len(sys.argv) < 2:
		showHelp()
	else:	
		countArg=0;
		for arg in sys.argv: 
			countArg+=1;
			if arg == "init": 
				if sys.argv[countArg] == '-n':
					file = sys.argv[countArg+1]
					path = '.'
					f = open(path + '/' + file + '.cpp',"w+")
					f.write(template)
					f.close()
					print(colored.yellow("Created "+file+'.cpp'))
					break;
				else:
					contestName = sys.argv[countArg]
					init(contestName, fileNames)
			elif arg == "listen":
				listen()
			elif arg == "practice": 
				contestName = sys.argv[countArg+1]
				init(contestName, practiceFiles)
		
