#!/usr/bin/python3

# Luke Nordheim, 10/15/21, CIT 383
# importing libraies
import os, shutil, subprocess as sp, time, zipfile, tarfile
from datetime import datetime, timedelta

# method that backs up a certain file to a directory
def backup(srcDir, destDir):
    if not os.path.exists(srcDir):
        print("The source directory does not exist.")
        exit(1)
    if not (os.path.isdir(destDir)):
        print("The destination directory does not exist.")
        exit(1)
    sp.run(['rsync','-a',srcDir,destDir]) #makes arhieve
    print("Directory backup is made")

# method that creates an archieve for a file/ directory
def archive(srcDir, archType, new):
    if not os.path.exists(srcDir):
        # for this dont raise just print a statement then exit
        print("The source directory does not exist.")
        exit(1)
    acceptableTypes =["zip", "tar", "gztar", "bztar", "xztar"] # if double quotes don't work use single
    if not (archType in acceptableTypes):
        print("This archType is not in the list of acceptable types ")
        exit(1)
    shutil.make_archive(base_name=new, format=archType, root_dir='..', base_dir=srcDir)

# method that prints all items greater than your given threshold
def checkSize():
    myData = 'Lab5_zip.zip'
    numKilo = 0
    numEntry = False

    while numEntry == False:
        try:
            numKilo = int(input("Please enter threshold size: "))
            numEntry = True
        except:
            print("Not an integer! Please try again: ")
    thresh = numKilo
    print("The following files are greater than the threshold:")
    with zipfile.ZipFile(myData) as zf:
        for data in zf.infolist():
            greaterThan = thresh < (int(data.compress_size)/1024)
            if greaterThan == True:
                print(data.filename)
            if data.create_system == 0:
                system = 'Windows'
            elif data.create_system == 3:
                system = 'Unix'
            else:
                system = 'UNKNOWN'
            print("Sytem: ", system)
            print("Compressed size: ", (data.compress_size / 1024), 'kilobytes')

# method that checks if you've accessed certain files within a dir within the last week
def checkAccess(dirUsed):
    modFile = False
    timeDif = datetime.today() - timedelta(days=14)
    if os.path.exists(dirUsed) == False:
        dirUsed = os.getcwd()
    print("Here are the files accessed within the last two weeks: ")
    with os.scandir(dirUsed) as dr:
        for data in dr:
            if data.is_file():
                if os.path.getmtime(data) < timeDif.timestamp():
                    modFile = True
                    print(data.name)
                elif modFile == False:
                    print("There's nothing that has been modified")

# prints the display
def printDisplay():
    print("Select one of the following user management options: ")
    print("*" * 50)
    print("1. Backup a selected folder to a certain directory")
    print("2. Create an archieve of a directory")
    print("3. Print all files within a zip file that exceeds your threshold")
    print("4. Print all files within a certain directory that have been accessed within last two weeks")
    print("5. Exit")

# method that returns your selected option and calls printDisplay
def selectOption():
    selectedOption = -1
    while selectedOption not in range(1,5):
        printDisplay()
        selectedOption = int(input("Enter one option above: "))
    return selectedOption

# method that takes your selected option and calls the method of your choice
def manageOption():
    option = selectOption()
    if option == 1:
        srcDir = input("Enter the source path of File/ Directory to backup: ")
        destDir = input("Enter the destination path for the File/ Directory to backup: ")
        backup(srcDir, destDir)
    elif option == 2:
        fileSource = input("Enter the source path of File/ Directory to backup: ")
        fileType = input("Enter a valid type of the file to archieve: ")
        newFile = input("Enter a new filename to archieve as: ")
        archive(fileSource, fileType, newFile)
    elif option == 3:
        checkSize()
    elif option == 4:
        dir = input("Enter the directory you want to check the access of: ")
        checkAccess(dir)
    else:
        exit(1)

manageOption()