import os
from clint.textui import colored
from codemon.CodemonMeta import Templates

# helper to create contest directory
def createContestDir(contestName, fileNames):
  try:
    cwd = os.getcwd()
    dirPath = os.path.join(cwd, contestName)
    os.makedirs(dirPath)
    for file in fileNames:
      filePath = os.path.join(cwd, contestName, file)
      os.makedirs(filePath)
  except OSError:
    print(colored.red(f"Failed to create directory {contestName}. "))
    print("Check if contest directory already exists")

# write content to target files
def writeToFiles(fileLoader):
  for file in fileLoader:
    with open(file["path"], "w+") as f:
      f.write(file["content"])
      f.close()

# get template and file extension
def getTemplatesMetadata(initFlags):
  ext, templateContent =  None, None
  if initFlags["is_py"]:
    ext = "py"
    templateContent = Templates().get_custom_template("py") or Templates().default_py()
  elif initFlags["is_java"]:
    ext = "java"
    templateContent = Templates().get_custom_template("java") or Templates().default_java()
  elif initFlags["is_cpp"]:
    ext = "cpp"
    templateContent = Templates().get_custom_template("cpp") or Templates().default_cpp()
  return ext, templateContent

# helper to create contest files
def createContestFiles(contestName, fileNames, initFlags):
  ext, templateContent = getTemplatesMetadata(initFlags)
  fileLoader = []
  cwd = os.getcwd()
  testCaseFile = os.path.join(cwd, contestName, f"test_case")
  testCaseProgramFile = os.path.join(cwd, contestName, f"test_case.{ext}")
  fileLoader.append({ "path": testCaseFile, "content": "" })
  fileLoader.append({ "path": testCaseProgramFile, "content": templateContent })
  for file in fileNames:
    fileName = f"{file}.{ext}"
    path = os.path.join(cwd, os.path.join(contestName, file), fileName)
    fileLoader.append({ "path": path, "content": templateContent })
    inpFileName = f"{file}.in"
    path = os.path.join(cwd, os.path.join(contestName, file), inpFileName)
    fileLoader.append({ "path": path, "content": "" })
    opFileName = f"{file}.op"
    path = os.path.join(cwd, os.path.join(contestName, file), opFileName)
    fileLoader.append({ "path": path, "content": "" })
  writeToFiles(fileLoader)

# creates a directory for a contest
def init(contestName, fileNames, init_flags):
  createContestDir(contestName, fileNames)
  createContestFiles(contestName, fileNames, init_flags)
  print(f"Initialized directory for {contestName}.")

# creates a single file with given filename and template
def init_single_file(filename, init_flags):
  ext, templateContent = getTemplatesMetadata(init_flags)
  path = os.path.join(os.getcwd(), f"{filename}.{ext}")
  writeToFiles([{ "path": path, "content": templateContent }])
  print(f"Created file {filename}.{ext}")

