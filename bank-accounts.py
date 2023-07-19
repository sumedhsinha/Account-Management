"""
This is a program to create a binary file account.dat which stores bank account records.
Each record is represented as dictionary with Accno as the key and name, type_of_account (Saving, Fixed, Recurring)
and balance as fields. 

A menu driven program enables the following functions:

1) Create a binary file by taking as many records from the user
2) Display and count the number of records present in the file
3) Search and edit the record of a user given Accno
4) Search and display all Records based on user given name
5) Count all Records having balance > 500000
6) Count all records matching with a user given Type of account.
"""


import pickle
import os


def create_file(data):
    with open("account.dat", "wb") as file:
        pickle.dump(data, file)


def countndisplay():
    cnt = 0
    with open("account.dat", "rb") as file:
        reader = pickle.load(file)
        print(reader)
        for j in reader:
            cnt += 1
    return cnt


def usr_search(name):
    with open("account.dat", "rb") as file:
        reader = pickle.load(file)
        for j in reader:
            if str(reader[j][0]) == name:
                return reader[j]


def acbal_5():
    cnt = 0
    with open("account.dat", "rb") as file:
        reader = pickle.load(file)
        for j in reader:
            if float(reader[j][1]) > 500000:
                cnt += 1
    return cnt


def usrtyp_search(type_ac):
    cnt = 0
    with open("account.dat", "rb") as file:
        reader = pickle.load(file)
        for j in reader:
            if str(reader[j][2]) == type_ac:
                cnt += 1
    return cnt


def accno_search_edit(number):
    file1 = open("account.dat", "rb")
    file2 = open("temp.dat", "wb")
    read = pickle.load(file1)
    for j in read:
        if j == number:
            print(read[j])
            read[j][0] = str(input("Enter new name of account holder: "))
            read[j][2] = str(input("Enter new type of account (Saving, Fixed, Recurring): "))
            read[j][1] = float(input("Enter new balance: "))
            print(read[j])
            pickle.dump(read, file2)
        else:
            pickle.dump(read, file2)
    file1.close()
    file2.close()
    os.remove("account.dat")
    os.rename("temp.dat", "account.dat")


accountdata = {}
ac_details = []
n = int(input("Enter no of records to be entered: "))
for i in range(n):
    accno = int(input("Enter account number: "))
    print("Now, please enter details like name, type_of_account (Saving, Fixed, Recurring), balance")
    a_name = str(input("Enter name of account holder: "))
    type_of_account = str(input("Enter type of account (Saving, Fixed, Recurring): "))
    a_bal = float(input("Enter balance: "))
    ac_details = [a_name, a_bal, type_of_account]
    accountdata.update({accno: ac_details})

print("Entered records are: ", accountdata)
print("Welcome\n\nPlease select one of the options:\n1) Create above binary file by taking as many records from the "
      "user.\n2) Display and count the number of records present in the file.\n3) Search and edit the record of a user"
      " given account no.\n4) Search and display all Records based on user given name.\n5) Count all Records having "
      "balance > 500000.\n6) Count all records matching with a user given Type of account.")

op = int(input("Enter your option number: "))
if op == 1:
    create_file(accountdata)
elif op == 2:
    print("No of records: ", countndisplay())
elif op == 3:
    usrno = int(input("Enter account number to search: "))
    print("Account with account number ", usrno, "is: ", accno_search_edit(usrno))
elif op == 4:
    usrname = str(input("Enter name to search: "))
    print("Account with user name", usrname, "is: ", usr_search(usrname))
elif op == 5:
    print("No of accounts with balance more than 500000 is: ", acbal_5())
elif op == 6:
    usrtyp = str(input("Enter type of account to search: "))
    print("Account with account type", usrtyp, "is: ", usrtyp_search(usrtyp))
else:
    print("\nInvalid input")
    quit("\nProgram Terminated\n")
