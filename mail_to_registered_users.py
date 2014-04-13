#!/usr/bin/env python 
"""
sending email to the registered oqtans users
"""

import time 
import psycopg2
import smtplib
from email.mime.text import MIMEText

def compose_mail(recipient):
    """
    compose group mail 
    """

    body_text = ""
    body_text += "Dear user,\n\n"

    body_text += "We have applied an up-to-date version of OpenSSL and re-issued a new security certificate for oqtans to counteract the Heartbleed security bug, which potentially exposes your username and password on infected sites. For continued safe computing, we recommend changing your PASSWORD.\n\n"
    
    body_text += "Thanks for using our Galaxy tools,\n"
    body_text += "Vipin | R\xc3\xa4tsch Lab Galaxy team\n\n"

    body_text += "You are receiving this email because you are a registered user of oqtans Galaxy server (https://galaxy.cbio.mskcc.org) provided from R\xc3\xa4tsch Laboratory(http://raetschlab.org). Any issues please contact galaxy@raetschlab.org\n"
    
    body_msg = MIMEText(body_text)

    sender = 'username@domain.org'
    
    body_msg['Subject'] = "Oqtans Security Update"
    body_msg['From'] = sender 
    body_msg['To'] = recipient

    try:	
        s = smtplib.SMTP('localhost')
        s.sendmail(sender, [recipient], body_msg.as_string())
        s.quit()
    except:
        pass
    
    time.sleep(5) 

dbcon = psycopg2.connect('dbname=galaxy-data')
cursor = dbcon.cursor() 
cursor.execute("""select email from galaxy_user""") 

for email_id in cursor.fetchall():
    print email_id[0]
    compose_mail(email_id[0]) 

cursor.close() 
dbcon.close() 

