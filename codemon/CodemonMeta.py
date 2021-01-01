import re
import os
import json
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
from os import path
from io import BytesIO, IOBase
import sys
from heapq import heappush,heappop
from functools import cmp_to_key as ctk
from collections import deque,Counter,defaultdict as dd 
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input().rstrip()
def mi():return map(int,input().split())
def li():return list(mi())
# mod=1000000007
mod=998244353
inf = float("inf")
file = 1
 
# write fastio for getting fastio template.
    
 
def solve():
 
 
    # Your Solution


        
if __name__ =="__main__":
 
    if(file):
 
        if path.exists('input.txt'):
            sys.stdin=open('input.txt', 'r')
            sys.stdout=open('output.txt','w')
        else:
            input=sys.stdin.readline
    solve()
   """ % (now)
    return template

  def default_java(self):
    now = datetime.now()
    template ="""
/*
  author: @ankingcodes
  created: %s
*/

import java.util.*;
import java.io.*;
import java.math.*;

// Rename the class as needed
class Solution {
  public static void main(String[] args) throws Exception {
    Scanner in = new Scanner(System.in);
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    in.close();
    br.close();
  }
}
""" % (now)
    return template

  def get_custom_template(self, ext):
    template = None
    home = os.path.expanduser("~")
    username = ''
    metafile = 'meta.json'
    if(os.path.exists(os.path.join(home, ".codemon"))):
      for file in os.listdir(os.path.join(home, ".codemon")):
        if(file == metafile):
          with open(os.path.join(home, '.codemon', metafile), 'r') as f:
            data = json.load(f)
            username = '@' + data['codeforces_username']
        if(file.split('.')[-1] == ext):
          with open(os.path.join(home, ".codemon", file), 'r') as f:
            template = f.read()
    now = datetime.now()
    
    header = """/*
  author: %s
  created: %s
*/\n""" % (username, now)
    template = header + template
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
