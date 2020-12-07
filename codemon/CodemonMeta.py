import re
import os
from clint.textui import colored
from datetime import datetime
import requests
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

int main(){
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
# Write your code here
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


def get_filename(contesName):
  fileNames = []
  contest_number = ''.join(re.findall(r'\d+', contesName))
  # In case contest number is not there, initialize a generic A, B, C, D, E, F
  if(not len(contest_number)):
    fileNames = ['A','B','C','D','E','F', 'G']
  else:
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

  return fileNames

def get_practice_files():
  practiceFiles = ['A','B','C']
  return practiceFiles
