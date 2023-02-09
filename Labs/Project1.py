#!/usr/bin/python3

# Project 1
# Luke Nordheim
# CIT 383, 002, FALL 2021
# 10/10/2021

# creating employee class
class Employee:
    def __init__(self, employeeID, firstName, lastName, deptCode, supName, tempPass, server, linuxID):
        self.employeeID = employeeID
        self.firstName = firstName
        self.lastName = lastName
        self.deptCode = deptCode
        self.supName = supName
        self.tempPass = tempPass
        self.server = server
        self.linuxID = linuxID

# this method counts how many different departments our employees are a part of
def getDeptCount(newDict):
    # you can use a varibale instead of  deptDict[code] =
    deptDict = dict()
    for employeeID in newDict:
        code = newDict[employeeID].deptCode
        if code not in deptDict:
            deptDict[code] = 1
        else:
            deptDict[code] += 1
    for code in deptDict:
        print(str(code) + "\t\t\t\t" + str(deptDict[code]))

# this method counts how many different servers our employees access
def getServerCount():
    serverDict = dict()
    for employeeID in newDict:
        code = newDict[employeeID].server
        if code not in serverDict:
            serverDict[code] = 1
        else:
            serverDict[code] += 1
    for code in serverDict:
        print(str(code) + "\t\t\t\t" + str(serverDict[code]))

# final print method
def finalPrint(newDict,count):
    print("\nSummary Report of User Records")
    print("=============================")
    print(str(count) + " record(s) created:")
    print("Department Code\tEmployee Count")
    print("=============================")
    getDeptCount(newDict)
    print("Servers Requested\tEmployee Count")
    print("***********************************")
    getServerCount()
    print("***********************************")
    print("\nEmployee Details")
    print("=============================")
    for employeeID in newDict:
        print("Name: " + newDict[employeeID].firstName + " " + newDict[employeeID].lastName)
        print("Employee ID: " + newDict[employeeID].employeeID)
        print("Department: " + newDict[employeeID].deptCode)
        print("Supervisor: " + newDict[employeeID].supName)
        print("Username: " + newDict[employeeID].linuxID + "\n")
    print("Thanks for the help Alex!")

# this method is gonna be called to fill our dictory with however many people we want
def employeeInfo():
    newDict = dict()
    count = 0
    while True:
        userID = 0
        userNum = False

        # these two blocks below are error catching
        while userNum == False:
            try:
                employeeID = input("Enter the user's employee id: ")
                userNum = True
            except:
                print("Please enter a numerical value")

        if newDict.get(employeeID,0):
            print("Please enter a valid number, this already exists")
            continue

        firstName = input("Enter the user's first name: ")
        lastName = input("Enter the user's last name: ")
        deptCode = input("Enter the user's department number: ")
        supName = input("Enter the user's supervisor (full name): ")
        tempPass = input("Enter the user's temporary password: ")
        server = input("Enter the name of the server they’ve requested: ")
        linuxID = input("Enter the user's Linux account ID:  ")
        # make a dictionary and append all these variables to it
        nEmpList = Employee(employeeID, firstName, lastName, deptCode, supName, tempPass, server, linuxID)
        newDict[employeeID] = nEmpList
        count = count + 1
        anotherRecord = input("Would  you  like  to  create  another  record  (type  yes  or  Y  to continue):  ")

        if anotherRecord == 'n' or anotherRecord == 'N':
            return newDict, count
            break
        elif anotherRecord == 'y' or anotherRecord == 'Y':
            continue

newDict, count = employeeInfo()
finalPrint(newDict, count)

