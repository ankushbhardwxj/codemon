import re
from tqdm import tqdm
from clint.textui import colored
from datetime import datetime
import requests
from bs4 import BeautifulSoup as beSo

def template_cpp():
  # get the current time
  now = datetime.now()
  # the template for initial code
  template = """/*
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


def get_filename(contesName):
  fileNames = []
  contest_number = ''.join(re.findall(r'\d+', contesName))
  # In case contest number is not there, initialize a generic A, B, C, D, E, F
  if(not len(contest_number)):
    fileNames = ['A.cpp','B.cpp','C.cpp','D.cpp','E.cpp','F.cpp']
  else:
    page = requests.get(f"https://codeforces.com/contest/{contest_number}/problems")
    soup = beSo(page.content, 'html.parser')
    titles = soup.findAll("div", attrs={"class":"title"})
    if titles[0].a:
      # In case contest number is wrong, initialize a generic A, B, C, D, E, F
      fileNames = ['A.cpp','B.cpp','C.cpp','D.cpp','E.cpp','F.cpp']
    else:
      # Scrape Codeforces problem page and get the exact problem names
      for t in titles:
        if '.' in t.text:
          fileNames.append(f"{t.text.split('.')[0]}.cpp")

  return fileNames

def get_practice_files():
  practiceFiles = ['A.cpp','B.cpp','C.cpp']
  return practiceFiles
