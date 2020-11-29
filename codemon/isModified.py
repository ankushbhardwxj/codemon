import os
from clint.textui import colored

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