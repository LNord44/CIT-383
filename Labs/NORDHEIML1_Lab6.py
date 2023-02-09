#!/usr/bin/python3

# Luke Nordheim, CIT 383

# importing libraries
import os, sys, subprocess, crypt, pwd, getpass

# this method prints the menu options
def printMenu():
    print("1. Create a new user: ")
    print("2. Remove a current user: ")
    print("3. Edit a current user: ")
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
        newUser()
    elif option == 2:
        deleteUser()
    elif option == 3:
        editUser()
    else:
        exit(1)

# this method checks whether the user exists
def checking(userName):
    checkPasswd = open('/etc/passwd','r')
    for name in sorted(checkPasswd.readline()):
        look = name.split(":")
        if userName == look[0]:
            return True
        else:
            return False

# option 1, creates a new user
def newUser():
    notUnique = True
    while notUnique == True:
        name = input("Enter first and last name: ")
        userName = input("Enter a username: ")
        notUnique = checking(userName)
        if notUnique == True:
            print("The username already exists")
            sys.exit(1)
        else:
            password = getpass.getpass()
            subprocess.run(['useradd', '-p', password, '-c', name, userName])
            sys.exit(1)

# option 2, deletes the given user
def deleteUser():
    username = input("Enter the username you want to delete: ")
    try:
        go = subprocess.run(['userdel', '-r', username])
        if go.returncode == 0:
            print("User successfully deleted")
            sys.exit(1)
    except:
        print("Failed to delete user")
        sys.exit(1)

# option 3, edit a user to lock an account or change their real name
def editUser():
    notUnique = True
    while notUnique == True:
        userName = input("Enter the username of the account you want to edit: ")
        newName = input("If you wish to edit the user's name, enter a new username for them: ")
        notUnique = checking(userName)
        if notUnique == False:
            print("The username doesn't exist!")
            sys.exit(1)
        else:
            option = int(input("Enter what aspect of the user you would like to edit (1: lock acount, 2: change real name): "))
            if option == 1:
                subprocess.call(['usermod', '-L', userName])
                sys.exit(1)
            elif option == 2:
                subprocess.call(['usermod', '-c', newName, userName])
                sys.exit(1)
            else:
                print("You didn't enter either 1 or 2!")
                sys.exit(1)

# calling manageOption() to start our script
manageOption()





