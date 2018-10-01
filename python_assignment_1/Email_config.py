#!/usr/bin/env python

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from getpass import getpass
# from smtplib import SMTP_SSL
from python_assignment_1.appendfile import AppendFile
from python_assignment_1.pythonassignment1 import WorkSheet


class EmailConfig:

    # Email Configurations not working due to firewall issue
    # def send_email():
        # server = smtplib.SMTP(host='smtp.gmail.com', port= '587')
        # server.starttls()
        # server.login("ratnaparkhipavitra@gmail.com", "p@ssw0rd")
        # sender_email="ratnaparkhipavitra@gmail.com"
        # receiver_email="ratnaparkhipavitra@gmail.com"
        # msg=MIMEMultipart("alternative")
        # msg['Subject'] = 'Every day work log update'
        # msg['From'] = login
        # msg['To'] = receiver_email
        # Email_text = MIMEText(html, 'html')
        # msg.attach(Email_text)
        # server.sendmail(sender_email, receiver_email, str(create_template.new_table))
        # print(Email_text)

    a = AppendFile()
    w = WorkSheet()
    a.appenddatatofile()

    # Create body of Message
    def create_template(self):

            self.strTable = "<html><header><b>Today's Status Update</b></Header><table border=1 cellpadding=10 cellspacing=0><tr bgcolor='#A6C4AA'>"

            for item in self.w.l:
                str_row = "<td>" + str(item) + "</td>"
                self.strTable = self.strTable + str_row
                if item == self.w.l[-1]:
                    self.strTable = self.strTable + "</tr><tr>"

            for item1 in self.w.output_list:
                str_row = "<td>" + str(item1) + "</td>"
                self.strTable = self.strTable + str_row

            strTable = self.strTable + "</tr></table></html>"
            return strTable


E = EmailConfig()
new_table= E.create_template()
hs = open("WorkSheet_Email_Template.html", 'w')
hs.write(new_table)








