#!/usr/bin/python3
# make sure to comment each section
import os
import os.path
import stat

#this method creates the files using the open() method
def createFiles(i):
    name = "file" + str(i) + ".txt"
    open(name, "w")
    return name

#this method makes the subdirectories using os.mkdir()
def createSubDirectories(i):
    dir = "dir_" + str(i)
    parentDir = "/home/student/Lab3/venv/Lab3"
    path = os.path.join(parentDir, dir)
    os.mkdir(path)

#this method is prints out our contents within the lab3 directory
def listEntries(pathType):
    print("Name" + "\t\t\t\tType")
    print("------" + "\t\t\t\t------")
    list = os.listdir("/home/student/Lab3/venv/Lab3")
    for entry in list:
        print(entry + "\t\t\t\t" + getInodeType(entry))

#this method checks and returns if it's a directory or not using os.path.isdir()
def getInodeType(pathType):
    if os.path.isdir(pathType):
        return "Directory"
    else:
        return "File"

# this method changes the extension of files using .split() method
def renameFiles(tempVarName, extension, newExtension):
    os.chdir(tempVarName)
    hasPeriod = os.listdir(".")
    for entry in hasPeriod:
        if getInodeType(entry) == 'File':
            change = tempVarName + '/' + entry
            temp = entry.split(".")[1]
            newTemp = entry.split(".")[0]
            if temp == extension:
                newType = tempVarName + '/' + newTemp + '.' + newExtension
                os.rename(change, newType)

# step 1
print(os.getcwd())

# step 2, remember to un-comment the line below
os.mkdir("Lab3")

# step 3
os.chdir("Lab3")
tempVarName = os.getcwd()

# step 4
print(os.getcwd())

# step 7
M = int(input("Enter the value for M: "))
while not(M > 1):
    M = int(input("Enter the value for M: "))

N = int(input("Enter the value for N: "))
while not(N > 1):
    N = int(input("Enter the value for N: "))

# step 5
for i in range(1, M + 1):
    createFiles(i)

# step 6
for i in range(1, N + 1):
    createSubDirectories(i)

# step 8
listEntries(os.getcwd())

# step 9
renameFiles(tempVarName, 'txt', 'dat')

# step 10
listEntries(os.getcwd())