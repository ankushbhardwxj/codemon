import os
import subprocess
import sys
import time
from difflib import Differ
from pathlib import Path
from clint.textui import colored
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

class Runner:
  def __init__(self, fileName, dirName):
    self.srcFilePath = os.path.join(dirName, fileName)
    self.testCaseFilePath = os.path.join(os.getcwd(), 'test_case')
    self.inputFilePath = os.path.join(dirName, f"{fileName.split('.')[0]}.in")
    self.outputFilePath = os.path.join(dirName, f"{fileName.split('.')[0]}.op")

  def getProgramMetadata(self, typeOfDir):
    testCaseFile, inputFile, outputFile = [], [], [] 
    if typeOfDir == 'contest':
      with open(self.testCaseFilePath, 'r+', encoding='utf-8') as testCaseInput,\
          open(self.inputFilePath, 'r+', encoding='utf-8') as sampleInput,\
          open(self.outputFilePath, 'r+', encoding='utf-8') as sampleOutput:
        testCaseFile = self.clean_file_content(testCaseInput.read())
        inputFile = self.clean_file_content(sampleInput.read())
        outputFile = self.clean_file_content(sampleOutput.read())
    if typeOfDir == 'single':
      with open(self.testCaseFilePath, 'r+', encoding='utf-8') as testCaseInput:
        testCaseFile = self.clean_file_content(testCaseInput.read())
    return testCaseFile, inputFile, outputFile

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

  def compileTarget(self, executable):
    compiledProcess = subprocess.Popen(['g++', self.srcFilePath, '-o', executable], 
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    compiledProcess.wait()
    compiledProcess.terminate()
    return compiledProcess.returncode

  def runExec(self, executable, inp):
    execProcess = subprocess.Popen([executable], 
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    execProcess.stdin.write(inp.encode(encoding='utf-8'))
    return execProcess

  def run_cpp(self, typeOfDir):
    print(colored.cyan(f"Compiling {os.path.basename(self.srcFilePath)}..."))
    executable = os.path.join(os.getcwd(), 'prog')
    returnCode = self.compileTarget(executable)
    if returnCode != 0:
      if returnCode == 127:
        print(colored.red("'g++' isn't installed.", file=sys.stderr))
      return
    testCases, sampleInputs, sampleOutputs = self.getProgramMetadata(typeOfDir)
    if testCases:
      print(colored.yellow("Running inputs from test_case file..."))
      for inp in testCases:
        execTarget = self.runExec(executable, inp)
        execOutput = execTarget.communicate()
        if(len(execOutput) > 0): self.showOutput(execOutput[0].decode())
        execTarget.terminate()
    elif sampleInputs and sampleOutputs:
      print(colored.yellow("Running sample testcases..."))
      for inp, outp in zip(sampleInputs, sampleOutputs):
        execTarget = self.runExec(executable, inp)
        execOutput = execTarget.communicate()
        if(len(execOutput) > 0): self.showOutput(execOutput[0].decode(), outp)
        execTarget.terminate()
    else:
      print(colored.yellow("No input found."))
      print("Output: ")
      subprocess.run(f'{executable}')

  def run_py(self):
    python_interpreter = "python" if os.name == "nt" else "python3"
    testCases, sampleInputs, sampleOutputs = self.getProgramMetadata(typeOfDir)
    print("Running...")
    if testCases:
      print(colored.yellow("Taking inputs from test_case file"))
      for inp in testCases:
        execution_child_process = subprocess.Popen([python_interpreter, self.srcFilePath],
            stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        current_output, err = execution_child_process.communicate(input=inp.encode(encoding='utf-8'))
        if(execution_child_process.returncode != 0):
          print(err.decode())
          return
        if(current_output):
          self.display_output(current_output.decode())
        execution_child_process.terminate()
    elif sampleInputs and sampleOutputs:
      print(colored.yellow("No custom input found."))
      print(colored.yellow("Running sample testcases."))
      for inp, outp in zip(sampleInputs, sampleOutputs):
        execution_child_process = subprocess.Popen([python_interpreter, self.srcFilePath], 
            stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        current_output, err = execution_child_process.communicate(input=inp.encode(encoding='utf-8'))
        if(execution_child_process.returncode != 0):
          print(err.decode())
          return
        if(current_output):
          self.showOutput(current_output.decode(), outp)
        execution_child_process.terminate()
    else:
      print(colored.yellow("No input found."))
      print("Output: ")
      subprocess.run([python_interpreter, self.srcFilePath])

  def showOutput(self, output, *args):
    if args:
      output = ''.join(line.rstrip()+'\n' for line in output.splitlines())
      expected_output = ''.join(line.rstrip()+'\n' for line in args[0].splitlines())
      if(output == expected_output):
        print(colored.green(f"Sample testcase passed."))
        print(colored.yellow("Output:"))
        print(output)
      else:
        print(colored.red(f"Sample testcase failed !"))
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
      return (True, 'contest')
    else:
      if not Path(self.srcFilePath).is_file():
        print("Cannot find source file to be compiled at {os.path.relpath(self.srcFilePath)}")
        return False
      if not Path(self.testCaseFilePath).is_file():
        print(f"Cannot find input file (test_case) at the current working directory.")
        return False
      return (True, 'single')

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
  try:
    modifiedFile = os.path.basename(event.src_path) 
    modifiedFileDirectory = os.path.dirname(event.src_path)
    execute = Runner(modifiedFile, modifiedFileDirectory)
    fileCheckRes, typeOfDir = execute.check_files()
    if fileCheckRes:
      if(modifiedFile.split('.')[-1] == 'cpp'): execute.run_cpp(typeOfDir)
      elif(modifiedFile.split('.')[-1] == 'py'): execute.run_py(typeOfDir)
  except:
    print("Error in codemon listen. Check if you're in correct contest directory.")

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

