import requests
import os
from bs4 import BeautifulSoup as beSo
import itertools
from clint.textui import colored

def make_structure(name):
  basedir = os.getcwd()

  # Check if the question folder exists for the name passed if not make it.
  if not  os.path.exists(os.path.join(basedir, f'{name}')):
    os.makedirs(os.path.join(basedir, f'{name}'))

  # Check if input file exists for the given name if not make it. 
  if not  os.path.exists(os.path.join(basedir, os.path.join(f'{name}',f'{name}.in'))):
    open(os.path.join(f'{name}',f'{name}.in'), 'w').close()

  # Check if output file exists for the given name if not make it. 
  if not  os.path.exists(os.path.join(basedir, os.path.join(f'{name}', f'{name}.out'))):
    open(os.path.join(f'{name}', f'{name}.out'), 'w').close()


def fetch_tests(contest_name):
  try:
    load_page = requests.get(f"https://codeforces.com/contest/{contest_name}/problems")
    soup = beSo(load_page.content, 'html.parser')
    tests = soup.findAll("div", attrs={"class":"sample-tests"})
    name_list = ['A', 'B', 'C', 'D', 'E', 'F']

    for file_name, test in zip(name_list, tests):
      # Make the neccesary folders and files for each source file if not present.
      make_structure(file_name)

      # Add  inputs to .in files
      for t in test.findAll("div", attrs={"class":"input"}):
        i = t.pre.text
        with open(os.path.join(f'{file_name}' , f'{file_name}.in'), 'a') as f:
          f.write(i)

      # Add outputs to .out files
      for t in test.findAll("div", attrs={"class":"output"}):
        o = t.pre.text
        with open(os.path.join(f'{file_name}' , f'{file_name}.out'), 'a') as f:
          f.write(o)

  # In case of any error with scraping, display warning.
  except:
    print(colored.red("There was some error fetching the tests !!"))




