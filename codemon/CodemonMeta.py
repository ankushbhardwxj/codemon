import re
import os
import requests
from clint.textui import colored
from datetime import datetime
from bs4 import BeautifulSoup as beSo

class Templates:

  def default_cpp(self):
    # get the current time
    now = datetime.now()
    # the template for initial code
    template ="""
/*
 author: @ankingcodes
 created: %s
*/
#include<bits/stdc++.h>
#include<algorithm>
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

  def default_py(self):
    now = datetime.now()
    template="""
# author: @ankingcodes
# created: %s
import sys
input = sys.stdin.readline

#integer inputs
def inp():
    return(int(input()))
#list inputs
def inlt():
    return(list(map(int,input().split())))
#string inputs(returns as list of characters)
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
#space seperated integer inputs
def invr():
    return(map(int,input().split()))

#start coding from here
   """ % (now)
    return template

  def default_java(self):
    now = datetime.now()
    template ="""
// author: @ankingcodes
// created: %s
// Write your code here
""" % (now)
    return template

  def get_custom_template(self, ext):
    template = None
    home = os.path.expanduser("~")
    if(os.path.exists(os.path.join(home, ".codemon"))):
      for file in os.listdir(os.path.join(home, ".codemon")):
        if(file.split('.')[-1] == ext):
          with open(os.path.join(home, ".codemon", file), 'r') as f:
            template = f.read()
    return template


def get_filename(contestName):
  fileNames = []
  contest_number = ''.join(re.findall(r'\d+', contestName))
  # In case contest number is not there, initialize a generic A, B, C, D, E, F
  if(not len(contest_number)):
    fileNames = ['A','B','C','D','E','F', 'G']
  else:
    try:
      page = requests.get(f"https://codeforces.com/contest/{contest_number}/problems")
      soup = beSo(page.content, 'html.parser')
      titles = soup.findAll("div", attrs={"class":"title"})
      if titles[0].a:
        # In case contest number is wrong, initialize a generic A, B, C, D, E, F
        fileNames = ['A','B','C','D','E','F','G']
      else:
        # Scrape Codeforces problem page and get the exact problem names
        for t in titles:
          if '.' in t.text:
            fileNames.append(f"{t.text.split('.')[0]}")
    # In case of an error initialize default directory.
    except:
      fileNames = ['A','B','C','D','E','F', 'G']
  return fileNames

def get_practice_files():
  practiceFiles = ['A','B','C']
  return practiceFiles
