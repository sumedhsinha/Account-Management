"""
A MENU-DRIVEN PROGRAM WHICH COMBINES MySQL AND Python TO CREATE A DATABASE BOOKDB AND TABLE BOOK

Available functions:
1) INSERT NEW RECORDS
2) DISPLAY ALL RECORDS
3) SEARCH AND DISPLAY
4) COUNT RECORDS FILTERED BY A CATEGORY
5) COUNT RECORDS MORE THAN A CERTAIN PRICE
6) DELETE RECORD MATCHING WITH A BOOKNO
7) DELETE RECORD MATCHING WITH A BOOK NAME
8) EDIT PRICE OF A RECORD FOR A BOOKNO
"""

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="defaultuser", passwd="bookdata")
if mydb.is_connected():
    print("Connection established successfully\n")
mycur = mydb.cursor()

dbname = str(input("Please enter a name for database, default name is BOOKDB, please press enter for that: "))
if dbname == "":
    dbname = "BOOKDB"
try:
    mycur.execute("CREATE DATABASE "+dbname+"")
except:
    print("Database already exists")
mycur.execute("USE "+dbname+"")
tbname = str(input("Please enter a name for table, default name is BOOK, please press enter for that: "))
if tbname == "":
    tbname = "BOOK"

try:
    mycur.execute("CREATE TABLE "+tbname+"(Bookno int, Name varchar(25), Category varchar(10), Price Decimal(10,2), "
                                         "DOP Date) ")
except:
    print("Table already exists")


def insert_func():
    print("Columns available are: Bookno, Name, Category, Price, DOP")
    usrent1 = input("Please enter name of columns, separated by a comma [,]: ")
    usrop1 = "Y"
    while usrop1 == "Y" or usrop1 == "y":
        usrvalues1 = input("Please enter values, and please enclose name and category within quotes [\" \"]: ")
        mycur.execute("INSERT INTO "+tbname+" ("+usrent1+") VALUES("+usrvalues1+")")
        print()
        usrop1 = str(input("Do you want to add another record Y/N"))
    print("Record(s) have been added successfully")
    mydb.commit()


def display_func():
    print("Columns available are: Bookno, Name, Category, Price, DOP")
    usrent2 = input("Please enter name of columns, separated by a comma [,] press enter for all columns: ")
    if usrent2 == "":
        usrent2 = "Bookno, Name, Category, Price, DOP"
    mycur.execute("SELECT "+usrent2+" FROM "+tbname+"")
    for i in mycur.fetchall():
        print(i)


def search_display_func():
    usrop3 = "Y"
    while usrop3 == "Y" or usrop3 == "y":
        try:
            print("Columns available are: Bookno, Name, Category, Price, DOP")
            usrent3 = str(input("Please enter name of column to search on: "))
            usrvalues3 = str(input("Please enter, if on name or category, enclose within quotes [\" \"]: "))
            mycur.execute("SELECT * FROM "+tbname+" WHERE "+usrent3+" = "+usrvalues3+"")
            outlst3 = mycur.fetchall()
            if outlst3 == []:
                print("Not found")
            else:
                print(outlst3)
        except:
            print("Not found due to incorrect column name or invalid input")
        usrop3 = str(input("Do you want to search again Y/N"))


def cat_count():
    usrop4 = "Y"
    while usrop4 == "Y" or usrop4 == "y":
        try:
            usrvalues4 = str(input("Please enter category and enclose within quotes [\" \"]: "))
            mycur.execute("SELECT COUNT(*) FROM "+tbname+" WHERE Category = "+usrvalues4+"")
            outlst4 = mycur.fetchone()
            print("Number of records in category ", usrvalues4, ":", outlst4[0])
        except:
            print("Not found due to invalid input")
        usrop4 = str(input("Do you want to search again Y/N"))


def more_than_price_count():
    usrop5 = "Y"
    while usrop5 == "Y" or usrop5 == "y":
        try:
            usrvalues5 = str(input("Please enter price: "))
            mycur.execute("SELECT COUNT(*) FROM "+tbname+" WHERE Price > "+usrvalues5+"")
            outlst = mycur.fetchone()
            print("Number of records with price greater than", usrvalues5, ":", outlst[0])
        except:
            print("Not found due to invalid input")
        usrop5 = str(input("Do you want to search again Y/N"))


def search_delete_func():
    usrop6 = "Y"
    while usrop6 == "Y" or usrop6 == "y":
        try:
            print("Columns available are: Bookno, Name, Category, Price, DOP")
            usrent6 = str(input("Please enter name of column to search on: "))
            usrvalues6 = str(input("Please enter, if on name or category, enclose within quotes [\" \"]: "))
            mycur.execute("DELETE FROM "+tbname+" WHERE "+usrent6+" = "+usrvalues6+"")
            print("Record(s) successfully deleted")
        except:
            print("Not found due to incorrect column name or invalid input")
        usrop6 = str(input("Do you want to search again Y/N"))
    mydb.commit()


def edit_func():
    usrop7 = "Y"
    while usrop7 == "Y" or usrop7 == "y":
        try:
            usrvalues7 = str(input("Please enter Bookno: "))
            mycur.execute("SELECT * FROM "+tbname+" WHERE Bookno = "+usrvalues7+"")
            outlst7 = mycur.fetchall()
            if outlst7 == []:
                print("Not found")
                exit()
            else:
                print(outlst7)
        except:
            print("Not found due to incorrect column name or invalid input")
            exit()
        print("\nColumns available are: Name, Category, Price, DOP")
        try:
            usrint8 = str(input("Please enter the name of column you wish to edit: "))
            usrval8 = str(input("Please enter the new value, if name or category, enclose within quotes [\" \"]:"))
            mycur.execute("UPDATE "+tbname+" SET "+usrint8+" = "+usrval8+" WHERE Bookno = "+usrvalues7+"")
            print("Updated record is as follows: ")
            mycur.execute("SELECT * FROM "+tbname+" WHERE Bookno = "+usrvalues7+"")
            outlst8 = mycur.fetchall()
            if outlst8 == []:
                print("Not found")
            else:
                print(outlst8)
        except:
            print("Invalid input")
        usrop7 = str(input("Do you want to search again Y/N"))
    mydb.commit()


optionsforuser = int(input("Please select an option and enter its number only:"
                           "\n1 - Insert new records"
                           "\n2 - Display all records"
                           "\n3 - Search and display record(s)"
                           "\n4 - Count records with entered category"
                           "\n5 - Count records with price greater than entered value"
                           "\n6 - Delete records"
                           "\n7 - Edit records\n"))
if optionsforuser == 1:
    insert_func()
elif optionsforuser == 2:
    display_func()
elif optionsforuser == 3:
    search_display_func()
elif optionsforuser == 4:
    cat_count()
elif optionsforuser == 5:
    more_than_price_count()
elif optionsforuser == 6:
    search_delete_func()
elif optionsforuser == 7:
    edit_func()
else:
    print("Invalid input")
    exit("Program terminated")
