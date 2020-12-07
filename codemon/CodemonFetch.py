import requests
import os
import itertools
from bs4 import BeautifulSoup as beSo
from clint.textui import colored
from codemon.CodemonMeta import get_filename

def make_structure(name, contestName):
  basedir = os.path.join(os.getcwd(), contestName)

  # Check if the question folder exists for the name passed if not make it.
  if not  os.path.exists(os.path.join(basedir, f'{name}')):
    os.makedirs(os.path.join(basedir, f'{name}'))

  # Check if input file exists for the given name if not make it. 
  if not os.path.exists(os.path.join(basedir, f'{name}',f'{name}.in')):
    open(os.path.join(basedir, f'{name}',f'{name}.in'), 'w').close()

  # Check if output file exists for the given name if not make it. 
  if not os.path.exists(os.path.join(basedir, f'{name}', f'{name}.op')):
    open(os.path.join(basedir, f'{name}', f'{name}.op'), 'w').close()


def fetch_tests(file_list, contestName):
  try:
    basedir = os.path.join(os.getcwd(), contestName)
    load_page = requests.get(f"https://codeforces.com/contest/{contestName}/problems")
    soup = beSo(load_page.content, 'html.parser')
    tests = soup.findAll("div", attrs={"class":"sample-tests"})

    if(len(tests) == 0):
      print(colored.red("Wrong contest number provided"))

    else:
      print(colored.green("Fetching sample test cases"))
      for file_name, test in zip(file_list, tests):
        # Make the neccesary folders and files for each source file if not present.
        make_structure(file_name, contestName)

        # Add  inputs to .in files
        for t in test.findAll("div", attrs={"class":"input"}):
          i = t.pre.text
          with open(os.path.join(basedir, f'{file_name}' , f'{file_name}.in'), 'a') as f:
            f.write(i)

        # Add outputs to .op files
        for t in test.findAll("div", attrs={"class":"output"}):
          o = t.pre.text
          with open(os.path.join(basedir, f'{file_name}' , f'{file_name}.op'), 'a') as f:
            f.write(o)

  # In case of any error with scraping, display warning.
  except:
    print(colored.red("There was some error fetching the tests !!"))




