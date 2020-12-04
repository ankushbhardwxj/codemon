import os
from clint.textui import colored
from datetime import datetime

def copy_template(filepath):
  with open(filepath) as fp:
    line = fp.readline()
    stringArr = []
    while line:
      stringArr.append(line.strip())
      line = fp.readline()
    return "\n".join(stringArr)


def template_exists(directory):
  for filename in os.listdir(directory):
    if filename == "template.cpp":
      return True
  return False

def template_cpp():
  # get the current time
  # now = datetime.now()
  # the template for initial code
  template = """
    #include<bits/stdc++.h>
    using namespace std;

    int main() {
  
      return 0;
  
    }
  """

  if(template_exists(os.getcwd())):
    template = copy_template(os.path.join(os.getcwd(), "template.cpp"))
  
  return template


def get_filename():
  fileNames = ['A','B','C','D','E','F']
  return fileNames

def get_practice_files():
  practiceFiles = ['A','B','C']
  return practiceFiles
