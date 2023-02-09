#!/usr/bin/python3

# Luke Nordheim, Project 2

import csv, subprocess, grp, re

# making our lists for the users
name=[]
append1=[]
append2=[]

def userName():
    with open('employee.csv', 'r') as file:
        data = csv.reader(file, delimiter=',')
        header = next(data)

        for i in data:
            count = 0
            name.append(i) # getting all entries from employee.csv
            user = i[1] + i[0][0] # taking the last name and first letter of their first name to make their usernames
            append1.append(user) # adding to second list

            for line in append1:
                re.search(user, line)
                count += 1
            if user in append2: # adding to append 2 if the users already in the list
                newName = user + str(count)
                append2.append(newName)

            else:
                append2.append(user) # adding to append2 if the username isn't in append2 yet
        file.close()

# this method checks whether the user exists
def checking(uName):
    checkPasswd = open('/etc/passwd','r')
    for name in sorted(checkPasswd.readline()):
        look = name.split(":")
        if uName == look[0]:
            return True
        else:
            return False

def userAdd():
    for row in name:
        if checking(str(append1)) == False:
            try: # adding the users within the name list
                subprocess.run(["useradd", "-c", str(row[0] + " " + row[1], str(append1))])
                print("User created")
            except:
                print("Not able to be made")
        else:
            print("This user does not need to be made")

def groupCreate():
    for row in name:
        try: # creating groups based off of the name list
            grp.getgrnam(row[2])
        except:
            subprocess.run(["groupadd", row[2]])
            print("Group created")
        try:
            subprocess.run(["usermod", "-a", "-G"])
        except:
            print("User couldn't be added to the group")

# method that prints to the new .csv
def newCSV():
    userList = []
    with open("employee.csv", "r") as newFile:
        change = csv.reader(newFile, delimiter=',')
        header = next(change)
        i = 0
        for line in change:
            userList.append([line[0], line[1], append2[i]])
            i = i + 1

            with open("useraccounts.csv", "w") as outFile:
                writer = csv.writer(outFile)
                writer.writerows(userList)
                outFile.close()

def allCall():
    userName()
    userAdd()
    groupCreate()
    newCSV()

allCall()