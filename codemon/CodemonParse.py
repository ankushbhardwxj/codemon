import re

# Parse all command line arguments and options.
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
    # No arguments provided
    if len(arg_list) == 0:
      self.help = True
      return
    # Extract all flags/option
    flags = list(map(lambda x: x.strip(), re.findall('.\-.\w*', " " + ' '.join(arg_list))))
    # Extract all non flag arguments
    arguments = [i for i in arg_list if i not in flags]

    for fl in flags:
      if fl == '-py':
        # error check: if two language flags present at the same time, show help.
        if "-java" in flags or "-cpp" in flags:
          self.help = True
          break
        self.init_flags["is_py"] = True
      elif fl == '-java':
        # error check: if two language flags present at the same time, show help.
        if "-py" in flags or "-cpp" in flags:
          self.help = True
          break
        self.init_flags["is_java"] = True
      elif fl == '-n':
        self.init_flags["is_single"] = True
      elif fl in ("-f", "--fetch"):
        self.init_flags["to_fetch"] = True
      elif fl == "--help":
        self.help = True

    for arg in arguments:
      # error check: if any other argument provided with listen show help.
      if arg == "listen":
        if(len(arguments) > 1):
          self.help = True
          break
        self.to_listen = True
      elif arg == "init":
        self.to_init = True
      # error check: if any other argument provided with reg show help.
      elif arg == "reg":
        if(len(arguments) > 1):
          self.help = True
          break
        self.Reg = True
      elif arg == "practice":
        self.to_practice = True
      elif arg == "fetch":
        if(len(arguments) > 1):
          self.help = True
          break
        self.to_fetch = True
      else:
        self.name += arg

