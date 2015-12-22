#!/usr/bin/python
import os
import time
import getpass
import re
def do_only_one():
  os.system("curl -o ./meaningless.txt --cookie ./cookie.txt --cookie-jar ./cookie.txt --user-agent Mozilla/4.0 -X POST --data \"j_username="+username+"&j_password="+password+"&last_login_id_save=1\" http://mpovis.postech.ac.kr/mpovis/login.do > ./trash.txt 2>&1")  

def dothis(number,wait):
  os.system("/usr/bin/curl -o ./mygrade.txt --cookie ./cookie.txt --cookie-jar ./cookie.txt --user-agent Mozilla/4.0 \"http://mpovis.postech.ac.kr/mpovis/zcm/ZCMW6011.do?pType=normal_search&iPeryr=2015&iPerid=092\" >> ./trash.txt 2>&1")

  f = open("./mygrade.txt","r")
  i=356
  line= f.readlines()
  for j in xrange(int(number)):
    subject = line[i].replace('<td>',' ').replace('</td>',' ').replace('\t\t\t\t\t',' ')
    grade = line[i+6].replace('<td>',' ').replace('</td>',' ').replace('\t\t\t\t\t\t\t',' ')
    print subject,grade
    if wait in subject and wait != '':
      if re.findall(r'[A-Z]', grade):
        print("\a")


    i+= 17

if __name__ == "__main__":
  os.system ("rm cookie.txt;rm meaningless.txt; rm ./trash.txt")
  username = raw_input ("input your POVIS ID: ")
  password = getpass.getpass ("input your password: ")
  number = raw_input ("the number of subjects: ")
  wait = raw_input ("If waiting: ")
  do_only_one ()
  while 1:
    print time.strftime ("%Y-%m-%d %A %I:%M", time.localtime ())
    dothis (number, wait)
    time.sleep (10)
    os.system ("/usr/bin/clear")

