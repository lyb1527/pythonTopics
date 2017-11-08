"""
many people use Python as a replacement for shell scripts, using it to automate
common system tasks, such as manipulating files, configuring systems, and so forht.

"""

1. accept script input via redirection, pipes, and input files

# script that accepts input using whatever mechanism is easiest for the user
# including piping output from a command to script, redirect a file into the
# script.

import fileinput

with fileinput.input() as f.input:
    for line in f_input:
        print(line, end='')

NOTE: then you can accept input to the script in many ways. If save it as
filein.py and make it executable. You can do all of the following:

$ls | ./filein.py # pipe output to script
$./filein.py /etc/passwd # redirect a file into script
$./filein.py < /etc/passwd #

The fileinput.input() creates and returns an instance of the FileInput class

The instance can be used as a context mangeger 




2. Terminate a program with an error message

# terminate program by printing a message to standard error and returning the nonzero status code


raise SystemExit("it failed!")




3. Parse Comman-line options

# a program that parses options supplied on the command line(found in sys.argv)

 argparse module can be used to parse command line options.


import argparse


4. Prompting for password at runtime
"""
a script that requires a password for interactive use.
Prompt user for password rather than hardcode the password
"""
import getpass


5. Getting the Terminal size
"""
get the terminal size in order to properly format the output of your program

"""
import os
sz = os.get_terminal_size()

sz.columns
sz.lines



6. Executing an external command getting its output

"""
execute an external command and collect its output as a python string
"""

import subprocess

# this returns output as a byte string, needs decoding
output_bytes = subprocess.check_output(['netstat', 'a'])

output = output_bytes.decode('utf-8')



7. COpying or moving files and directories

"""
need to copy or move files and dirs around without shell commands
"""

# shutil has portable implementation of functions of copying fiels and directories
import shutil

# copy src to es (cp sr dst)
shutil.copy(src, dst)

# copy files, but preserve metadata(cp -p src dst)
shutil.copy2(src, dst)

# copy direcotyr tree (cp -R src dst)
shutil.copytree(src, dst)

# move sr to dst
shutil.move(src, dst)

NOTE: arguesmtn are all strings supplying file and dir names.



8. Creating and Unpacking Archives

"""
carete or unpack archives in tar, tgz, or zip formats
"""

import shutil

shutil.unpack_archive('python3.3.tgz')
shutil.make_archive('py33', 'zip', 'python-3-3.0')
#   argumets        (outName, outFormat, fileToArchive)


# get list of supported archive formates
shutil.get_archive_formats()



9. Find Files by name
"""
find files,
"""

# to search for files, use os.walk(), supply


os.walk method traverses the directory hierachy for us. FOr each dir it enter,
it returns a 3-tuple, containing relative path, dirs, and fiels in the list

import os

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))

10. Reading configuration files
"""
read config files written in the common .ini config file format
"""

from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')
config.setctions() # return sections in [], EX: [server]




11. Adding Logging to simple Scripts
"""
to write diagonostic information to log files
"""


# add logging to simple programmings use logging module
import logging

def main():
    # config the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
    )





12. Adding logging to libraries




13. Making a Stopwatch Timer

"""
record the time it takes to perform various tasks
"""

time module contains various function for performing time-related funtion
but useful to put a high-level on them to mimic a stop watch



14. Putting limits on Memory and CPU usage

"""
place some limits on the memory or CPU use of a program on Unix system
"""

the resource module can be used to perfrom both tasksself.

import signal
import resource
import os


15. Launch A web Browser
"""
launch a web browser from a script and have it point to some URL specified
"""

import webbrowser
webbrowser.open("www.google.com")
