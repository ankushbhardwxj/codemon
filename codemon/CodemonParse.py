import re

class Parser:
  def __init__(self):
    self.to_listen = False
    self.help = False
    self.to_practice = False
    self.to_init = False,
    self.init_flags = {
      "is_single": False,
      "is_cpp":True,
      "is_java":False,
      "is_py":False,
      "to_fetch":False
    }
    self.to_fetch = False
    self.Reg = False
    self.clean = False
    self.Err = False
    self.name = ""

  def parse(self, arg_list):
    if len(arg_list) == 0:
      self.help = True
      return
    # Extract all flags/option
    flags = list(map(lambda x: x.strip(), re.findall('.\-.\w*', " " + ' '.join(arg_list))))
    # Extract all non flag arguments
    arguments = [i for i in arg_list if i not in flags]

    # flags for languages
    for fl in flags:
      if fl == '-py':
        if checkMultipleLangFlags(fl, '-java', '-cpp', flags):
          self.Err = True
          break
        self.init_flags["is_py"] = True
      elif fl == '-java':
        if checkMultipleLangFlags(fl, '-py', '-cpp', flags):
          self.Err = True
          break
        self.init_flags["is_java"] = True
      elif fl == '-n':
        self.init_flags["is_single"] = True
      elif fl in ("-f", "--fetch"):
        self.init_flags["to_fetch"] = True
      elif fl == "--help":
        self.help = True

    # arg parsing for commands
    for arg in arguments:
      if arg == "listen":
        if checkExtraArgs(arg, arguments) == True:
          self.Err = True
          break
        self.to_listen = True
      elif arg == "init":
        self.to_init = True
      elif arg == "reg":
        if checkExtraArgs(arg, arguments) == True:
          self.Err = True
          break
        self.Reg = True
      elif arg == "practice":
        self.to_practice = True
      elif arg == "clean":
        self.clean = True
      elif arg == "fetch":
        if checkExtraArgs(arg, arguments) == True:
          self.Err = True
          break
        self.to_fetch = True
      else:
        self.name += arg

# error check for multiple extension flags used together
def checkMultipleLangFlags(actualFlag, flag1, flag2, flags):
  if flag1 in flags:
    print(f"Codemon cannot create a file with both {actualFlag.replace('-', '.')} and {flag1.replace('-','.')} extensions.")
    print("Please use a single flag for the file extension.")
    return True
  elif flag2 in flags:
    print(f"Codemon cannot create a file with both {actualFlag.replace('-', '.')} and {flag2.replace('-','.')} extensions.")
    print("Please use a single flag for the file extension.")
    return True
  return False

# error check for extra arguments used
def checkExtraArgs(cmd, args):
  if len(args) > 1:
    print(f"Cannot use additional arguments with '{cmd}'. Try using 'codemon {cmd}'.")
    return True
  return False
