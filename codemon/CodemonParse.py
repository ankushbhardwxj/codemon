import re

class Parser:
  def __init__(self):
    self.help = False
    self.init = False
    self.listen = False
    self.fetch = False
    self.clean = False
    self.register = False
    self.contestName = ""
    self.initFlags = {
      "single": False,
      "cpp": True,
      "java": False,
      "py": False,
      "fetch": False
    }
    self.name = ""
    self.error = ""

  def parse(self, arg_list):
    if len(arg_list) == 0:
      self.help = True
      return
    # Extract all flags/option
    flags = list(map(lambda x: x.strip(), re.findall('.\-.\w*', " " + ' '.join(arg_list))))
    # Extract all non flag arguments
    arguments = [i for i in arg_list if i not in flags]

    # flags for languages
    for flag in flags:
      if flag == "-h" or flag == "--help": self.help = True
      elif flag == "-f" or flag == "--fetch": self.initFlags["fetch"] = True
      elif flag == "-n": self.initFlags["single"] = True
      elif flag == "-py": self.initFlags["py"] = True
      elif flag == "-java": self.initFlags["java"] = True
      else: self.error = f'Incorrect Flag "{flag}" used. Type "codemon -h" for help.'

    cmdArr = ["init", "listen", "reg", "clean", "fetch"]
    # arg parsing for commands
    for arg in arguments:
      if arg == "init": self.init = True
      elif arg == "listen": self.listen = True
      elif arg == "reg": self.register = True
      elif arg == "clean": self.clean = True
      elif arg == "fetch": self.fetch = True
      elif arg not in cmdArr and len(self.name) == 0: self.name = arg
      else: self.error = f'Invalid command {arg}. Type "codemon -h" for help.'

# error check for multiple extension flags used together
def checkMultipleLangFlags(currflag, flag1, flag2, flagsArr):
  if flag1 in flagsArr:
    print(f"Codemon cannot create a file with both {currflag.replace('-', '.')} and {flag1.replace('-','.')} extensions.")
    print("Please use a single flag for the file extension.")
    return True
  elif flag2 in flagsArr:
    print(f"Codemon cannot create a file with both {currflag.replace('-', '.')} and {flag2.replace('-','.')} extensions.")
    print("Please use a single flag for the file extension.")
    return True
  return False

# error check for extra arguments used
def checkExtraArgs(cmd, args):
  if len(args) > 1:
    print(f"Cannot use additional arguments with '{cmd}'. Try using 'codemon {cmd}'.")
    return True
  return False
