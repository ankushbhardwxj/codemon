import os
import sys
import time
from sys import platform as _platform
from clint.textui import colored
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

def listen():
  print(colored.yellow("Getting files in directory"))
  path = os.getcwd()
  dircontents = os.listdir(path)

  if len(dircontents) != 0:
    print(colored.magenta("Currently listening for file changes"))
    patterns = "*"
    ignore_patterns = ['prog', '*.exe']
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


def isModified(event):
  filename = os.path.basename(event.src_path)
  foldername = os.path.basename(os.getcwd())
  if filename != foldername and filename != "prog" and filename != "input.txt": 
    print(colored.yellow('\nChange made at '+ filename))
    print(colored.cyan('\nCompiling '+ filename))
    if os.system('g++ ' + filename + ' -o ' + 'prog') == 0:
        print('Running')	
        print(colored.yellow('Taking inputs from input.txt'))

        #Differentiating between different OS and running code accordingly.
        if _platform == "linux" or _platform == "linux2":
          # linux
          os.system('./prog < input.txt')
        elif _platform == "darwin":
          # MAC OS X
          os.system('./prog < input.txt')
        elif _platform == "win32":
          # Windows
          os.system('prog < input.txt')
        elif _platform == "win64":
          # Windows 64-bit
          os.system('prog < input.txt')

        print(colored.green('Changed CPP file compiled and run. Check output.'))
