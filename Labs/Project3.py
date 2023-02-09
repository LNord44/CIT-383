import os, sys, ftplib, smtplib, mimetypes, getpass, subprocess, shutil, subprocess as sp, paramiko
from datetime import datetime,timedelta
from email.message import EmailMessage

# these two lists will be used in modweeks()
lof = []
compromisedFiles = {}

def email():
    message = EmailMessage()
    # getting necessary varibales and logging into email
    send = input("Please enter the senders email address: ")
    passwd = getpass.getpass("Please enter the senders password associated: ")
    reciever = input("Please enter the recipiants email: ")
    subj = input("Enter subject header: ")
    compUser = input("Enter compromised userName: ")
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.login(send, passwd)

    #defining headers
    message['From'] = send
    message['To'] = reciever
    message['Subject'] = subj
    body = """Hello,
    The following list of files are compromised along with the user: """ + '\nUser of compromised files:' + compUser + '\n' + str(modWeeks())
    # modweeks is the method you need to make that returns the modified files within the last few weeks

    # sending message with attached file or not
    message.set_content(body)
    varCheck = input("Please enter y or n to attach a file: ")
    if (varCheck == "y"):
        fileN = input("Please enter filename: ")
        mime_type, _ = mimetypes.guess_type('fileN')
        mime_type = mimetypes.MimeTypes().guess_type(fileN)
        print(mime_type)
        mime_type, mime_subtype = mime_type.split('/')
        with open(fileN, 'rb') as file:
            message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=fileN)
            mail_server.send_message(message)
            mail_server.quit()
    else:
        mail_server.send_message(message)
        mail_server.quit()

def modFiles():
    # finding compromised files from modweeks()
    modWeeks()
    port=22
    # getting variables
    host = input("Enter your machine's ip")
    passwd = input("Please enter student's password")
    users = input("Please enter sshuser")
    con = paramiko.SSHClient()
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    con.load_system_host_keys()
    con.connect(host, port, users, passwd)
    sftp = con.open_sftp()

    # getting files in you want them
    selection = input("Would you like to download the modified files? y or n: ")
    if selection == "y" or selection == "Y":
        dest = input("Please input absolute to the files: ")
        print(lof)
        for files in lof:
            sftp.get('/home/sshuser/' + files, dest + files)
        sftp.close()

def modWeeks():
    # getting necessary variables
    port = 22
    host = input("Enter your machine's ip")
    passwd = input("Please enter student's password")
    users = input("Please enter sshuser")
    con = paramiko.SSHClient()  # you need to download paramiko
    con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    con.load_system_host_keys()
    con.connect(host, port, users, passwd)
    sftp = con.open_sftp()

    #timeOfDiff = datetime.today() - timedelta(days=21)

    for iters in sftp.listdir():
        output = str(sftp.lstat(iters)).split()[0]
        if not 'd' in output: # must be dir not file
            lof.append(iters)

    for files in lof:
        timeOfFile = sftp.stat(files).st_mtime
        timeOfLastMod = datetime.fromtimestamp(timeOfFile)

        timeDiff = datetime.now() - timeOfLastMod
        if timeDiff < timedelta(weeks=3):
            nameOfFile = str(files)
            date = str(timeOfLastMod)
            #lof.append([nameOfFile, date])
            compromisedFiles[timeOfFile]=date
    # making a string that contains the compromised files and their data
    firstString = ("Compromised Files", "Last Modified")
    secondString = ("\n--------------------------------")
    firstString = firstString + secondString
    for files, data in compromisedFiles.items():
        thirdString = str(files + date)
        finalString = firstString + thirdString
    return finalString

# this method prints the menu options
def printMenu():
    print("1. Using a certain Ip address, find compromised files modifed within the last three weeks on that machine's home dir and send an email: ")
    print("2. Download affected files from compromised IP: ")
    print("3. Exit")

# this function retrieves the menu option they want
def userChoice():
    printMenu()
    choice = int(input("Enter one of the options above: "))
    return choice

# this function manages the option that you want
def manageOption():
    option = userChoice()
    if option == 1:
        email()
    elif option == 2:
        modFiles()
    else:
        exit(1)

manageOption()




