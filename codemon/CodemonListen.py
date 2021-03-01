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
  def __init__(self, fileName, dirName):
    #self.src_file_path = os.path.join(os.getcwd(), filename.split('.')[0], filename)
    self.srcFilePath = os.path.join(dirName, fileName)
    self.testCaseFilePath = os.path.join(os.getcwd(), 'test_case')
    self.inputFilePath = os.path.join(dirName, f"{fileName.split('.')[0]}.in")
    self.outputFilePath = os.path.join(dirName, f"{fileName.split('.')[0]}.op")

  def get_inputs_and_outputs(self):
    user_in_list, sample_in_list, sample_out_list = [], [], []
    with open(self.user_in_file_path, 'r+', encoding='utf-8') as cin:
        #open(self.sample_in_file_path, 'r+', encoding='utf-8') as sin, \
        #open(self.sample_out_file_path, 'r+', encoding='utf-8') as sout:
      user_in_list = self.clean_file_content(cin.read())
      #sample_in_list = self.clean_file_content(sin.read())
      #sample_out_list = self.clean_file_content(sout.read())
    #return user_in_list, sample_in_list, sample_out_list
    return user_in_list

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
    # compiles the C++ program
    compilation_child_process = subprocess.Popen(['g++', self.src_file_path, 
      '-o', cpp_executable_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    compilation_child_process.wait()
    compilation_child_process.terminate()
    if compilation_child_process.returncode != 0:
      return_code = compilation_child_process.returncode
      if return_code == 127:
        print("'g++' isn't installed.", file=sys.stderr)
      return
    print('Running...')
    # Runs executable, with testcases
    #user_in_list, sample_in_list, sample_out_list = self.get_inputs_and_outputs()
    user_in_list = self.get_inputs_and_outputs()
    if user_in_list:
      print(colored.yellow("Taking inputs from test_case file"))
      for inp in user_in_list:
        execution_child_process = subprocess.Popen([cpp_executable_path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        execution_child_process.stdin.write(inp.encode(encoding='utf-8'))
        current_output = execution_child_process.communicate()
        if(len(current_output) > 0):
          self.display_output(current_output[0].decode())
        execution_child_process.terminate()
    else:
      print(colored.yellow("No input found."))
      print("Output: ")
      subprocess.run(f'{cpp_executable_path}')
    """
    elif sample_in_list and sample_out_list:
      print(colored.yellow("No custom input found."))
      print(colored.yellow("Running sample testcases."))
      for inp, outp in zip(sample_in_list, sample_out_list):
        execution_child_process = subprocess.Popen([cpp_executable_path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        execution_child_process.stdin.write(inp.encode(encoding='utf-8'))
        current_output = execution_child_process.communicate()
        if(len(current_output) > 0):
          self.display_output(current_output[0].decode(), outp)
        execution_child_process.terminate()
    """

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

  # Check for necessary files and create them
  def check_files(self):
    fName = os.path.basename(self.srcFilePath).split('.')[0]
    if len(fName) <= 1: 
      # if its a contest dir
      if not Path(self.srcFilePath).is_file():
        print("Cannot find source file to be compiled at {os.path.relpath(self.srcFilePath)}")
        return False
      if not Path(self.inputFilePath).is_file():
        print(f"Cannot find input file at {os.path.relpath(self.inputFilePath)}")
        print("Pro tip: If you're not playing a contest, init fileNames with length greater than 1 to avoid discrepancies.")
        return False
      if not Path(self.outputFilePath).is_file():
        print(f"Cannot find output file at {os.path.relpath(self.outputFilePath)}")
        return False
    else:
      # if its not a contest dir
      if not Path(self.srcFilePath).is_file():
        print("Cannot find source file to be compiled at {os.path.relpath(self.srcFilePath)}")
        return False
      if not Path(self.testCaseFilePath).is_file():
        print(f"Cannot find input file (test_case) at the current working directory.")
    return True

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

def isModified(event):
  modifiedFile = os.path.basename(event.src_path) 
  modifiedFileDirectory = os.path.dirname(event.src_path)
  execute = Runner(modifiedFile, modifiedFileDirectory)
  if execute.check_files():
    print(colored.yellow('\nChange made at '+ modifiedFile))
    """
    if(modifiedFile.split('.')[-1] == 'cpp'): execute.run_cpp()
    elif(modifiedFile.split('.')[-1] == 'py'): execute.run_py()
    """
    

def listen():
  print(colored.yellow("Getting files in directory"))
  path = os.getcwd()
  dircontents = os.listdir(path)
  if len(dircontents) != 0: 
    print(colored.magenta("Currently listening for file changes"))
    patterns = ['*.cpp', '*.py']
    ignore_patterns = ['prog', '*.exe', '*.swp']
    #ignore_directories = True # TODO : check otherwise
    case_sensitive = True
    event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, case_sensitive)
    event_handler.on_created = isModified 
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

