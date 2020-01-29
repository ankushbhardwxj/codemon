import fire
import os
from clint.textui import colored

# init takes an input contest name and creates a directory
# with that name and creates 5 files. Also it copies content 
# from a template doc to each of the files.
template = '#include<iostream>\nusing namespace std;\n\nint main(){ \n\n	return 0; \n}'

def init(contestName):
	print(colored.green('Make some files and folders for ' + contestName));
	# create a directory with contest name
	try:
		path = os.getcwd()
		os.mkdir(path + '/' + contestName)
	except OSError: 
		print("Failed! This directory already exists.")
	else:
		print(colored.blue('Directory is made'))

		# create files for contest (should be 6 cpp files)
		fileNames = ['A.cpp','B.cpp','C.cpp','D.cpp','E.cpp','F.cpp']
		for files in range(len(fileNames)):
			f = open(path + '/' + contestName + '/' + fileNames[files],"w+")
			f.write(template)
			f.close()
		print(colored.blue('Files have been created'))

def listen(filename):
  print('listen to some file changes');
