#!/usr/bin/env python

from config import *
from datetime import datetime
from email.mime.text import MIMEText

import smtplib

date = datetime.now().strftime("%Y%m%d")
report_file = "report/{0}.html".format(date)

# read generated report from file
try:
    fp = open(report_file, 'rb')
    msg = MIMEText(fp.read(), 'html')
    fp.close()
except:
    print("Error, failed to open report files.")

# setup mail content
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# send reprt
try:
    smtp = smtplib.SMTP(smtp_server)
    smtp.sendmail(sender, recipient, msg.as_string())
    smtp.quit()
except:
    print("Error, failed to send report.")
