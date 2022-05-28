# Hospital Database Management System with Python

A simple CRUD based SQL database management system with python.

## Description
The project implements 4 operations Create,Retrieve,Update and Delete. It also implements 4 types of login (Doctor,Staff,Patient and Management). Every login type/user type can perform the CRUD operations on various fields of various tables. Only the management login has complete access to the Database. The access to fields vary with operation and tables. Every user type doesn't have access to every table even every operation(CRUD) doesn't have the same access to fields. For example, a user may Retrieve a certain field but may not be able to Update/Create it. The project uses the library mysql.connector.

The project includes 3 files:
	
	1)database_python.py : this is the file that contains all the necessary functions
	2)database_management_system.py : this is the file that runs the main management system
	3)sql export of the created database

Example:
A Doctor has access to Patient_Emergency table. The fields accessable to a doctor are:
	Create: ID,NAME,AGE INT,SEX,ADDRESS ,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE 
	Retrieve: ID,NAME,AGE INT,SEX,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE  (Can't view address unless he has to create the entry)
	Update: NAME,REPORT_ID,DOC_ID (The other fields can not be updated by a doctor)
	Delete: Soft delete an entry 

The Management login can access all operations across all fields in all the tables. Authorization was not implemented.  


### Operations
CRUD(Create,Retrieve,Update,Delete) was implemented

### Create 

User can only create the fields to which he has access. For example a staff can only create a report based on ID and Blood Group. Only doctors have access to rest of the fields in report.

### Retrieve

4 types of retrieve were implemented.
* The whole table is shown
* The table is left joined with another related table(Only tables and fields the user has access to view)
* Search a specific row with Primary Key
* Retrieve based on values/range of multiple fields 
The fields that are shown are based on the acess of the user

### Update

Only row specific update was selected based on primary key. Also user can update only the tables and fields he has access to.

### Delete

Delete is also row specific and implemented based on primary key. Only management has access to hard delete a row. All other users can only soft delete.


# VIEWS

doctor_view CREATE Patient_Outdoor           ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE
doctor_view CREATE Patient_Emergency         ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,ROOM_NO,DOC_ID,VISIT_DATE
doctor_view CREATE Patient_Admission         ID,NAME,AGE,SEX,ADDRESS,WARD,ROOM_NO,BED_NO,REPORT_ID,CONTACT,DOC_ID,ADMIT_DATE
doctor_view CREATE Medicine                  ID,NAME,AVAILIBILITY,COMPANY,EXPIRY_DATE
doctor_view CREATE Report                    ID,BLOOD_TYPE,SYMPTOMPS,DIAGNOSIS,MEDICINES


doctor_view RETRIEVE Patient_Outdoor         ID,NAME,AGE,SEX,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE
doctor_view RETRIEVE Patient_Emergency       ID,NAME,AGE,SEX,REPORT_ID,CONTACT,ROOM_NO,DOC_ID,VISIT_DATE
doctor_view RETRIEVE Patient_Admission       ID,NAME,AGE,SEX,WARD,ROOM_NO,BED_NO,REPORT_ID,CONTACT,DOC_ID,ADMIT_DATE
doctor_view RETRIEVE Medicine                ID,NAME,AVAILIBILITY,COMPANY,EXPIRY_DATE
doctor_view RETRIEVE Report                  ID,BLOOD_TYPE,SYMPTOMPS,DIAGNOSIS,MEDICINES
doctor_view RETRIEVE Doctor         	     ID,NAME,SEX,CONTACT,DEPT,ROOM_NO,FEE
doctor_view RETRIEVE Staff         	     ID,NAME,SEX,DUTY,SHIFT
doctor_view RETRIEVE Building         	     ID,ADDRESS,DEPTS
doctor_view RETRIEVE Room         	     ID,BUILDING_ID,DEPT_NAME
doctor_view RETRIEVE Machines         	     NAME,ROOM_ID


doctor_view UPDATE Patient_Outdoor           ID,REPORT_ID,DOC_ID
doctor_view UPDATE Patient_Emergency         ID,REPORT_ID,ROOM_NO,DOC_ID
doctor_view UPDATE Patient_Admission         ID,ROOM_NO,BED_NO,REPORT_ID,CONTACT,DOC_ID,ADMIT_DATE
doctor_view UPDATE Medicine         	     ID,NAME,AVAILIBILITY,COMPANY,EXPIRY_DATE
doctor_view UPDATE Report         	     ID,BLOOD_TYPE,SYMPTOMPS,DIAGNOSIS,MEDICINES


staff_view CREATE Patient_Outdoor            ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE
staff_view CREATE Patient_Emergency          ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,ROOM_NO,DOC_ID,VISIT_DATE
staff_view CREATE Patient_Admission          ID,NAME,AGE,SEX,ADDRESS,WARD,ROOM_NO,BED_NO,REPORT_ID,CONTACT,DOC_ID,ADMIT_DATE
staff_view CREATE Report         	     ID,BLOOD_TYPE


staff_view RETRIEVE Patient_Outdoor          ID,NAME,AGE,SEX,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE
staff_view RETRIEVE Patient_Emergency        ID,NAME,AGE,SEX,REPORT_ID,CONTACT,ROOM_NO,DOC_ID,VISIT_DATE
staff_view RETRIEVE Patient_Admission        ID,NAME,AGE,SEX,ADDRESS,WARD,ROOM_NO,BED_NO,REPORT_ID,CONTACT,DOC_ID,ADMIT_DATE
staff_view RETRIEVE Medicine         	     ID,NAME,AVAILIBILITY,COMPANY,EXPIRY_DATE
staff_view RETRIEVE Report         	     ID,BLOOD_TYPE,MEDICINES
staff_view RETRIEVE Doctor         	     ID,NAME,SEX,CONTACT,DEPT,ROOM_NO,FEE
staff_view RETRIEVE Staff         	     ID,NAME,SEX,DUTY,SHIFT
staff_view RETRIEVE Building         	     ID,ADDRESS,DEPTS
staff_view RETRIEVE Room         	     ID,BUILDING_ID,DEPT_NAME,AVAILIBITY,FEES
staff_view RETRIEVE Machines        	     NAME,ROOM_ID


staff_view UPDATE Patient_Outdoor            ID,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE
staff_view UPDATE Patient_Emergency          ID,REPORT_ID,CONTACT,ROOM_NO,DOC_ID,VISIT_DATE
staff_view UPDATE Patient_Admission          ID,WARD,ROOM_NO,BED_NO,REPORT_ID,DOC_ID,ADMIT_DATE
staff_view UPDATE Report         	     ID,BLOOD_TYPE
staff_view UPDATE Doctor         	     ID,DEPT,ROOM_NO,FEE
staff_view UPDATE Staff         	     ID,NAME,SEX,DUTY,SHIFT


patient_view RETRIEVE Patient_Outdoor        NAME,SEX,CONTACT,VISIT_DATE
patient_view RETRIEVE Patient_Emergency      NAME,SEX,REPORT_ID,DOC_ID
patient_view RETRIEVE Patient_Admission      NAME,SEX,REPORT_ID,DOC_ID
patient_view RETRIEVE Building         	     ID,ADDRESS,DEPTS
patient_view RETRIEVE Report         	     ID,BLOOD_TYPE,MEDICINES 


patient_view UPDATE Patient_Outdoor          NAME,AGE,SEX,ADDRESS,CONTACT
patient_view UPDATE Patient_Emergency        NAME,AGE,SEX,ADDRESS,CONTACT
patient_view UPDATE Patient_Admission        NAME,AGE,SEX,ADDRESS,CONTACT 


management_view CREATE Patient_Outdoor       ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE
management_view CREATE Patient_Emergency     ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,ROOM_NO,DOC_ID,VISIT_DATE
management_view CREATE Patient_Admission     ID,NAME,AGE,SEX,ADDRESS,WARD,ROOM_NO,BED_NO,REPORT_ID,CONTACT,DOC_ID,ADMIT_DATE
management_view CREATE Report         	     ID,BLOOD_TYPE,SYMPTOMPS,DIAGNOSIS,MEDICINES
management_view CREATE Doctor         	     ID,NAME,SEX,CONTACT,ADDRESS,DEPT,ROOM_NO,FEE,DEGREE
management_view CREATE Staff         	     ID,NAME,SEX,CONTACT,ADDRESS,BUILDING_ID,DUTY,SHIFT,WAGE
management_view CREATE Vehicle         	     NUM_PLATE,BRAND,MODEL,PURPOSE,BUILDING_ID
management_view CREATE Medicine              ID,NAME,AVAILIBILITY,COMPANY,EXPIRY_DATE
management_view CREATE Building              ID,ADDRESS,ROOM_NUM,MACHINE_NUM,VEHICLE_NUM,DOCTOR_NUM,DEPTS
management_view CREATE Room         	     ID,BUILDING_ID,DEPT_NAME,AVAILIBITY,FEES
management_view CREATE Machines              ID,NAME,ROOM_ID 


management_view RETRIEVE Patient_Outdoor     ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE
management_view RETRIEVE Patient_Emergency   ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,ROOM_NO,DOC_ID,VISIT_DATE
management_view RETRIEVE Patient_Admission   ID,NAME,AGE,SEX,ADDRESS,WARD,ROOM_NO,BED_NO,REPORT_ID,CONTACT,DOC_ID,ADMIT_DATE
management_view RETRIEVE Report              ID,BLOOD_TYPE,SYMPTOMPS,DIAGNOSIS,MEDICINES
management_view RETRIEVE Doctor              ID,NAME,SEX,CONTACT,ADDRESS,DEPT,ROOM_NO,FEE,DEGREE
management_view RETRIEVE Staff               ID,NAME,SEX,CONTACT,ADDRESS,BUILDING_ID,DUTY,SHIFT,WAGE
management_view RETRIEVE Vehicle             NUM_PLATE,BRAND,MODEL,PURPOSE,BUILDING_ID
management_view RETRIEVE Medicine            ID,NAME,AVAILIBILITY,COMPANY,EXPIRY_DATE
management_view RETRIEVE Building            ID,ADDRESS,ROOM_NUM,MACHINE_NUM,VEHICLE_NUM,DOCTOR_NUM,DEPTS
management_view RETRIEVE Room         	     ID,BUILDING_ID,DEPT_NAME,AVAILIBITY,FEES
management_view RETRIEVE Machines            ID,NAME,ROOM_ID 


management_view UPDATE Patient_Outdoor       ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,DOC_ID,VISIT_DATE,DEL
management_view UPDATE Patient_Emergency     ID,NAME,AGE,SEX,ADDRESS,REPORT_ID,CONTACT,ROOM_NO,DOC_ID,VISIT_DATE,DEL
management_view UPDATE Patient_Admission     ID,NAME,AGE,SEX,ADDRESS,WARD,ROOM_NO,BED_NO,REPORT_ID,CONTACT,DOC_ID,ADMIT_DATE,DEL
management_view UPDATE Report         	     ID,BLOOD_TYPE,SYMPTOMPS,DIAGNOSIS,MEDICINES,DEL
management_view UPDATE Doctor         	     ID,NAME,SEX,CONTACT,ADDRESS,DEPT,ROOM_NO,FEE,DEGREE,DEL
management_view UPDATE Staff                 ID,NAME,SEX,CONTACT,ADDRESS,BUILDING_ID,DUTY,SHIFT,WAGE,DEL
management_view UPDATE Vehicle         	     NUM_PLATE,BRAND,MODEL,PURPOSE,BUILDING_ID,DEL
management_view UPDATE Medicine              ID,NAME,AVAILIBILITY,COMPANY,EXPIRY_DATE,DEL
management_view UPDATE Building              ID,ADDRESS,ROOM_NUM,MACHINE_NUM,VEHICLE_NUM,DOCTOR_NUM,DEPTS,DEL
management_view UPDATE Room         	     ID,BUILDING_ID,DEPT_NAME,AVAILIBITY,FEES,DEL
management_view UPDATE Machines              ID,NAME,ROOM_ID,DEL
