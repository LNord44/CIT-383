#!/usr/bin/python3

# Luke Nordheim, Lab8

import re, csv

# this method finds all compromised ips using regex and writes to compromised.csv
def compIP():
    compromised = r'^250\.30\.8\.([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])$'
    compData = []
    with open("empdata.csv", "r") as newFile:
        ips = csv.reader(newFile, delimiter=',')
        header = next(ips)
        for line in ips:
            if re.search(compromised, line[3]):
                print(line[0] + "," + line[1] + "," + line[2] + "," + line[4])
                compData.append([line[0], line[1], line[2], line[4]])

            with open("compromised.csv", "w") as outFile:
                writer = csv.writer(outFile)
                writer.writerows(compData)
                outFile.close()

# this method finds all passwords that are considered weak by using regex and adding a count if they don't meet a criteria
def badPass():
    passWord = r'(?=.{10})|(?=.{11})|(?=.{12})'
    with open("empdata.csv", "r") as newFile:
        passwords = csv.reader(newFile, delimiter=',')
        for line in passwords:
            count = 0
            if len(line[6]) > 10 and len(line[6]) > 12:
                count += 1
            if re.search("[A-Z]",line[6]):
                count += 1
            if re.search("[a-z]",line[6]):
                count += 1
            if re.search("\W",line[6]):
                count += 1
            if re.search("[A-Z]",line[6]):
                count += 1
            # use r in front if issues
            if re.search("[\d]+",line[6]):
                count += 1

            if count > 0:
                print(line[0] + " " + line[1] + " " + line[6])

# this method changes the accounting dept. to finance dept. and writes their info to empdata-new.csv
def changeDept():
    dept = r'Accounting'
    deptList = []
    with open("empdata.csv", "r") as newFile:
        change = csv.reader(newFile, delimiter=',')
        header = next(change)
        for line in change:
            if re.search(dept, line[4]):
                print(line[0] + " "+ line[1])
                deptList.append([line[0],line[1],line[2],line[3],'Finance',line[5],line[6]])

            with open("empdata-new.csv", "w") as outFile:
                writer = csv.writer(outFile)
                writer.writerows(deptList)
                outFile.close()

# this method prints the menu options
def printMenu():
    print("1. Find compromised IPs: ")
    print("2. Find weak passwords: ")
    print("3. Change dept names: ")
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
        compIP()
    elif option == 2:
        badPass()
    elif option == 3:
        changeDept()
    else:
        exit(1)

manageOption()
