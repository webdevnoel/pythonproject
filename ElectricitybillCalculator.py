import mysql.connector
from datetime import date
print("=-"*44)
print("\n   =-=-=--=-=-=ELECTRICITY BILL-=-=-=-=-=-=-   ")

print("\nPlease wait the connection is being established…")

mydb=mysql.connector.connect(user="new_user",passwd="123",host="localhost")

if mydb.is_connected():
    print("\nConnection successful\n")
else:
    print("\nConnection failed\n")

mycursor = mydb.cursor()

# DATABASE CREATION AND USING
mycursor.execute("SHOW DATABASES;")


dataBaseExists = False

for x in mycursor:
    if x[0] == 'electricity_bill':
        dataBaseExists = True
        break

if dataBaseExists:
    q = mycursor.fetchall()
    mycursor.execute("use electricity_bill")
    print("using electricity billl")
else:
    mycursor.execute("CREATE DATABASE electricity_bill;")
    mycursor.execute("USE electricity_bill")
    print("created electricity_bill")

# REQUIRED TABLE CREATION AND USING
mycursor.execute("CREATE TABLE bill_data(billno integer primary key,customer_name varchar(25),customers_address varchar(45),total_units integer,total_bill integer,date date, due_date date)")

mycursor.execute("SHOW TABLES;")
billdataExists = False 

for x in mycursor:
    print(x)
    if x[0] == "bill_data":
        billdataExists = True
        print("presesnt")
 
if billdataExists:
    print("table exists")
else:
    mycursor.execute("CREATE TABLE bill_data(billno integer primary key,customer_name varchar(25),customers_address varchar(45),total_units integer,total_bill integer,date date, due_date date)")
    print("table created")
    

# ADDING SOME DATA TO DATABASE

mycursor.execute("insert into bill_data values(1000,'Hester Lutz','Kochi Kerala 682016',55,232,'2022-12-09','2022-12-30')")
mycursor.execute("insert into bill_data values(1001,'Terrie Mayo','Muvattupuzha 686662',678,7728, '2022-12-12','2022-11-12')")
mycursor.execute("insert into bill_data values(1002,'Vickie Matthews','Kochi, Kerala 682016',128,643,'2023-03-01','2023-03-30')")
mycursor.execute("insert into bill_data values(1003,'Erna Webb','koothattukulam 686664',201,1996,'2023-04-21','2023-03-30')")
mycursor.execute("insert into bill_data values(1004,'Charlotte Cox','Kochi, Kerala 682011',305,2144,'2023-09-27','2023-10-30')")
mycursor.execute("insert into bill_data values(1005,'Gordon morse','koothattukulam,686664',465,4541,'2023-11-17','2023-10-30')")
mycursor.execute("insert into bill_data values(1006,'Corrine Franco','Elanji, 686665',198,1231,'2023-01-10','2023-02-28')")
mycursor.execute("insert into bill_data values(1007,'Walton Petty','mutholapuram,686666',305,2144,'2023-06-14','2023-06-30')")
mycursor.execute("insert into bill_data values(1008,'Leanne Holloway','Kochi, Kerala 682016',904,9758,'2023-11-03','2023-10-30')")
mycursor.execute("insert into bill_data values(1009,'Freda Fritz','Kochi, Kerala 682016',523,4772,'2023-03-01','2023-04-30')")
mycursor.execute("insert into bill_data values(1010,'Bonita Hinton','Muvattupuzha 686662',99,404,'2023-09-27','2023-10-30')")
mycursor.execute("insert into bill_data values(1011,'Raquel Romer','Elanji 686665',128,643,'2023-03-30','2023-04-30')")
mycursor.execute("insert into bill_data values(1012,'Douglas Dawson','koothattukulam,686664',465,4541,'2023-04-12','2023-04-30')")

mydb.commit()


