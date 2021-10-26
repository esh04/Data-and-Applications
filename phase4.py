import subprocess as sp
import pymysql
import pymysql.cursors
import time
from datetime import date, timedelta

#--------------------LOGGING INTO THE DB
def login():
	tmp = sp.call('clear', shell=True)
	print("LOG IN TO THE SQL SERVER");
	global con
	username = input("Username: ")
	password = input("Password: ")
	try:
		con = pymysql.connect(host='localhost',
	                              user=username,
	                              password=password,
	                              db='RealEstate',
	                              cursorclass=pymysql.cursors.DictCursor)
		global cur
		cur = con.cursor()
	except:
		print()
		print("Failed,Please TRY AGAIN!")
		input("Press Enter to continue")
		login()

#------------CUSTOMARY OUTPUT
def main_output():
	tmp = sp.call('clear', shell=True);
	print("\t\t------------------------------------------------------------------------------------")
	print("\t\t                             WELCOME TO THE HOTEL DB                             ")
	print("\t\t------------------------------------------------------------------------------------")
	print();print();


'''
    new booking
    new customer
    new service order
    add new employee
    remove employee
    update details of employee
    new dependant
    
'''
#--------TASKS

def newEmployee():
    
    try:
        row = {}
        print("Enter new employee's details: ")
        ID = int(input("Enter Employee ID"))
        name = (input("Enter Name"))
        email = input("Enter Email")
        h_no= int(input("Enter House Number"))
        street = input("Enter Street Name")
        dob = str(input("Enter DOB (YYYY-MM-DD) "))
        gender = str(input("Enter M/F/O"))
        phone = str(input("Enter Number"))
        salary = int(input("Enter salary"))
        dpt_code = int(input("Enter department code"))
        superid = int(input("Enter Super ID"))

        birth_date = date( int(dob[:4],int(dob[5:7]),int(dob[8:])))
        
        age = (date.today() - birth_date) // timedelta(days=365.2425)
        query = "INSERT INTO EMPLOYEE VALUES('%d', '%s', '%s', '%d', '%s', '%s', '%c', %s, %d, %d, %d)" % (
            ID, name, email, h_no, street, dob, gender, phone, salary, dpt_code, superid)

        
        print(query)
        cur.execute(query)
        con.commit()
        
                           
##    
##        query = "IF NOT EXISTS(SELECT * FROM AGECONVERSION WHERE DOB='" + dob + "') INSERT INTO AGECONVERSION VALUES ('" + dob + "'," + str(age) +");"
##                           
##
##        cur.execute(query)
##        con.commit()
##                        
##*******check if this is even neccessary**********

        
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def deleteEmployee():
    try:
        ID = int(input("Enter Employee ID"))
        query = "DELETE FROM EMPLOYEE WHERE employeeID = ",ID,";"
        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted Employee from Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def newBooking():

    try:
        ID = int(input("Enter Booking ID"))
        bookdate=input("Enter Date of Booking")
        c_in = input("Enter CheckIn Date")
        c_out= input("Enter CheckOut Date")
        n_rooms = int(input("Enter number of rooms"))
        book_status= input("Booking Status:")
        no_adults = int(input("Enter number of adults"))
        no_kids = int(input("Enter number of kids"))
        c_ID = int(input("Enter Customer ID"))

        query = "INSERT INTO BOOKING VALUES('%d','%s','%s','%s','%d','%s','&d','%d','%d')" % (ID,bookdate,c_in,c_out,n_rooms,book_status,no_adults,no_kids,c_ID)

        for i in range(0,n_rooms):
            room_no=int(input("Enter ",1+i,"th room number: "))
            roomtype=input("Enter room type: ")

            ####Query to somehow link the bookingid in room to booking id in booking table

        mode=input("Enter payment mode: ")
        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def updateBooking():

    try:
        ID=int(input("Enter BookingID: "))
        entity=input("Enter which entity should be changed: ")

        value = input("Enter new value: ")

        if entity in ['dobooking','checkin','checkout','bookingstatus']:
            query = "UPDATE TABLE BOOKING SET " + entity + " = '" + value + "' WHERE bookingID = " + str(ID)
        else:
            query = "UPDATE TABLE BOOKING SET " + entity + " = " + str(value) + " WHERE bookingID = " + str(ID)

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
    
def newDependent():
    try:
        ID = int(input("Enter the Employee ID"))

        name = input("Enter the dependent name: ")
        dob = input("Enter the dependent DOB: ")
        no = str(input("Enter the phone number: "))

        query = "INSERT INTO DEPENDENT VALUES( '"+name+"',"+ID+",'"+dob+"','"+str(no)+"');"

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        newBooking()
    elif(ch == 2):
        updateBooking()
    elif(ch == 3):
        newEmployee()
    elif(ch == 4):
        deleteEmployee()
    elif (ch==5):
        newDependent()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="password",
                              db='hotel',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. New Booking")  # Hire an Employee
                print("2. Update Booking")  # Fire an Employee
                print("3. New Employee")  # Promote Employee
                print("4. Delete Employee")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
