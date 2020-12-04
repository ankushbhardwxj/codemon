import os
import sys
import subprocess
from datetime import datetime

# template
now = datetime.now()
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

# runs codemon init -n test
print('Running command: "codemon init -n test"...')
codemonInit = subprocess.Popen(['codemon', 'init', '-n', 'test'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
codemonInit.wait()
#codemonInit.terminate()

# check if correct file is created & content matches to that of template
print('Validating file...')
if os.path.exists('test.cpp'):
  with open('test.cpp') as f:
    code = f.read()
    code = code[67:len(code)]
    template = template[67:len(template)]
    if code == template:
      print('Templates match !')
    else:
      print('No match !')

# clean the file
os.remove('./test.cpp')
print('Cleaned tests directory.')
    

