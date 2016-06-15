#!/usr/bin/python
 
import sys
import socket
import math
import re
import time
import os.path
def matchip(ip, nowTime):
    if os.path.exists('/tmp/users'):
        f=open('/tmp/users','r')
        for line in f:
            line = line.strip()
            time = line[:line.find(' ')]
            ipaddr = line[line.find(' ')+1:]
            if (ipaddr == ip and nowTime - int(time) < 1800):
                return True
        f.close()
    f=open('/tmp/users','a')
    f.write(str(nowTime))
    f.write(' ')
    f.write(ip)
    f.write('\n')
    f.close()
    return False 
 
while True:
    # read a line from stdin
    line = sys.stdin.readline()
    # remove '\n' from line
    line = line.strip()
    # extract username and password from line
    integer = line[:line.find(' ')]
    ip = line[line.find(' ')+1:]
    if matchip(ip,int(time.time())):
        sys.stdout.write('OK\n')
    else:
        sys.stdout.write('ERR\n')
    # Flush the output to stdout.
    sys.stdout.flush()
