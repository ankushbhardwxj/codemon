import os
from clint.textui import colored
from codemon.CodemonMeta import Templates

def write_to_file(filename, text, contestName=None):
  full_filename = os.path.join(os.getcwd(), os.path.join(contestName, filename.split('.')[0]), filename)
  with open(full_filename, 'w+') as f:
    f.write(text)
  open(os.path.join(os.getcwd(),contestName, filename.split('.')[0], f"{filename.split('.')[0]}.in"), 'w').close()
  open(os.path.join(os.getcwd(),contestName, filename.split('.')[0], f"{filename.split('.')[0]}.op"), 'w').close()

# creates a directory for a contest
def init(contestName, fileNames, init_flags):
  try:
    os.makedirs(os.path.join(os.getcwd(), contestName))
    for f in fileNames:
      os.makedirs(os.path.join(os.getcwd(), contestName, f))
  except OSError:
    print(colored.red(f"Failed to create directory {contestName} !"))
  else:
    print(f"Created directory {contestName}")
    templates, ext, use_template = Templates(), None, None
    if init_flags["is_py"]:
        ext, use_template = "py", templates.get_custom_template("py") or templates.default_py()
    elif init_flags["is_java"]:
        ext, use_template = "java", templates.get_custom_template("java") or templates.default_java()
    elif init_flags["is_cpp"]:
        ext, use_template = "cpp", templates.get_custom_template("cpp") or templates.default_cpp()
    open(os.path.join(os.getcwd(), contestName, f"test_case"), 'w').close()
    with open(os.path.join(os.getcwd(), contestName, f"test_case.{ext}"), 'w') as f:
      f.write(testCaseTemplate)
      f.close()
    for files in fileNames:
      write_to_file(f"{files}.{ext}", use_template, contestName)

# creates a single file with given filename and template
def init_single_file(filename, init_flags):
  templates, ext, use_template = Templates(), None, None
  if init_flags["is_py"]:
    ext, use_template = "py", templates.get_custom_template("py") or templates.default_py()
  elif init_flags["is_java"]:
    ext, use_template = "java", templates.get_custom_template("java") or templates.default_java()
  elif init_flags["is_cpp"]:
    ext, use_template = "cpp", templates.get_custom_template("cpp") or templates.default_cpp()
  full_filename = os.path.join(os.getcwd(), f"{filename}.{ext}")
  with open(full_filename, 'w+') as f:
    f.write(use_template)
    f.close()
  print(f"Created file {filename}.{ext}")

# template for test_case.cpp
testCaseTemplate = """#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  return 0;
}
"""
