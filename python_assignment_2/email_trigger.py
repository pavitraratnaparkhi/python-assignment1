from python_assignment_2.read_data_from_file import ReadData
from python_assignment_2.confid_access import ConfigAccess


class EmailConfiguration:

    # Email Configurations not working due to firewall issue
    # def send_email():
        # server = smtplib.SMTP(host='smtp.gmail.com', port= '587')
        # server.starttls()
        # server.login(ConfigAccess.sender_email, ConfigAccess.password)
        # sender_email=ConfigAccess.sender_email
        # receiver_email=ConfigAccess.password
        # msg=MIMEMultipart("alternative")
        # msg['Subject'] = 'Every day work log update'
        # msg['From'] = login
        # msg['To'] = receiver_email
        # Email_text = MIMEText(html, 'html')
        # msg.attach(Email_text)
        # server.sendmail(sender_email, receiver_email, str(create_template.new_table))
        # print(Email_text)
    r = ReadData()
    r.accept_input()
    r.read_data(r.final_date)
    l = ["Topic", "Contents", "Start-Date","End-date","Progress(Completed/In-progress)","Confidence-level(High/Medium/Low)", "Team member", "Comments"]

    # Create body of Message
    def create_template(self):

            self.strTable = "<html><header><b>Pending Tasks:</b></Header><table border=1 cellpadding=10 cellspacing=0><tr bgcolor='#A6C4AA'>"

            for item in self.l:
                str_row = "<td>" + str(item) + "</td>"
                self.strTable = self.strTable + str_row
                if item == self.l[-1]:
                    self.strTable = self.strTable + "</tr><tr>"

            for item1 in self.r.output_list:
                    for item2 in item1:
                        str_row = "<td>" + str(item2) + "</td>"
                        self.strTable = self.strTable + str_row
                        if item2 == item1[-1]:
                            self.strTable = self.strTable + "</tr><tr>"

            strTable = self.strTable + "</tr></table></html>"
            return strTable

    def check_output_list(self):
        if self.r.output_list == []:
            print("No Delayed Tasks..")
        else:
            print("Preconfigured email triggered. Please check email.")
            print(self.r.output_list)
            output_table=str(E.create_template())
            return output_table
            # e = EmailConfiguration()
            # e.create_template()
            #trigger_email()


E = EmailConfiguration()
new_table= str(E.check_output_list())
hs = open("WorkSheet_Email_Template_for_inprogress_data.html", 'w')
hs.write(new_table)