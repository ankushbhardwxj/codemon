#!/usr/bin/env python
import sys
import commands

command = sys.argv[0]
argument = sys.argv[1]


if argument == "init":
  contestName = sys.argv[2]
  commands.init(contestName)
elif argument == "listen":
  fName = sys.argv[2]
  commands.listen(fName)
