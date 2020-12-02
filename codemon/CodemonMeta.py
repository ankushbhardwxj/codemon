import os
from pathlib import Path
import subprocess
import sys
from clint.textui import colored
from datetime import datetime

def template_cpp():
  # get the current time
  now = datetime.now()
  # the template for initial code
  template = """/*
  author: @ankingcodes
  created: %s
*/
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

#define ll long long
#define MOD 1000000000

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll t;
  return 0;
}
""" % (now)

  return template


def get_filenames():
  fileNames = ['A.cpp','B.cpp','C.cpp','D.cpp','E.cpp','F.cpp']
  return fileNames

def get_practice_files():
  practiceFiles = ['A.cpp','B.cpp','C.cpp']
  return practiceFiles

def write_to_file(filename, text, contestName=None):
  full_filename = os.path.join(os.getcwd(), filename)
  if contestName is not None:
    full_filename = os.path.join(os.getcwd(), contestName, filename)
  with open(full_filename, 'w+') as f:
    f.write(text)

def compile_and_run(filename):
  # Store full file paths
  full_filename = os.path.join(os.getcwd(), filename)
  full_output_filename = os.path.join(os.getcwd(), 'prog')
  full_input_filename = os.path.join(os.getcwd(), 'input.txt')

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
    else:
      print('Error in compilation.', file=sys.stderr)
      print(f'Return code: {return_code}', file=sys.stderr)
    return
  print('Running...')
  execution_child_process = subprocess.Popen([full_output_filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  input_text = ''
  with open(full_input_filename, 'r', encoding='utf-8') as infile:
    input_text = infile.read()
  if len(input_text) > 0 and not input_text.isspace():
    print(colored.yellow('Taking input from input.txt.'))
    execution_child_process.stdin.write(input_text.encode(encoding='utf-8'))
    execution_child_process.stdin.close()
  else:
    print(colored.yellow('input.txt is empty.\nSkipping input.'))
  output = execution_child_process.communicate()
  if len(output) > 0:
    print(colored.green(output[0].decode()))
    print()
  else:
    print(colored.red('No output.'))
  execution_child_process.terminate()
  print(f'Programme returned {execution_child_process.returncode}.')