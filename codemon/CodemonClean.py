import os
import shutil

# cleans unnecessary items from contest directory
def codemonClean(dirName):
  try:
    cwd = os.getcwd()
    contestDirPath = os.path.join(cwd, dirName)
    files = os.listdir(contestDirPath)
    for file in files:
      filePath = os.path.join(contestDirPath, file)
      if os.path.isdir(filePath):
        items = os.listdir(filePath)
        # rm -rf A/A.in A/A.op ...
        for item in items:
          itemPath = os.path.join(filePath, item)
          itemExt = itemPath.lower().endswith(('.cpp', '.py', '.java'))
          if itemExt:
            shutil.move(itemPath, contestDirPath)
          else:
            os.remove(itemPath)
        shutil.rmtree(filePath)
      # rm -rf test_case.cpp test_case
      if os.path.isfile(filePath):
        itemExt = filePath.lower().endswith(('.cpp', '.py', '.java'))
        if itemExt:
          item = os.path.basename(filePath)
          if item.startswith("test_case"):
            os.remove(filePath)
        else:
          os.remove(filePath)
    print(f"Successfully cleaned {dirName}.")
  except:
    print("Error cleaning contest directory. Try again")
