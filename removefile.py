# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:38:21 2019

@author: Mansi Shukla
"""

import smtplib 
import time
import datetime
# creates SMTP session 
def removefile():
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# start TLS for security 
    s.starttls() 

# Authentication 
    s.login("mansi.shukla2017@vitstudent.ac.in","jailakshmi") 
    subject="File remove"
# message to be sent 
    text = "Hi admin\n An existing file has been removed at time\n %s" %st
    message = 'Subject: {}\n\n{}'.format(subject, text)
# sending the mail 
    s.sendmail("mansi.shukla2017@vitstudent.ac.in", "mansishukla2505@gmail.com", message) 

# terminating the session 
    s.quit() 
