# Parse all command line arguments and options.


class Commands:
  def __init__(self):
    self.to_listen = False
    self.help = False
    self.to_practice = False
    self.to_init, self.init_flags = False, { "is_single": False, "is_cpp":True,
                                             "is_java":False, "is_py":False,
                                             "to_fetch":False }
    self.single_file_name = ""
    self.contest_name = ""

  def parse(self, arg_list):
    countArg = 0

    # No arguments provided
    if len(arg_list) == 0:
      self.help = True

    # One argument commands.
    elif len(arg_list) == 1:
      if arg_list[countArg] == "listen":
        self.to_listen = True
      elif arg_list[countArg] == "practice":
        self.to_practice = True
      elif arg_list[countArg] == "--help":
        self.help = True

    # Commands with several arguments, options or flags.
    else:
      if(arg_list[countArg] == "init"):
        self.to_init = True
        if(arg_list[countArg+1] == "-n"):
          self.init_flags["is_single"] = True
          self.single_file_name += arg_list[countArg + 2]
          if len(arg_list[2:]) == 2:
            if(arg_list[countArg+3] == "-py"):
              self.init_flags["is_py"] = True
            elif(arg_list[countArg+3] == "-java"):
              self.init_flags["is_java"] = True
        else:
          self.contest_name += arg_list[countArg+1]
          if len(arg_list[1:]) == 2:
            if(arg_list[countArg+2] == "-py"):
              self.init_flags["is_py"] = True
            elif(arg_list[countArg+2] == "-java"):
              self.init_flags["is_java"] = True
