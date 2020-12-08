# Parse all command line arguments and options.
import re


class Parser:

  def __init__(self):
    self.to_listen = False
    self.help = False
    self.to_practice = False
    self.to_init, self.init_flags = False, { "is_single": False, "is_cpp":True,
                                             "is_java":False, "is_py":False,
                                             "to_fetch":False }
    self.to_fetch = False
    self.Reg = False
    self.name = ""

  def parse(self, arg_list):
    countArg = 0

    # No arguments provided
    if len(arg_list) == 0:
      self.help = True

    # Extract all flags/option
    flags = list(map(lambda x: x.strip(), re.findall('.\-.\w*', " " + ' '.join(arg_list))))

    # Extract all non flag arguments
    arguments = [i for i in arg_list if i not in flags]

    for fl in flags:
      if fl == '-py':
        self.init_flags["is_py"] = True
      elif fl == '-java':
        self.init_flags["is_java"] = True
      elif fl == '-n':
        self.init_flags["is_single"] = True
      elif fl in ("-f", "--fetch"):
        self.init_flags["to_fetch"] = True
      elif fl == "--help":
        self.help = True

    for a in arguments:

      if a == "listen":
        self.to_listen = True

      elif a == "init":
        self.to_init = True

      elif a == "reg":
        self.Reg = True

      elif a == "practice":
        self.to_practice = True

      elif a == "fetch":
        self.to_fetch = True

      else:
        self.name += a

