import os
from clint.textui import colored
from codemon.CodemonMeta import Templates

def write_to_file(filename, text, contestName=None):
  full_filename = os.path.join(os.getcwd(), os.path.join(contestName, filename.split('.')[0]), filename)
  with open(full_filename, 'w+') as f:
    f.write(text)
  open(os.path.join(os.getcwd(),contestName, filename.split('.')[0], f"{filename.split('.')[0]}.in"), 'w').close()
  open(os.path.join(os.getcwd(),contestName, filename.split('.')[0], f"{filename.split('.')[0]}.op"), 'w').close()

def init(contestName,fileNames, init_flags):
  # create a directory with contest name
  try:
    print(colored.green(f'Creating directories for {contestName}'))
    os.makedirs(os.path.join(os.getcwd(), contestName))
    for f in fileNames:
      os.makedirs(os.path.join(os.getcwd(), contestName, f))
  except OSError:
    print("Failed! This directory cannot be created.")
  else:
    print(colored.yellow('Directories are made.'))
    templates, ext, use_template = Templates(), None, None
    if init_flags["is_py"]:
        ext, use_template = "py", templates.get_custom_template("py") or templates.default_py()
    elif init_flags["is_java"]:
        ext, use_template = "java", templates.get_custom_template("java") or templates.default_java()
    elif init_flags["is_cpp"]:
        ext, use_template = "cpp", templates.get_custom_template("cpp") or templates.default_cpp()
    open(os.path.join(os.getcwd(), contestName, f"test_case"), 'w').close()
    open(os.path.join(os.getcwd(), contestName, f"test_case.{ext}"), 'w').close()
    for files in fileNames:
      write_to_file(f"{files}.{ext}", use_template, contestName)

def init_single_file(filename, init_flags):
  templates, ext, use_template = Templates(), None, None
  if init_flags["is_py"]:
    ext, use_template = "py", templates.get_custom_template("py") or templates.default_py()
  elif init_flags["is_java"]:
    ext, use_template = "java", templates.get_custom_template("java") or templates.default_java()
  elif init_flags["is_cpp"]:
    ext, use_template = "cpp", templates.get_custom_template("cpp") or templates.default_cpp()
  full_filename = os.path.join(os.getcwd(), f"{filename}.{ext}")
  print("Making single file")
  with open(full_filename, 'w+') as f:
    f.write(use_template)
  print(colored.yellow(f"Created {filename}.{ext}"))
