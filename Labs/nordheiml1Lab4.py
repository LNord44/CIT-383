#!/usr/bin/python3

import csv

header = []
row = []

def readData():
    with open("employee_logins.csv", "r") as loginFile:
        name = csv.reader(loginFile, delimiter=',')
        header = next(name)
        count = 0
        for lines in name:
            if int(lines[3]) >= 50:
                row.append([lines[0], lines[1], lines[3]])
                print(lines[0], lines[1], lines[3])
                count = count + 1
        print(row)
        print("The number of suspicious accounts are " + str(count))
        loginFile.close()
        return header, row


def makeFile(header, row):
    finalHeader = []
    finalHeader.append(header[0])
    finalHeader.append(header[1])
    finalHeader.append(header[3])
    with open("NewFile.txt", "w") as newFile:
        writer = csv.writer(newFile)
        writer.writerow(finalHeader)
        i = 0
        for indexes in row:
            writer.writerow(row[i])
            i = i + 1
        newFile.close()

header, row = readData()
makeFile(header, row)