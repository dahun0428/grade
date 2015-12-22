#!/usr/bin/python
import os
import time
import getpass
import re
def do_only_one():
  os.system("curl -o ./meaningless.txt --cookie ./cookie.txt --cookie-jar ./cookie.txt --user-agent Mozilla/4.0 -X POST --data \"j_username="+username+"&j_password="+password+"&last_login_id_save=1\" http://mpovis.postech.ac.kr/mpovis/login.do > ./trash.txt 2>&1")  

def dothis(number,wait):
  year = time.strftime ("%Y", time.localtime ())
  month = (int (time.strftime ("%m", time.localtime ()))) % 10
  
  semester = "090"

  if month < 4:
    semester = "092"

  os.system("/usr/bin/curl -o ./mygrade.txt --cookie ./cookie.txt --cookie-jar ./cookie.txt --user-agent Mozilla/4.0 \"http://mpovis.postech.ac.kr/mpovis/zcm/ZCMW6011.do?pType=normal_search&iPeryr="+year+"&iPerid="+semester+"\" >> ./trash.txt 2>&1")

  f = open("./mygrade.txt","r")

  while 1:
    line = f.readline()
    if "Completed" in line:
      break

  while 1:
    line = f.readline()

    if re.findall (r"[A-Z]{4}[0-9]{3}",line):
      courseNo = line.replace('<td>','').replace('</td>','').replace('\t\t\t\t\t\t\t','')
      f.readline()
      subject = f.readline().replace('<td>','').replace('</td>','').replace('\t\t\t\t\t','').replace('\n','')
    
    elif "Credit" in line:
      grade = f.readline().replace('<td>','').replace('</td>','').replace('\t','')
      print subject, courseNo
      
      if re.findall (r"[ABCDFISU]",grade):
        print "\tGrade: ", grade
      else:
        print ""
        

    elif "</html>" in line:
      break



if __name__ == "__main__":
  os.system ("/bin/rm cookie.txt 2>/dev/null ;/bin/rm meaningless.txt 2>/dev/null; /bin/rm ./trash.txt 2>/dev/null")
  username = raw_input ("input your POVIS ID: ")
  password = getpass.getpass ("input your password: ")
#  number = raw_input ("the number of subjects: ")
#  wait = raw_input ("If waiting: ")
  number = 1
  wait = 1
  do_only_one ()
  while 1:
    print time.strftime ("%Y-%m-%d %A %I:%M", time.localtime ())
    dothis (number, wait)
    time.sleep (10)
    os.system ("/usr/bin/clear")

