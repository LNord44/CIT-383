#!/usr/bin/python3

import os, argparse as ap, sys

# creating instance of argument parser
parser = ap.ArgumentParser(prog ="listProgram", description="This program will print the contents of a dir for you!",
                           usage="./Lab7.py [-h][-l]", add_help=True)

# defining arguments to add
parser.add_argument("dir_path", action="store", default=".", help="Enter dir path") # required? dest="dir_path"
parser.add_argument("-l", "--logfile", action="store", default=".", dest="log_file", help="This option will list the dir's content to a logfile")

# parsing our arguments
try:
    results = parser.parse_args()
except:
    print("Unknown argument provided! Program will exit") # this is the error handling for when an unknown argument is provided
    exit(1)

# getting our dir path and defining a logFile to write to
dirPath = results.dir_path
logFile = str(results.log_file)

if os.path.exists(dirPath): # check for if Dir exists
    if logFile == ".": # if no -l parameter provided
        list = os.listdir(dirPath)
        print("Name")
        print("*" * 32)
        for files in list:
            print(files)
    else: # if -l provided
        list = os.listdir(dirPath)
        with open(logFile, 'w') as logF:
            logF.write("Name\n")
            logF.write("******************\n")
            for newFiles in list:
                logF.write(newFiles + "\n")
else: # if dir does not exist
    print("This directory does not exist!")
    exit(1)

# ./Lab7.py -l "path for file to write to" "path of dir you want to write"
# python3 Lab7.py -l  /home/student/Lab7New/venv/new.txt  /home/student/Lab7New/venv/bin
# python3 Lab7.py /home/student/Lab7New/venv/bin

