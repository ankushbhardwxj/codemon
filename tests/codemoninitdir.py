import os
import sys
import subprocess
import shutil

def codemoninitdir():
  try:
    print("Running command: 'codemon init test'")
    codemonInit = subprocess.Popen(['codemon', 'init', 'test'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    codemonInit.wait()

    print("Validating files...")
    if os.path.exists("./test"): print("Test dir found")
    if len(os.listdir("./test")) == 9: print("All files found")
    shutil.rmtree("./test")
    return 0
  except:
    return 1


if __name__=="__main__":
  codemoninitdir()
