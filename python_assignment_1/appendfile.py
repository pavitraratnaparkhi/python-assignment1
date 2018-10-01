from python_assignment_1.pythonassignment1 import WorkSheet


class AppendFile:

    # Creating worksheet instance and access/call accept user input and validate input methods
    w1 = WorkSheet()
    w1.accept_user_input()
    print("This is valid data:",w1.output_list)
    print("Please check in Output file and also check email.")

    # function to write/append all parameters to file
    def appenddatatofile(self):
        with open(self.w1.file_path, 'a') as file:
            for nested_list in self.w1.output_list:
                file.write(str(nested_list))
                # code to prevent delimiter display after last element
                if nested_list != self.w1.output_list[-1]:
                    file.write(self.w1.delimiter)
            file.write("\n")


# Created instance variable of Appendfile class and call method appenddatatofile
# a = AppendFile()
# a.appenddatatofile()

