import os
import sys
import time
from clint.textui import colored
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from codemon.CodemonMeta import compile_and_run

def listen():
  print(colored.yellow("Getting files in directory"))
  path = os.getcwd()
  dircontents = os.listdir(path)
  if len(dircontents) != 0: 
    print(colored.magenta("Currently listening for file changes"))
    patterns = ['*.cpp']
    ignore_patterns = ['prog', '*.exe', '*.swp']
    ignore_directories = True
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
    print(colored.red("No files exist, check filename/path."))


def isModified(event):
  filename = os.path.basename(event.src_path)
  foldername = os.path.basename(os.getcwd())
  if filename != foldername and filename != "prog" and filename != "input.txt": 
    print(colored.yellow('\nChange made at '+ filename))
    print(colored.cyan('\nCompiling '+ filename))
    compile_and_run(filename)
