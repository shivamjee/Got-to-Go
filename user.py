import csv
import os
import time
import getpass

class user:
    'Common class for User Management'

    def __init__(self):
        self.user = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        self.last_login = ''
        self.current_login = ''
        self.active = ''
        self.valid = 'N'

    def login(self):

        'Load user csv file'
        csv_file_obj = open('//Users/abhishek/Desktop/shivam/python-got-to-go/user.csv')
        csv_reader = csv.reader(csv_file_obj)
        csv_rows = list(csv_reader)
        csv_file_obj.close()

        for i in range(3):

            self.valid = "N"
            self.user = input("Enter valid user name : ")
            self.password = input("Enter valid password  : ")
            #self.password = getpass.getpass("Enter valid password  : ")

            for row in csv_rows:
                if row[0] == self.user and row[1] == self.password:
                    self.first_name = row[2]
                    self.last_name = row[3]
                    self.last_login = row[4]
                    self.current_login = time.strftime("%d/%m/%Y %H:%M:%S")
                    self.active = row[5]
                    self.valid = 'Y'
                    break

            if self.valid == "N":
                print("You have either entered invalid username or password")
                print("Please retry, you have " + str(int(2-i)) + " chances remaining")
                self.user = ''
            else:
                break


    def logout(self):

        csv_file_obj = open('/Users/abhishek/Desktop/shivam/python-got-to-go/user.csv')
        csv_reader = csv.reader(csv_file_obj)
        csv_rows = list(csv_reader)
        for row in csv_rows:
            if row[0] == self.user:
                row[4] = self.current_login
        csv_file_obj.close()

        csv_file_obj = open('/Users/abhishek/Desktop/shivam/python-got-to-go/user.csv', 'w', newline='')
        csv_writer = csv.writer(csv_file_obj)
        for row in csv_rows:
            csv_writer.writerow(row)
        csv_file_obj.close()

        self.user = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        self.last_login = ''
        self.active = ''
        self.valid = 'N'

        print("You have successfully logged out of the system")

    def new_user(self):

        'Load user csv file'
        csv_file_obj = open('/Users/abhishek/Desktop/shivam/python-got-to-go/user.csv')
        csv_reader = csv.reader(csv_file_obj)
        csv_rows = list(csv_reader)
        csv_file_obj.close()

        found = True
        while found:

            self.user = input("Enter valid username ")

            found = False
            for row in csv_rows:
                if self.user == row[0]:
                    print("Username already exists, please retry")
                    found = True
                    break

        print("You have chosen unique username, Congratulations")
        self.password   = input("Enter your password   ")
        #self.password   = getpass.getpass("Enter valid password  : ")
        self.first_name = input("Enter your first name ")
        self.last_name  = input("Enter your last name  ")
        self.last_login = time.strftime("%d/%m/%Y %H:%M:%S")
        self.active = "Y"
        self.valid = "Y"

        row = [self.user, self.password, self.first_name, self.last_name, self.last_login, self.active]
        csv_rows.append(row)

        csv_file_obj = open('/Users/abhishek/Desktop/shivam/python-got-to-go/user.csv', 'w', newline='')
        csv_writer = csv.writer(csv_file_obj)
        for row in csv_rows:
            csv_writer.writerow(row)
        csv_file_obj.close()
