Hospital Database Management System with Python

The project uses the library mysql.connector

The project includes 3 files:
	
	1)database_python.py : this is the file that contains all the necessary functions
	2)database_management_system.py : this is the file that runs the main management system
	3)sql export of the created database


About:
The project implements 4 operations Create,Retrieve,Update and Delete. It also implements 4 types of login (Doctor,Staff,Patient and Management). Every login type/user type can perform the CRUD operations on various fields of various tables. Only the management login has complete access to the Database. The access to fields vary with operation and tables. Every user type doesn't have access to every table even every operation(CRUD) doesn't have the same access to fields. For example, a user may Retrieve a certain field but may not be able to Update/Create it.

Example:
A Doctor has access to Patient_Emergency table. The fields accessable to a doctor are:
	Create: ID,NAME,AGE INT,SEX,ADDRESS ,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE 
	Retrieve: ID,NAME,AGE INT,SEX,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE  (Can't view address unless he has to create the entry)
	Update: NAME,REPORT_ID,DOC_ID (The other fields can not be updated by a doctor)
	Delete: Soft delete an entry 

The Management login can access all operations across all fields in all the tables. Authorization was not implemented.  


Operations:
CRUD(Create,Retrieve,Update,Delete) was implemented

Create: 

User can only create the fields to which he has access. For example a staff can only create a report based on ID and Blood Group. Only doctors have access to rest of the fields in report.

Retrieve: 

4 types of retrieve were implemented.
* The whole table is shown
* The table is left joined with another related table(Only tables and fields the user has access to view)
* Search a specific row with Primary Key
* Retrieve based on values/range of multiple fields 
The fields that are shown are based on the acess of the user

Update:

Only row specific update was selected based on primary key. Also user can update only the tables and fields he has access to.

Delete:

Delete is also row specific and implemented based on primary key. Only management has access to hard delete a row. All other users can only soft delete.
