# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:22:16 2019

@author: Mansi Shukla
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:51:46 2019

@author: Mansi Shukla
"""

# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 
import time
import datetime
# creates SMTP session 
def addfile():
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# start TLS for security 
    s.starttls() 

# Authentication 
    s.login("mansi.shukla2017@vitstudent.ac.in","jailakshmi")  
    subject="File addition"
# message to be sent 
    text = "Hi admin\n A new file has been added at time\n %s" %st
    message = 'Subject: {}\n\n{}'.format(subject, text)
# sending the mail 
    s.sendmail("mansi.shukla2017@vitstudent.ac.in", "mansishukla2505@gmail.com", message) 

# terminating the session 
    s.quit() 

