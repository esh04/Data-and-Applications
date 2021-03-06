# Data-and-Applications
The mini-world is a Hotel Management System where we implement a database to efficiently record and manage the different crucial aspects required to successfully run a hotel. We record bookings, their payment statuses and the party who was responsible for the booking with their credentials. We store information regarding the type of room which was booked and the employees who are responsible for maintaining the standards of the room and organization of the hotel. The recording is also made of the different types of services offered by the hotel to its customers. For effective workforce management, we store all employees including their dependents. 

Link to the demo: https://iiitaphyd-my.sharepoint.com/:v:/g/personal/adith_r_research_iiit_ac_in/ESdgn9ussxhEsuv6riHUsFIBq5UM1WE1SeoJC-0bt11Xrg?e=XvnwGa

## Requirements
- PyMySql python module
  - `pip install PyMySQL`
- MySQL Server
    - Windows: https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/windows-install-archive.html
    - Ubuntu: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04
    - Mac: https://database.guide/how-to-install-sql-server-on-a-mac/
## How To USe
- `mysql -u <Your MySQL UserName> -p < dump.sql`
- `python3 hotel.py`

## Functionalities Provided
After logging in, the following funcitonalities would be provided to the user:

![img](https://media.discordapp.net/attachments/825048469872836638/902605891839336569/Screenshot_from_2021-10-26_22-42-08.png)

### Description of each function:
1. Add details of a new customer into the table name `CUSTOMER` 
2. Record details of a new booking made by a customer into table name 'BOOKING'
3. Update a pre-existing booking in the table name `BOOKING`
4. Display all the data from table name `BOOKING` available under a particular date 
5. Display the details of a specific customer from the table `CUSTOMER`
6. Display all the rooms that can be booked under a certain price from the table `ROOM` 
7. Add details of a new employee into table `EMPLOYEE`
8. Update the details of a pre-existing employee
9. Delete the records of an employee from the table `EMPLOYEE`
10. Add a new dependent for an existing employee
11. Update the details of any dependent of an existing employees from the table `EMPLOYEE`
12. Display all the employees that are working under a specific department from the table `DEPARTMENT`
13. Update the manager of a department 
14. Handling of requests and services offered from tables `SERVICE` and view the same in `RECSERVICE`, `CAB`, `RESTAURANT`
15. Logout from the server 