# MAIN FUNCTIONALITY
while True:
    print("=-=-=-PLEASE CHOOSE YOUR OPTIONS=-=-=-")
    print("Enter 'ADD' to Add data of a customer")
    print("Enter 'DELETE' to delete data of a  customer")
    print("Enter 'UPDATE' to edit data of a customer")
    print("Enter 'DETAILS' to get requierd details : ")

    choice = input("Enter your choice:") 
    # ADDING A NEW BILL
    if choice == "ADD" :
        if choice == "ADD":
            billno = int(input("Enter the bill number :"))
            CustomerName = str(input("Enter the name of the customer:"))
            address = str(input("Enter the address of the customer:"))
            unit = int(input("Enter the units used by the customer:"))
            year = int(input("Enter year:"))
            month = int(input("Enter the month"))
            day = int(input("Enter the day"))
            currentDate = date(year,month,day)
            print(currentDate)

            dueYear = int(input("Enter due year:"))
            dueMonth = int(input("Enter the due month:"))
            dueDay = int(input("Enter the due day:"))
            dueDate = date(dueYear, dueMonth, dueDay)
            print(dueDate)

            if dueDate < currentDate:
                days = (currentDate - dueDate).days
                print("You are", days, "late")
                fine = days*30
                print("Your fine is", fine, " rupees")
            else:
                print("The customer has paid the bill on time")
            # IF UNIT IS LESS THAN 100
            if unit<=100:
                if dueDate < currentDate:
                    f=int(input("Enter the fine to be paid:"))
                    bill=unit*3.5 + f
                    print("Bill=",bill)
                else:
                    bill=unit*3.5
                    print("Bill=",bill)
            # IF UNIT IS BETWEEN 101 AND 300
            elif unit>=101 and unit<=300:
                if dueDate < currentDate:
                    f = int(input("Enter the fine to be paid:"))
                    bill = 350+((unit-100)*7.5)+ f
                    print("Bill=",bill)
                else:
                    bill = 350+((unit-100)*7.5)
                    print("Bill=",bill)
            # IF UNIT IS BETWEEN 301 AND 500
            elif unit>=301 and unit<=500:
                if dueDate < currentDate:
                    f = int(input("Enter the fine to be paid:"))
                    bill = 350+1500+((unit-300)*10) +  f
                    print("Bill=",bill) 
                else:
                    bill=350+1500+((unit-300)*10)
                    print("Bill=",bill)
            # IF UNIT IS GREATER THAN 500
            elif unit>500:
                if dueDate < currentDate:
                    f = int(input("Enter the fine to be paid:"))
                    bill = 350+1500+2000+((unit-500)*12) + f
                    print("Bill=",bill)
                else:
                    bill=350+1500+2000+((unit-500)*12)
                    print("Bill=",bill)
            else:
                print("There is an error")
            # METER RENT CALCULATION
            bill = bill + 14.28
            print("Bill after adding meter rent:", bill)
            # TAX ADDITION
            bill = bill + (bill*0.12)
            print("Total bill after tax:",bill)
            mycursor.execute("insert into bill_data values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(billno,CustomerName,address,unit,bill,currentDate,dueDate))
            mydb.commit()
    # DELETING A BILL
    elif choice == 'DELETE':
        billNumber = int(input("Enter the bill number: "))
        mycursor.execute("delete from bill_data where billno={}".format(billNumber))
        print("Record deleted")
    # UPDATEING BILL    
    elif choice == "UPDATE":
        print("=-=-=-=YOUR OPTIONS=-=-=-=")
        print("1. To update the name ")
        print("2. To update the address")
        print("3.To update the unit used")
        choice2 = int(input("Enter the choice:"))
        if choice2 == 1:
            billNumber = input("Enter the bill number:")
            billNumber = '"'+billNumber+'"'
            name = input("Enter the new name:")
            name = '"'+name+'"'
            query="update bill_data SET customer_name={0} where billno={1}".format(name, billNumber)
            mycursor.execute(query)
            print("Record updated")
            mydb.commit()
            mydb.close()
        elif choice2 == 2:
            billNumber = input("Enter the bill number:")
            billNumber = '"'+billNumber+'"'
            newAddress = input("Enter the new address:")
            newAddress = '"'+newAddress+'"'
            mycursor.execute("update bill_data set customers_address={0} where billno={1}".format(newAddress,billNumber))
            print("Record updated")
            mydb.commit()
            mydb.close()
        elif choice2 == 3:
            billNumber = input("Enter the bill number: ")
            mycursor.execute("select billno from bill_data")
            rec = mycursor.fetchall()
            for i in rec:
                if str(billNumber) in str(i):
                    billNumber = (input("Please re-enter the bill number:"))
                    billNumber = '"'+billNumber+'"'
                    print(billNumber)
                    unit = int(input("Enter the new units:"))
                    if unit<=100:
                        bill=unit*3.5
                    elif unit>=101 and unit<=300:
                        bill=350+((unit-100)*7.5)
                    elif unit>=301 and unit<=500:
                        bill=350+1500+((unit-300)*10)
                    elif unit>500:
                        bill=350+1500+2000+((unit-500)*12)
                    mycursor.execute("update bill_data set total_units={0}, total_bill={1} where billno={2}".format(unit, bill, billNumber))
                    print("Record updated")
                    mydb.commit()
    # GETTING DETAILS
    elif choice == "DETAILS":
        billno = int(input("Enter the bill number:"))
        mycursor.execute("select * from bill_data where billno={}".format(billno))
        rec = mycursor.fetchall()
        for i in rec:
            print(i)
        mydb.commit()
    else:
        print("Invalid choice check the details")
    c = input("Do you want to continue(yes/no):")
    if c == "yes":
        print("Please choose your next choice")
        continue
    else:
        mydb.commit()
        mydb.close()
        break
