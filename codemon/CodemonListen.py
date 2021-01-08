import os
import subprocess
import sys
import time
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
  if filename not in (foldername, 'prog', 'input.txt'): 
    print(colored.yellow('\nChange made at '+ filename))
    print(colored.cyan('\nCompiling '+ filename))
    compile_and_run(filename)

def compile_and_run(filename):
  # Store full file paths
  full_filename = os.path.join(os.getcwd(), filename.split('.')[0], filename)
  full_output_filename = os.path.join(os.getcwd(), 'prog')
  full_input_filename = os.path.join(os.getcwd(), 'test_case')

  # Check if required files exist
  if not Path(full_filename).is_file():
    print(f"{filename} doesn't exist.", file=sys.stderr)
  if not Path(full_input_filename).is_file():
    print("'input.txt' doesn't exist.", file=sys.stderr)

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

import os
import subprocess
import sys
import time
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
  full_filename = os.path.join(os.getcwd(), filename)
  full_output_filename = os.path.join(os.getcwd(), 'prog')
  full_input_filename = os.path.join(os.getcwd(), 'test_case')
  print(f"fullinputfilename: {full_input_filename}\n")

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
=======
import os
import subprocess
import sys
import time
import itertools
from difflib import Differ
from pathlib import Path
from clint.textui import colored
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

