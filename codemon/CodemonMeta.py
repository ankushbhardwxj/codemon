import os
from clint.textui import colored
from datetime import datetime

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

def get_filename():
  fileNames = ['A','B','C','D','E','F']
  return fileNames

def get_practice_files():
  practiceFiles = ['A','B','C']
  return practiceFiles
