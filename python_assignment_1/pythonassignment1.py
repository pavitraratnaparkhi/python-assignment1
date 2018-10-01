"""
Write a python code to accept input for following format of daily status report from python
terminal. Write this information to a delimiter separated file. New information should be
appended at the end of the file. FilePath, FileName, Delimiter, Date Format to display:
should be configurable through config file. Input received should also be emailed to
pre-configured email list in format as below:
"""
import configparser
import re
import time


class WorkSheet:

    # Input Output List
    l = ["Topic", "Contents", "Start-Date","End-date","Progress(Completed/In-progress)","Confidence-level(High/Medium/Low)", "Team member", "Comments"]
    output_list=[]

    # Config File parsing
    configParser = configparser.RawConfigParser()
    configFilePath = r'/home/pavitra/Documents/workspace_python/Python_Programs_11/python_assignment_1/config.csv'
    configParser.read(configFilePath)
    file_path = configParser.get('my-config', 'filepath')
    file_name = configParser.get('my-config', 'filename')
    delimiter = configParser.get('my-config', 'delimiter')
    date_format = configParser.get('my-config', 'date_format')

    # Accept user input
    def accept_user_input(self):
        for item in self.l:
            print("Enter data for", item, ":")
            user_input = input()
            self.validate_input(item, user_input)

    # Validating user input
    def validate_input(self,item, user_input):
        if item == self.l[0] or item == self.l[1]:
            validate = re.search('^[a-zA-Z0-9._!@#$%^&*() ]{1,255}$', user_input)
            if validate:
                self.output_list.append(user_input)
            else:
                print("Invalid input detected. Please re-enter data for", item,":")
                user_input = input()
                self.validate_input(item, user_input)

        if item == self.l[2] or item == self.l[3]:

            # Validation for accepting date in form of DD/MM/YYYY
            validate = re.search('^(0?[1-9]|[12][0-9]|3[01])[/](0?[1-9]|1[012])[/]\d{4}$', user_input)
            # Validation for accepting only past and present date
            try:
                self.date_timestamp = time.mktime(time.strptime(user_input, self.date_format))
            except ValueError:
                print("Exception Catched!!..in except block..directing towards else block")
                # user_input = input()
                # self.validate_input(item, user_input)

            if validate and self.date_timestamp <= time.time():
                self.output_list.append(user_input)
                # print("in if block")
            else:
                # print("in-else block")
                print("Invalid input detected. Please re-enter data for", item, "in form of DD/MM/YYYY:")
                user_input = input()
                self.validate_input(item, user_input)

        if item == self.l[4]:
            complete=user_input.lower()

            if complete == "completed" or complete == "in-progress":
                self.output_list.append(user_input.lower())
            else:
                print("Invalid input detected. Please re-enter data in form of (Completed/In-Progress):")
                user_input = input()
                self.validate_input(item, user_input)

        if item == self.l[5]:
            complete=user_input.lower()

            if complete == "high" or complete == "medium" or complete == "low":
                self.output_list.append(user_input.lower())
            else:
                print("Invalid input detected. Please re-enter data in form of (High/Medium/Low):")
                user_input = input()
                self.validate_input(item, user_input)

        if item == self.l[6]:
            validate=re.search('^[a-zA-Z0-9_ ]{1,100}$', user_input)
            if validate:
                self.output_list.append(user_input)
            else:
                print("Invalid input detected. Please re-enter data for", item,":")
                user_input = input()
                self.validate_input(item, user_input)

        if item == self.l[7]:
            validate=re.search('^[a-zA-Z0-9._!@#$%^&*() ]{1,1024}$', user_input)
            if validate:
                self.output_list.append(user_input)
            else:
                print("Invalid input detected. Please re-enter data for", item,":")
                user_input = input()
                self.validate_input(item, user_input)