class Runner:
  def __init__(self, filename):
    self.src_file_path = os.path.join(os.getcwd(), filename.split('.')[0], filename)
    self.user_in_file_path = os.path.join(os.getcwd(), 'test_case')
    self.sample_in_file_path = os.path.join(os.getcwd(), filename.split('.')[0], f"{filename.split('.')[0]}.in")
    self.sample_out_file_path = os.path.join(os.getcwd(), filename.split('.')[0], f"{filename.split('.')[0]}.op")

  def get_inputs_and_outputs(self):
    user_in_list, sample_in_list, sample_out_list = [], [], []
    with open(self.user_in_file_path, 'r+', encoding='utf-8') as cin, \
        open(self.sample_in_file_path, 'r+', encoding='utf-8') as sin, \
        open(self.sample_out_file_path, 'r+', encoding='utf-8') as sout:
      user_in_list = self.clean_file_content(cin.read())
      sample_in_list = self.clean_file_content(sin.read())
      sample_out_list = self.clean_file_content(sout.read())
    return user_in_list, sample_in_list, sample_out_list

  def clean_file_content(self, content):
    res, temp = [], []
    if len(content) == 0 or content.isspace():
      res = None
      return res
    check = content.splitlines()
    for i in range(len(check)):
      temp.append(check[i])
      if check[i] == '' or i == len(check)-1:
        if(temp == ['']):
          temp = []
          continue
        res.append('\n'.join(temp))
        temp = []
    return res

  def run_cpp(self):
    print(colored.cyan(f"Compiling {os.path.basename(self.src_file_path)}..."))
    cpp_executable_path = os.path.join(os.getcwd(), 'prog')
    compilation_child_process = subprocess.Popen(['g++', self.src_file_path, '-o', cpp_executable_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    compilation_child_process.wait()
    compilation_child_process.terminate()
    if compilation_child_process.returncode != 0:
      return_code = compilation_child_process.returncode
      if return_code == 127:
        print("'g++' isn't installed.", file=sys.stderr)
      return
    print('Running...')
    user_in_list, sample_in_list, sample_out_list = self.get_inputs_and_outputs()
    if user_in_list:
      print(colored.yellow("Taking inputs from test_case file"))
      for inp in user_in_list:
        execution_child_process = subprocess.Popen([cpp_executable_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        execution_child_process.stdin.write(inp.encode(encoding='utf-8'))
        current_output = execution_child_process.communicate()
        if(len(current_output) > 0):
          self.display_output(current_output[0].decode())
        execution_child_process.terminate()
    elif sample_in_list and sample_out_list:
      print(colored.yellow("No custom input found."))
      print(colored.yellow("Running sample testcases."))
      for inp, outp in zip(sample_in_list, sample_out_list):
        execution_child_process = subprocess.Popen([cpp_executable_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        execution_child_process.stdin.write(inp.encode(encoding='utf-8'))
        current_output = execution_child_process.communicate()
        if(len(current_output) > 0):
          self.display_output(current_output[0].decode(), outp)
        execution_child_process.terminate()
    else:
      print(colored.yellow("No input found."))
      print("Output: ")
      subprocess.run(f'{cpp_executable_path}')

  def run_py(self):
    python_interpreter = "python" if os.name == "nt" else "python3"
    user_in_list, sample_in_list, sample_out_list = self.get_inputs_and_outputs()
    print("Running...")
    if user_in_list:
      print(colored.yellow("Taking inputs from test_case file"))
      for inp in user_in_list:
        execution_child_process = subprocess.Popen([python_interpreter, self.src_file_path], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        current_output, err = execution_child_process.communicate(input=inp.encode(encoding='utf-8'))
        if(execution_child_process.returncode != 0):
          print(err.decode())
          return
        if(current_output):
          self.display_output(current_output.decode())
        execution_child_process.terminate()
    elif sample_in_list and sample_out_list:
      print(colored.yellow("No custom input found."))
      print(colored.yellow("Running sample testcases."))
      for inp, outp in zip(sample_in_list, sample_out_list):
        execution_child_process = subprocess.Popen([python_interpreter, self.src_file_path], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        current_output, err = execution_child_process.communicate(input=inp.encode(encoding='utf-8'))
        if(execution_child_process.returncode != 0):
          print(err.decode())
          return
        if(current_output):
          self.display_output(current_output.decode(), outp)
        execution_child_process.terminate()
    else:
      print(colored.yellow("No input found."))
      print("Output: ")
      subprocess.run([python_interpreter, self.src_file_path])

  def display_output(self, output, *args):
    if args:
      output = ''.join(line.rstrip()+'\n' for line in output.splitlines())
      expected_output = ''.join(line.rstrip()+'\n' for line in args[0].splitlines())
      if(output == expected_output):
        print(colored.green(f"Sample testcase passed."))
        print()
        print(colored.yellow("Output:"))
        print(output)
      else:
        print(colored.red(f"Sample testcase failed !"))
        print()
        print(colored.yellow("Output:"))
        print(output)
        print(colored.yellow("Changes needed:"))
        diff = Differ()
        diffed_output = self.color_diff(diff.compare(output.splitlines(), expected_output.splitlines()))
        print('\n'.join(diffed_output))
    else:
      print(colored.yellow(f"Output: "))
      print(output)

  def check_files(self):
    # Check if required files exist
    status = True
    if not Path(self.src_file_path).is_file():
      print(colored.red(f"{filename} doesn't exist !"), file=sys.stderr)
      status = False
    if not Path(self.user_in_file_path).is_file():
      print(colored.red(f"User input file doesn't exist !"), file=sys.stderr)
      status = False
    if not Path(self.sample_in_file_path).is_file():
      print(colored.red(f"Sample input file doesn't exist !"), file=sys.stderr)
      status = False
    if not Path(self.sample_out_file_path).is_file():
      print(colored.red(f"Sample output file doesn't exist !"), file=sys.stderr)
      status = False
    return status

  def color_diff(self, diff):
    for line in diff:
      if line.startswith('+'):
        yield str(colored.green(line))
      elif line.startswith('-'):
        yield str(colored.red(line))
      elif line.startswith('?'):
        yield str(colored.blue(line))
      else:
        yield line

def listen():
  print(colored.yellow("Getting files in directory"))
  path = os.getcwd()
  dircontents = os.listdir(path)
  if len(dircontents) != 0: 
    print(colored.magenta("Currently listening for file changes"))
    patterns = ['*.cpp', '*.py']
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
  execute = Runner(filename)
  if execute.check_files() and filename not in (foldername, "prog", "test_case"):
    print(colored.yellow('\nChange made at '+ filename))
    if(filename.split('.')[-1] == 'cpp'):
      execute.run_cpp()
    elif(filename.split('.')[-1] == 'py'):
      execute.run_py()
                                             