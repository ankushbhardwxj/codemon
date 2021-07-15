import os
import shutil
import subprocess

def codemoncleantest():
  codemonInit = subprocess.Popen(['codemon', 'init', 'test'],
                 stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  codemonInit.wait()
  codemonClean = subprocess.Popen(['codemon', 'clean', 'test'],
                  stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  codemonClean.wait()
  cwd = os.getcwd()
  filePath = os.path.join(cwd, 'test')
  files = os.listdir(filePath)
  if len(files) == 7:
    shutil.rmtree("./test")
    return 0
  else: return 1

if __name__=="__main__":
  codemoncleantest()
