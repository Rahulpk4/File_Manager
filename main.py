import csv
import os


def create_table(fields):
    if os.path.isfile('Data.csv'):
        print("File Already Exists!")

    else:
        with open("Data.csv", 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=",", lineterminator='\n')
            csv_writer.writeheader()

        csv_file.close()


def email(first_name, last_name, email, password, fields):

    with open("Data.csv", 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=",", lineterminator='\n')
        csv_writer.writerow({'First_Name': first_name, 'Last_Name': last_name, 'Email': email, 'Password': password})

    csv_file.close()


def credential(user, password, acc):
    with open('Data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            if user == line['Email'] and password == line['Password']:
                acc = 1

            else:
                continue

    csv_file.close()
    if acc == 1:
        print ('Access Approved!')

    else:
        print ('Access Denied!')


field_names = ['First_Name', 'Last_Name', 'Email', 'Password']
access = 0

create_table(field_names)

First_Name = input("Enter your first name: ")
Last_Name = input("Enter your last name: ")
Email = input("Enter your Email ID: ")
Password = input("Enter your Password: ")

email(First_Name, Last_Name, Email, Password, field_names)


print("*********************Login**************************")
user = input('Enter username/email: ')
password = input('Enter password: ')

credential(user, password, access)