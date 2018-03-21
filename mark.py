#!/usr/bin/env python3
import sys
import shutil
import os

uid = sys.argv[1]
rf = "return/u" + uid + ".txt"
print(uid)
if not os.path.isfile(rf):
	shutil.copyfile("template.txt", rf)

editor = "subl"
osCommandString = editor + " " + rf
os.system(osCommandString)

