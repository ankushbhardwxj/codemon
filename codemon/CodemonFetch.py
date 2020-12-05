import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as beSo
import itertools
from clint.textui import colored
from codemon.CodemonMeta import get_filename

def make_structure(name):
  basedir = os.getcwd()

  # Check if the question folder exists for the name passed if not make it.
  if not  os.path.exists(os.path.join(basedir, f'{name}')):
    os.makedirs(os.path.join(basedir, f'{name}'))

  # Check if input file exists for the given name if not make it. 
  if not  os.path.exists(os.path.join(basedir, os.path.join(f'{name}',f'{name}.in'))):
    open(os.path.join(f'{name}',f'{name}.in'), 'w').close()

  # Check if output file exists for the given name if not make it. 
  if not  os.path.exists(os.path.join(basedir, os.path.join(f'{name}', f'{name}.op'))):
    open(os.path.join(f'{name}', f'{name}.op'), 'w').close()


def fetch_tests(contest_name):
  try:
    load_page = requests.get(f"https://codeforces.com/contest/{contest_name}/problems")
    soup = beSo(load_page.content, 'html.parser')
    tests = soup.findAll("div", attrs={"class":"sample-tests"})

    if(len(tests) == 0):
      print(colored.red("Wrong contest number provided"))

    else:
      # Get the file names to scrape test cases for.
      file_list = list(map(lambda x: x.split('.')[0], get_filename(contest_name)))
      for file_name, test in tqdm(zip(file_list, tests), unit="ticks", desc="Fetching Sample test cases", 
                                  total=len(tests)):
        # Make the neccesary folders and files for each source file if not present.
        make_structure(file_name)

        # Add  inputs to .in files
        for t in test.findAll("div", attrs={"class":"input"}):
          i = t.pre.text
          with open(os.path.join(f'{file_name}' , f'{file_name}.in'), 'a') as f:
            f.write(i)

        # Add outputs to .op files
        for t in test.findAll("div", attrs={"class":"output"}):
          o = t.pre.text
          with open(os.path.join(f'{file_name}' , f'{file_name}.op'), 'a') as f:
            f.write(o)

  # In case of any error with scraping, display warning.
  except:
    print(colored.red("There was some error fetching the tests !!"))




