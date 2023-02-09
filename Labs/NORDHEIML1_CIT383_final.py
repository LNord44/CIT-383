#!/usr/bin/python3

import csv, os, shutil, smtplib, fnmatch
from email.message import EmailMessage

# Luke Nordheim, this is the final project for CIT383

absoInfected = [] # this list contains the absolute paths to our test files
absoDir = [] # this list is going to hold the subdirectories that our infected files are in
infectedFiles = [] # this is the list of our infected files
infectedDir = [] # this is the list of our infected dir
fileSize = [] # this is the list of the infected file's sizes in bytes
csvList = [] # this is the list for my csv

# IMPORTANT, my two test files are named finalTest1.py and finalTest2.py

# this method finds my two test files and apppends their absolute path and the file name to the absoTest and the names list
def find():
    path = '/home/student'
    find = 'finalTest*.py'

    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, find):
                file = os.path.basename(name)
                infectedFiles.append(file)
                absoInfected.append(os.path.join(root, name))
    print(infectedFiles)

# this method finds the parent dirs of our infected files and appends them to dirInfected list
def getDirLists():
    for files in absoInfected:
        dir = os.path.dirname(files)
        absoDir.append(dir)
        dirName = os.path.basename(dir)
        infectedDir.append(dirName)

# this method finds the sizes of our infected files
def getFileSize():
    for path in absoInfected:
        size = os.path.getsize(path)
        fileSize.append(size)

# this method is going to move my infected files to a new home dir and change their permissions
def moveFiles():
    newLocation = '/home/student/Music'
    for path in absoInfected:
        os.chmod(path, 0o700)
        shutil.move(path, newLocation)

# this writes to a new CSV with all the information needed in the email
def getCSV():
    with open("NORDHEIML1infected.csv", "w") as outFile:
        writer = csv.writer(outFile)
        i = 0
        while i < len(absoInfected):
            csvList.append([str(infectedFiles[i])] + [str(fileSize[i])] + [str(absoInfected[i])])
            i = i +1
        writer.writerows(csvList)
        outFile.close()
        return csvList

# this method sends an email to our supervisor
def email():
    message = EmailMessage()
    send = 'cit383.testmail@gmail.com'
    passwd = 'NKU@CIT383'
    reciever = 'sebklearning@gmail.com'
    subj = 'compromised .py files'
    myEmail = 'lukenordheim@outlook.com'
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.login(send, passwd)

    message['From'] = send
    message['To'] = reciever
    message['Cc'] = myEmail
    message['Subject'] = subj
    csvList = getCSV()
    body = """Hello,
    The following list of files are compromised : """ + str(csvList)
    message.set_content(body)
    mail_server.send_message(message)
    mail_server.quit()

# this the method where all the functions are called
def allCall():
    find()
    getDirLists()
    getFileSize()
    moveFiles()
    email()
    #getCSV()

allCall()