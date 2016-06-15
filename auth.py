#!/usr/bin/python
 
import sys
import socket
import math
import re

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def matchpasswd(login,passwd):
    # Write your own function definition. 
    # Use mysql, files, /etc/passwd or some service or whatever you want
    loginNumbers = ''.join(re.findall('\d', login ))
    passwdNumbers = ''.join(re.findall('\d', passwd ))
    if str.isdigit(loginNumbers) and is_prime(int(loginNumbers)) and str.isdigit(passwdNumbers) and is_prime(int(passwdNumbers)):
        return True
    return False
 
while True:
    # read a line from stdin
    line = sys.stdin.readline()
    # remove '\n' from line
    line = line.strip()
    # extract username and password from line
    username = line[:line.find(' ')]
    password = line[line.find(' ')+1:]
    
    if matchpasswd(username, password):
        sys.stdout.write('OK\n')
    else:
        sys.stdout.write('ERR\n')
    # Flush the output to stdout.
    sys.stdout.flush()
