"""
This program creates a CSV file to store employee records by accepting employee no, name and basic salary from user till user wants.
Furthermore it calculates deduction as 5% of basic salary, allowance = 2000 and net salary = basic salary + allowance - deduction. The program should provide the following menu option

Following functions are available:
Create CSV file
Display contents
Count number of records
Search on employee no
Search on Name
"""

import csv


def createFile():
    n = int(input('Enter Number of employees: '))
    records = [['Number','Name','Basic Salary','Deduction','Allowance','Net Salary']]
    for i in range(n):
        record = [int(input('Enter Employee Number: ')),input('Enter Employee Name: '),float(input('Enter Employee Basic salary: '))]
        record.append(0.05*record[2])
        record.append(2000)
        record.append(record[2]-record[3]+record[4])
        records.append(record)
    with open('Report.csv','w',newline = '') as fout:
        w = csv.writer(fout)
        w.writerows(records)
        print('Report.csv generated')

def displayData():
    try:
        with open('Report.csv','r') as fin:
            r = csv.reader(fin)
            for row in r:
                print(row)

    except:
        print('Report.csv not found')

def countRecords():
    try:
        with open('Report.csv','r') as fin:
            r = csv.reader(fin)
            first = True
            c = 0
            for row in r:
                if first:
                    first = False
                    continue
                c += 1
            print('There are',c,'records in file')
    except:
        print('Report.csv not found')

def search(v,i):
    try:
        with open('Report.csv','r') as fin:
            r = csv.reader(fin)
            for row in r:
                if row[i] == v:
                    print(row)
    except:
        print('Report.csv not found')

def searchNo():
    search(input('Enter Employee Number to be searched: '),0)

def searchName():
    search(input('Enter Employee Name to be searched: '),1)

while True:
    print('''1. Create csv file
2. Display contents
3. Count number of records
4. Search on employee no
5. Search on Name
''')
    ch = str(input('Choose an option: '))
    if ch == '1':
        createFile()
    elif ch == '2':
        displayData()
    elif ch == '3':
        countRecords()
    elif ch == '4':
        searchNo()
    elif ch == '5':
        searchName()
    else:
        print('Invalid choice')

    ch = input('Continue? (Y/N)')
    if ch not in 'yY':
        break
