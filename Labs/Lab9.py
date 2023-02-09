#!/usr/bin/python3

# Luke Nordheim, Lab 9

import http.client, os, socket, re, getpass as ps
from ftplib import FTP

# connects us to the 2nd VM
def connecting():
    host = input("Enter your host ip address: ")
    userName = 'ftpuser'
    passwd = ps.getpass("Enter password: ")
    try:
        con = FTP(host, userName, passwd)
    except:
        print("Cannot establish connection")
    return con

# sends files from this VM to my second VM
def sending():
    con = connecting()
    con.cwd('cit383Labs')
    file = input("What file do you want to give to your second VM?: ")
    if os.path.exists(file):
        newBinary = con.retrbinary(file, open('/home/student/Downloads', 'wb').write)
        con.storbinary('STOR' + str(file), newBinary)
        newBinary.close, con.close()
        print("File was successfully given!")
    else:
        print("File couldn't be transferred!"), con.close()

# gets certain HTTP information from a certain website
def httpWork():
    site = input("Please enter the full URL of a webiste you want the information on (includes www. and the extension):")
    connection = http.client.HTTPSConnection(site)
    connection.request("GET", "/")
    response = connection.getresponse()
    print("The site's status code is " + response.status)
    print("The site's verions is " + response.version)
    print("The site's length is " + str(response.length)) # units need to change
    print("The site was last modified on " + response.headers['Last-Modifed'])
    connection.close()

#method that downloads all Files with a certain extension from the same directory
def downFiles():
    con = connecting()
    con.cwd('cit383Labs')
    con.close()

# this method prints the menu options
def printMenu():
    print("1. Remotely upload a file using the FTP: ")
    print("2. Download all files with the same extension from one directory: ")
    print("3. View HTTP information: ")
    print("4. Exit")

# this function retrieves the menu option they want
def userChoice():
    printMenu()
    choice = int(input("Enter one of the options above: "))
    return choice

# this function manages the option that you want
def manageOption():
    option = userChoice()
    if option == 1:
        sending()
    elif option == 2:
        downFiles()
    elif option == 3:
        httpWork()
    else:
        exit(1)

manageOption()
