# SMTP - Kacper

import smtplib
import os
import getpass

serverHost = input("Enter SMTP server: ")

# do poprawy
while type(serverHost) != str:
    serverHost = input("Enter SMTP server: ")

if os.system("ping /n 1 " + serverHost):
    print(serverHost + " - no response")
    input()
    exit()
else:
    smtpObj = smtplib.SMTP(serverHost, 587)
    print(smtpObj.ehlo())
    print(smtpObj.starttls())

    login = input("Enter login(full): ")
    try:
        password = getpass.getpass("Enter password: ")
    except Exception as error:
        print('ERROR', error)
    else:
        print('Password entered!')

    smtpObj.login(login, password)

    recipient = input("Enter recipient: ")
    subject = input("Enter subject: ")
    content = input("Enter content: ")
    smtpObj.sendmail(login, recipient, "Subject: " + subject + "\n" + content)

    print(smtpObj.quit())
    input()
