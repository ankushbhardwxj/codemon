import fire
import os
from clint.textui import colored

# init takes an input contest name and creates a directory
# with that name and creates 5 files. Also it copies content 
# from a template doc to each of the files.
def init(contestName):
	print(colored.green('Make some files and folders for ' + contestName));
	try:
		path = os.getcwd()
		os.mkdir(path + '/' + contestName)
	except OSError: 
		print("Failed! This directory already exists.")
	else:
		print(colored.blue('Directory is made'))

def listen(filename):
  print('listen to some file changes');

if __name__ == '__main__':
  fire.Fire({
    'init': init,
    'listen': listen
  })

