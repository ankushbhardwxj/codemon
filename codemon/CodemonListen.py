import os
from pathlib import Path
import subprocess
import sys
import time
from clint.textui import colored
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

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

def compile_and_run(filename):
  # Store full file paths
  full_filename = os.path.join(os.getcwd(), filename)
  full_output_filename = os.path.join(os.getcwd(), 'prog')
  full_input_filename = os.path.join(os.getcwd(), 'test_case')

  # Check if required files exist
  if not Path(full_filename).is_file():
    print(f"{filename} doesn't exist.", file=sys.stderr)
  if not Path(full_input_filename).is_file():
    print(f"'input.txt' doesn't exist.", file=sys.stderr)

  compilation_child_process = subprocess.Popen(['g++', full_filename, '-o', full_output_filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  compilation_child_process.wait()
  compilation_child_process.terminate()
  if compilation_child_process.returncode != 0:
    return_code = compilation_child_process.returncode
    if return_code == 127:
      print("'g++' isn't installed.", file=sys.stderr)
    return
  print('Running...')
  execution_child_process = subprocess.Popen([full_output_filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  input_text = ''
  with open(full_input_filename, 'r+', encoding='utf-8') as infile:
    input_text = infile.read()
  if len(input_text) > 0 and not input_text.isspace():
    print(colored.yellow('Taking input from test_case file.'))
    execution_child_process.stdin.write(input_text.encode(encoding='utf-8'))
  else:
    print(colored.yellow('Skipped fetching inputs as input file is empty.'))
  output = execution_child_process.communicate()
  if len(output) > 0:
    print(output[0].decode())
    print()
  execution_child_process.terminate()
