import requests
import re
import os
import itertools
from bs4 import BeautifulSoup as beSo
from clint.textui import colored

def check_structure(name, basedir):
  # Check if the question folder exists for the name passed.
  status = True
  if not os.path.exists(os.path.join(basedir, f'{name}')) or not \
         os.path.exists(os.path.join(basedir, f'{name}',f'{name}.in')) or not \
         os.path.exists(os.path.join(basedir, f'{name}', f'{name}.op')):
      status = False
  return status

def fetch_tests(file_list, contestName):
  try:
    basedir = os.path.join(os.getcwd(), contestName) if not os.path.basename(os.getcwd()) == contestName else os.getcwd()
    contest_number = ''.join(re.findall(r'\d+', contestName))
    if not len(contest_number):
        print(colored.red("Invalid contest number."))
        return
    load_page = requests.get(f"https://codeforces.com/contest/{contest_number}/problems")
    soup = beSo(load_page.content, 'html.parser')
    tests = soup.findAll("div", attrs={"class":"sample-tests"})
    if(len(tests) == 0):
      print(colored.red("Invalid contest number."))
    else:
      print("Fetching sample test cases...")
      for file_name, test in zip(file_list, tests):
        # Check if proper directory structure exists, if not generate error.
        correct_dir_structure = True
        if(check_structure(file_name, basedir)):
          # Add  inputs to .in files
          for t in test.findAll("div", attrs={"class":"input"}):
            i = t.pre.text
            with open(os.path.join(basedir, f'{file_name}' , f'{file_name}.in'), 'a') as f:
              f.write(i[1:])
          # Add outputs to .op files
          for t in test.findAll("div", attrs={"class":"output"}):
            o = t.pre.text
            with open(os.path.join(basedir, f'{file_name}' , f'{file_name}.op'), 'a') as f:
              f.write(o[1:])
        else:
          correct_dir_structure = False
          break
      print("Sample test cases added." if correct_dir_structure else 
            colored.red(f"Failed to add sample test cases: Incorrect directory structure !!"))
  # In case of any error with scraping, display warning.
  except:
    print(colored.red("There was some error fetching the tests !!"))




