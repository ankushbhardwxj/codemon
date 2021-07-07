import requests
import re
import os
import shutil
from bs4 import BeautifulSoup as beSo
from clint.textui import colored

# Check if the question folder exists for the name passed.
def checkStructure(name, basedir):
  status = True
  if not os.path.exists(os.path.join(basedir, f'{name}')) or not \
         os.path.exists(os.path.join(basedir, f'{name}',f'{name}.in')) or not \
         os.path.exists(os.path.join(basedir, f'{name}', f'{name}.op')):
      status = False
  return status

# scrape contest testcases 
def scrapeContestData(contestNumber):
  contestProblemsPage = requests.get(f"https://codeforces.com/contest/{contestNumber}/problems")
  soup = beSo(contestProblemsPage.content, "html.parser")
  testcases = soup.findAll("div", attrs={"class": "sample-tests"})
  return testcases

# write inputs and outputs to respective files
def writeToFile(fileName, testcase, basedir, classtype, ext):
  for test in testcase.findAll("div", attrs={"class": classtype}):
    contents = test.pre.contents
    with open(os.path.join(basedir, f'{fileName}', f'{fileName}.{ext}'), 'a') as f:
      for i in range(len(contents)):
        if str(contents[i]) in ('<br>', '<br/>'):
          if i == len(contents) - 1: f.write('\n\n')
          else: f.write('\n')
          continue
        f.write(contents[i][1:])
  return

# deletes the contest folder on error
def deleteContestFolder(path):
  try:
    shutil.rmtree(path)
  except OSError:
    print("Error deleting contest directory")

# fetches test cases from Codeforces by contest number lookup
def fetchTestcases(fileList, contestName):
  cwd = os.getcwd()
  if not os.path.basename(cwd) == contestName:
    basedir = os.path.join(cwd, contestName)
  else: basedir = cwd
  contestNumber = ''.join(re.findall(r'\d+', contestName))
  try:
    if not len(contestNumber):
      print(colored.red("Contest Number could not be parsed."))
      print("Please make sure to add contest number while creating a new contest folder")
      deleteContestFolder(basedir)
      return
    tests = scrapeContestData(contestNumber)
    if(len(tests) == 0):
      print(colored.red("Could not find this contest number on Codeforces."))
      print("Please check if the contest number given while creating contest is correct.")
      deleteContestFolder(basedir)
      return

    print("Fetching sample test cases...")

    for file_name, test in zip(fileList, tests):
      if(checkStructure(file_name, basedir)):
        writeToFile(file_name, test, basedir, 'input', 'in')
        writeToFile(file_name, test, basedir, "output", "op")
      else:
        print(colored.red(f"Failed to add sample testcases due to incorrect directory structure."))
        deleteContestFolder(basedir)
        break

    print("Successfully fetched sample testcases.")
  except:
    print(colored.red("Internal Error while fetching tests. Try again."))
    deleteContestFolder(basedir)
