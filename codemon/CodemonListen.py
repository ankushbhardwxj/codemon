import os
import subprocess
import sys
import time
from difflib import Differ
from pathlib import Path
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
  if filename != foldername and filename != "prog" and filename != "test_case": 
    print(colored.yellow('\nChange made at '+ filename))
    print(colored.cyan('\nCompiling '+ filename))
    compile_and_run(filename)

def compile_and_run(filename):
  # Store full file paths
  full_filename = os.path.join(os.getcwd(), filename.split('.')[0], filename)
  full_output_filename = os.path.join(os.getcwd(), 'prog')
  full_input_filename = os.path.join(os.getcwd(), 'test_case')
  sample_test_case_file = os.path.join(os.getcwd(), filename.split('.')[0], f"{filename.split('.')[0]}.in")
  sample_output_file = os.path.join(os.getcwd(), filename.split('.')[0], f"{filename.split('.')[0]}.op")

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
  sample_input = ''
  sample_output = ''
  with open(full_input_filename, 'r+', encoding='utf-8') as infile:
    input_text = infile.read()
  with open(sample_test_case_file, 'r+', encoding='utf-8') as infile:
    sample_input = infile.read()
  with open(sample_output_file, 'r+', encoding='utf-8') as outfile:
    sample_output = outfile.read()
  if len(input_text) > 0 and not input_text.isspace():
    print(colored.yellow('Taking input from test_case file.'))
    execution_child_process.stdin.write(input_text.encode(encoding='utf-8'))
    output = execution_child_process.communicate()
    if len(output) > 0:
      print()
      print(colored.yellow("Output:"))
      print(output[0].decode())
    return
  elif len(sample_input) > 0 and not sample_input.isspace():
    print(colored.yellow('No custom input found.'))
    print("Running sample test cases...")
    execution_child_process.stdin.write(sample_input.encode(encoding='utf-8'))
  else:
    print(colored.yellow("No input found."))
  output = execution_child_process.communicate()
  if len(output) > 0:
    if(output[0].decode() == sample_output):
      print()
      print(colored.green("Sample test case passed."))
      print()
      print(colored.yellow("Output:"))
      print(output[0].decode())
    else:
      print()
      print(colored.red("Sample test case failed !"))
      print()
      print(colored.yellow("Output:"))
      print(output[0].decode())
      print(colored.yellow("Changes needed to pass testcase:"))
      diff = Differ()
      diffed_output = color_diff(diff.compare(output[0].decode().splitlines(), sample_output.splitlines()))
      print('\n'.join(diffed_output))
  execution_child_process.terminate()


def color_diff(diff):
  for line in diff:
    if line.startswith('+'):
      yield str(colored.green(line))
    elif line.startswith('-'):
      yield str(colored.red(line))
    elif line.startswith('?'):
      yield str(colored.blue(line))
    else:
      yield line
