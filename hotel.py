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
	                              db='hotel',
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


#-----------MODIFICATIONS
def newEmployee():

    try:
        row = {}
        print("Enter new employee's details: ")
        ID = int(input("Enter Employee ID: "))
        name = (input("Enter Name: "))
        email = input("Enter Email: ")
        h_no= int(input("Enter House Number: "))
        street = input("Enter Street Name: ")
        dob = str(input("Enter DOB (YYYY-MM-DD): "))
        gender = str(input("Enter M/F/O: "))
        phone = str(input("Enter Number: "))
        salary = int(input("Enter salary: "))
        dpt_code = int(input("Enter department code: "))
        superid = int(input("Enter Super ID: "))

        birth_date = date( int(dob[:4],int(dob[5:7]),int(dob[8:])))

        age = (date.today() - birth_date) // timedelta(days=365.2425)
        query = "INSERT INTO EMPLOYEE VALUES('%d', '%s', '%s', '%d', '%s', '%s', '%c', %s, %d, %d, %d);" % (
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

def updateEmployee():

    try:
        ID=int(input("Enter EmployeeID: "))
        entity=input("Enter which entity should be changed: ")

        value = input("Enter new value: ")

        if entity in ['email','streetAddress','dob','gender','phoneNo']:
            query = "UPDATE TABLE EMPLOYEE SET " + str(entity) + " = '" + value + "' WHERE employeeID = " + str(ID) + ";"
        else:
            query = "UPDATE TABLE EMPLOYEE SET " + str(entity) + " = " + str(value) + " WHERE employeeID = " + str(ID) + ";"

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def newBooking():

    try:
        print("Enter Booking details: \n")
        ID = int(input("Enter Booking ID: "))
        bookdate=input("Enter Date of Booking: ")
        c_in = input("Enter CheckIn Date: ")
        c_out= input("Enter CheckOut Date: ")
        n_rooms = int(input("Enter number of rooms: "))
        book_status= input("Booking Status: ")
        no_adults = int(input("Enter number of adults: "))
        no_kids = int(input("Enter number of kids: "))
        c_ID = int(input("Enter Customer ID: "))

        query = "INSERT INTO BOOKING VALUES('%d','%s','%s','%d','%s','%d','%d','%d','%s');" % (ID,bookdate,c_out,n_rooms,book_status,no_adults,no_kids,c_ID,c_in)
        cur.execute(query)
        con.commit()

        for i in range(0,n_rooms):
            #room_no=int(input("Enter ",1+i,"th room number: "))
            roomtype=input("Enter room type: ")

            query = "SELECT roomNo FROM ROOM WHERE bookingID IS NULL AND roomType='"+str(roomtype)+"';"
            cur.execute(query)
            data=cur.fetchall()
            print(" The rooms that are available are: ")
            for i in data:
                print(i["roomNo"], end =" ")
            print()

            room_no=int(input("Enter the room number: "))

            query = "UPDATE ROOM SET bookingID="+str(ID)+" WHERE roomNo="+str(room_no)+";"
            cur.execute(query)
            con.commit()


        # mode=input("Enter payment mode: ")
        # print(query)
        # cur.execute(query)
        # con.commit()

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
            query = "UPDATE TABLE BOOKING SET " + entity + " = '" + value + "' WHERE bookingID = " + str(ID) + ";"
        else:
            query = "UPDATE TABLE BOOKING SET " + entity + " = " + str(value) + " WHERE bookingID = " + str(ID) + ";"

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

def updateDependent():

    try:
        ID=int(input("Enter EmployeeID: "))
        entity=input("Enter which entity should be changed: ")

        value = input("Enter new value: ")

        
        query = "UPDATE TABLE DEPENDENT SET " + entity + " = '" + value + "' WHERE employeeID = " + str(ID) + ";"
        
        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def updateDepartmentManager():
    try:
        code = int(input("Enter Department Code: "))

        id = int(input("Enter new Manager's ID: "))

        query = "UPDATE TABLE DEPARTMENT SET managerID = " + str(id) + " departmentCode="+str(code)+";"

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
        

def newCustomer():
    try:
        print("Enter new customer's details: ")
        ID = int(input("Enter Customer ID: "))
        aadhar = str(input("Enter Cutomer Aadhar Number: "))
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        h_no= int(input("Enter House Number: "))
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        dob = str(input("Enter DOB (YYYY-MM-DD): "))
        gender = str(input("Enter gender Name: "))
        phone = str(input("Enter Number: "))
        # birth_date = date( int(dob[:4]),int(dob[5:7]),int(dob[8:]))
        # age = (date.today() - birth_date) // timedelta(days=365.2425)
        # query = "IF NOT EXISTS(SELECT * FROM AGECONVERSION WHERE DOB='" + dob + "') INSERT INTO AGECONVERSION VALUES ('" + dob + "'," + str(age) +");"
                           
        # cur.execute(query)
        # con.commit()
        
        query = "INSERT INTO CUSTOMER VALUES('%d','%s','%s','%s','%d','%s','%s','%s','%s','%s','%s');" % (
            ID, aadhar, name, email, h_no, address, city,state, dob, gender,phone,)

        print(query)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


#-----------RETRIEVALS

def deptEmployees():
    try:
        name = str(input("Enter the Department Name: "))

        query = "SELECT EMPLOYEE.employeeID, EMPLOYEE.email, DEPARTMENT.managerID from EMPLOYEE,DEPARTMENT WHERE  DEPARTMENT.departmentCode = EMPLOYEE.deptcode AND DEPARTMENT.departmentName= '"+name+"';"

        #print(query)
        cur.execute(query)
        data=cur.fetchall()

        for i in data:
            print("The EmployeeID is: "+str(i["employeeID"]))
            print("The EmailID is: "+i["email"])
            print("The ManagerID is: "+str(i["managerID"]))
            print("  ---- \n")
        
    except Exception as e:
        con.rollback()
        #print("Failed to display from database")
        print(">>>>>>>>>>>>>", e)

    return
    
def dateBookings():
    try:
        date = str(input("Enter required Date: "))

        query = "SELECT * FROM BOOKING WHERE dobooking = '"+date+"';"

        cur.execute(query)
        data=cur.fetchall()

        for i in data:
            print("Booking ID: "+str(i["bookingID"]))
            print("Customer ID: "+str(i["customerID"]))
            print("Booking Status: "+str(i["booking_Status"]))
            print("No Of Rooms: "+str(i["num_rooms"]))
            print("---- \n")

    except Exception as e:
        con.rollback()
        print(">>>>>>>>>>>>>", e)

    return

def customerInfo():
    try:
        name = str(input("Enter customer name: "))

        query = "SELECT * FROM CUSTOMER WHERE customerName = '"+name+"';"
        
        #print(query)
        cur.execute(query)
        data=cur.fetchall()

        for i in data:
            print("CustomerID: "+str(i["customerID"]))
            print("Customer AadharID: "+str(i["aadharID"]))
            print("Customer Name: "+str(i["customerName"]))
            print("Customer Email: "+str(i["email"]))
            print("Customer Address: "+str(i["address"])+","+str(i["city"])+","+str(i["state"])+","+str(i["country"]))
            print("Customer Gender: "+str(i["gender"]))
            print("Customer Phone: "+str(i["phoneNo"]))
            print("---- \n")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def priceRooms():
    try:
        price = int(input("Rooms below what price? "))

        query = "SELECT roomType FROM ROOMCLASS WHERE pricePerNight < "+str(price)+";"
        #print(query)
        print("Rooms below the price are:")
        cur.execute(query)
        data=cur.fetchall()
        for i in data:
            print("-> "+i["roomType"])
    
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def yearSum():
    try:
        year = int(input("Enter year for sum "))
        query= "SELECT SUM(price) from BOOKING WHERE YEAR(dobooking) = "+str(year)+";"
        print(query)
        cur.execute(query)
        data=cur.fetchall()
        print(data)

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def service():
    try:
        ID=int(input("Enter Service ID: "))
        room_no=int(input("Enter Room Number: "))
        
        print("Enter Type of Service")
        print("1. Restaurant")
        print("2. Recreational")
        print("3. Cab")
        choice = int(input())
        price = int(input("Enter Price: "))
        query = "INSERT INTO SERVICE VALUES("+str(ID)+","+str(room_no)+","+str(price)+");"
        cur.execute(query)
        con.commit()
        if choice==1:
            dish_code=int(input("Enter Dish Code: "))
            request = input("Any Special Requests? ")

            query = "INSERT INTO RESTAURANT VALUES("+str(ID)+","+str(dish_code)+",'"+str(request)+"');"
            cur.execute(query)
            con.commit()
        elif choice==2:
            activity_type=str(input("Enter Activity Type: "))
            no_people = int(input("Number of People"))

            query = "INSERT INTO RECSERVICE VALUES("+str(ID)+",'"+str(activity_type)+"',"+str(no_people)+");"
            cur.execute(query)
            con.commit()
        elif choice==3:
            activity_type=str(input("Enter Cab Details: "))
            no_people = int(input("Number of People travelling:"))

    except Exception as e:
        con.rollback()

        print(">>>>>>>>>>>>>", e)
    return

################

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        newCustomer()
    elif(ch == 2):
        newBooking()
    elif(ch == 3):
        updateBooking()
    elif(ch == 4):
        dateBookings()
    elif (ch==5):
        customerInfo()
    elif (ch==6):
        priceRooms()
    elif (ch==7):
        newEmployee()
    elif (ch==8):
        updateEmployee()
    elif (ch==9):
        deleteEmployee()
    elif (ch==10):
        newDependent()
    elif (ch==11):
        updateDependent()
    elif (ch==12):
        deptEmployees()
    elif (ch==13):
        updateDepartmentManager()
    elif (ch==14):
        yearSum()
    elif (ch==15):
        service()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hardcode username and password
    #username = input("Username: ")
    #password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              password="Harsh!t18",
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
                print("1. New Customer")  
                print("2. New Booking")  
                print("3. Update Booking")
                print("4. All Bookings Under a Date")
                print("5. Customer Information")
                print("6. Rooms Under a Price")
                print("7. New Employee")  
                print("8. Update Employee Details")
                print("9. Delete Employee Details")
                print("10. New Dependent")
                print("11. Update Dependent")
                print("12. All Employees Under a Department")
                print("13. Update Department Manager")
                print("14. Analysis of Sum of all Bookings in a Year")
                print("15. Services")
                
                print("16. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 16:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")