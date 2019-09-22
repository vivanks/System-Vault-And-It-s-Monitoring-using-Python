# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:51:46 2019

@author: Mansi Shukla
"""

# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 
import datetime
import time
# creates SMTP session 
def un_mailfunc():
	s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
	s.starttls() 

# Authentication 
	s.login("mansi.shukla2017@vitstudent.ac.in","jailakshmi") 

# message to be sent 
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	print(st)

	subject = "Re - Unauthorized Access"
	text = """
   Hello Admin,\n

    User has tried to enter a private file\n

    At """+str(st)+"""

    Thanks,

    From,
    System
    """

	message = 'Subject:{} \n\n\n {}'.format(subject,text)
# sending the mail 
	s.sendmail("mansi.shukla2017@vitstudent.ac.in", "mansishukla2505@gmail.com", message, ) 

# terminating the session 
	s.quit() 

