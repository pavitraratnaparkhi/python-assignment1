
import re
import time
import csv
from python_assignment_2.confid_access import ConfigAccess

class ReadData:

    inprogress = "in-progress"
    final_date = ""
    output_list =[]

    def accept_input(self):

        print("Enter End date in form of DD/MM/YYYY:")
        end_date = input()
        self.input_validation(end_date)
        # self.user_input_datetime = datetime.strptime(self.final_date, '%d/%m/%Y')

    def input_validation(self, end_date):
        validate = re.search('^(0?[1-9]|[12][0-9]|3[01])[/](0?[1-9]|1[012])[/]\d{4}$', end_date)
        # Validation for accepting only past and present date
        try:
            self.date_timestamp = time.mktime(time.strptime(end_date, ConfigAccess.date_format))
        except ValueError:
            print("Exception Catched!!..in except block..directing towards else block")
            # user_input = input()
            # self.validate_input(item, user_input)

        if validate and self.date_timestamp <= time.time():
            self.final_date = self.date_timestamp
            # print("in if block")
        else:
            # print("in-else block")
            print("Invalid input detected. Please re-enter data for", end_date, "in form of DD/MM/YYYY:")
            end_date = input()
            self.input_validation(end_date)

        # if validate:
        #     self.final_date = end_date
        # else:
        #     print("Invalid input detected. Please re-enter data for", end_date, "in form of DD/MM/YYYY:")
        #     end_date = input()
        #     self.input_validation(end_date)

    def read_data(self, final_date):

        with open(ConfigAccess.file_path, 'r') as f:
            reader = csv.reader(f, delimiter=ConfigAccess.delimiter)
            for row in reader:
                date_in_file = time.mktime(time.strptime(str(row[3]), ConfigAccess.date_format))
                # date_in_file = datetime.strptime(str(row[3]), '%d/%m/%Y')

                if str(row[4]).lower() == self.inprogress and date_in_file <= self.date_timestamp:
                    print(row)
                    self.output_list.append(row)




# r = ReadData()
# r. accept_input()
# r.read_data(r.final_date)
# r.check_output_list()
