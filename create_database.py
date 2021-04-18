import mysql.connector

def connect2server(server_name,password=""):
	connection = mysql.connector.connect(host="localhost",user="root",passwd=password,database=server_name )
	cursor = connection.cursor()
	return connection,cursor

def table_exists(table,cursor):
	query ="SHOW TABLES LIKE '{}';".format(table)
	cursor.execute(query)
	if len(cursor.fetchall()) == 0:
		return False
	else:
		return True

connection,cursor = connect2server("medical database")

ID = list(range(10))
NAME = ["Sadman", "Sakib","Fahim","Salman"]
AGE = [18,20,50,60]
SEX = ["MALE","FEMALE"]
ADDRESS = ["DHAKA","SYLHET","CHITTAGONG"]
DATE = ["21-1-1","20-2-2","20-3-3"]

Patient_Outdoor_TableSql = """CREATE TABLE Patient_Outdoor(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  VARCHAR(100) NOT NULL,
AGE INT(3),
SEX CHAR(10),
ADDRESS VARCHAR(100),
REPORT_ID INT(20),
FOREIGN KEY(REPORT_ID) REFERENCES Report(ID) ON DELETE CASCADE ON UPDATE CASCADE,
CONTACT VARCHAR(15),
DOC_ID INT(20),
FOREIGN KEY(DOC_ID) REFERENCES Doctor(ID) ON DELETE CASCADE ON UPDATE CASCADE,
VISIT_DATE DATE, 
DEL BOOLEAN DEFAULT FALSE)"""

Patient_Emergency_TableSql = """CREATE TABLE Patient_Emergency(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  VARCHAR(100) NOT NULL,
AGE INT(3),
SEX CHAR(10),
ADDRESS VARCHAR(100),
REPORT_ID INT(20),
FOREIGN KEY(REPORT_ID) REFERENCES Report(ID) ON DELETE CASCADE ON UPDATE CASCADE,
CONTACT VARCHAR(15),
DOC_ID INT(20),
FOREIGN KEY(DOC_ID) REFERENCES Doctor(ID) ON DELETE CASCADE ON UPDATE CASCADE,
VISIT_DATE DATE, 
DEL BOOLEAN DEFAULT FALSE)"""


Patient_Admission_TableSql = """CREATE TABLE Patient_Admission(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  VARCHAR(100) NOT NULL,
AGE INT(3),
SEX CHAR(10),
ADDRESS VARCHAR(100),
WARD TEXT,
#BUILDING_NO INT(11),
#FOREIGN KEY(BUILDING_NO) REFERENCES Building(ID) ON DELETE CASCADE ON UPDATE CASCADE,
ROOM_NO INT(11),
FOREIGN KEY(ROOM_NO) REFERENCES Room(ID) ON DELETE CASCADE ON UPDATE CASCADE,
BED_NO INT(11),
REPORT_ID INT(20) ,
FOREIGN KEY(REPORT_ID) REFERENCES Report(ID) ON DELETE CASCADE ON UPDATE CASCADE,
CONTACT VARCHAR(15),
DOC_ID INT(20) ,
FOREIGN KEY(DOC_ID) REFERENCES Doctor(ID) ON DELETE CASCADE ON UPDATE CASCADE,
ADMIT_DATE DATE, 
DEL BOOLEAN DEFAULT FALSE)"""

Report_TableSql = """CREATE TABLE Report(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
#PATIENT_ID INT(20) NOT NULL,
#PATIENT_NAME VARCHAR(100) NOT NULL,
#DOC_ID INT(20),
#FOREIGN KEY(DOC_ID) REFERENCES Doctor(ID) ON DELETE CASCADE ON UPDATE CASCADE,
#DOC_NAME VARCHAR(100),
BLOOD_TYPE VARCHAR(20),
SYMPTOMPS TEXT,
DIAGNOSIS TEXT,
MEDICINES TEXT,
DEL BOOLEAN DEFAULT FALSE)"""

Doctor_TableSql = """CREATE TABLE Doctor(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(100) NOT NULL,
SEX CHAR(10),
CONTACT VARCHAR(15),
ADDRESS VARCHAR(100),
DEPT VARCHAR(100),
ROOM_NO INT(20),
FOREIGN KEY(ROOM_NO) REFERENCES Room(ID) ON DELETE CASCADE ON UPDATE CASCADE,
#BUILDING_ID INT(20),
FEE INT(20),
DEGREE TEXT,
DEL BOOLEAN DEFAULT FALSE)"""

Staff_TableSql = """ CREATE TABLE Staff(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(100) NOT NULL,
SEX CHAR(10),
CONTACT VARCHAR(15),
ADDRESS VARCHAR(100),
BUILDING_ID INT(20),
FOREIGN KEY(BUILDING_ID) REFERENCES Building(ID) ON DELETE CASCADE ON UPDATE CASCADE,
DUTY VARCHAR(100),
SHIFT VARCHAR(100),
WAGE INT(20),
DEL BOOLEAN DEFAULT FALSE)"""

Vehicle_TableSql = """CREATE TABLE Vehicle(
NUM_PLATE VARCHAR(100) PRIMARY KEY,
BRAND VARCHAR(100),
MODEL VARCHAR(100),
PURPOSE VARCHAR(100),
BUILDING_ID INT(20),
FOREIGN KEY(BUILDING_ID) REFERENCES Building(ID) ON DELETE CASCADE ON UPDATE CASCADE,
DEL BOOLEAN DEFAULT FALSE)"""

Medicine_TableSql = """CREATE TABLE Medicine(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(100) NOT NULL,
AVAILIBILITY BOOLEAN,
COMPANY VARCHAR(100),
EXPIRY_DATE DATE,
DEL BOOLEAN DEFAULT FALSE)"""

Building_TableSql = """CREATE TABLE Building(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
ADDRESS VARCHAR(100),
ROOM_NUM INT(20),
MACHINE_NUM INT(20),
VEHICLE_NUM INT(20),
DOCTOR_NUM INT(20),
DEPTS TEXT,
DEL BOOLEAN DEFAULT FALSE)"""

Room_TableSql = """CREATE TABLE Room(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
BUILDING_ID INT(20) NOT NULL,
FOREIGN KEY(BUILDING_ID) REFERENCES Building(ID) ON DELETE CASCADE ON UPDATE CASCADE,
#FOREIGN KEY REFERENCES Building(ID),
DEPT_NAME VARCHAR(100),
AVAILIBITY BOOLEAN,
FEES INT(20),
DEL BOOLEAN DEFAULT FALSE)"""

Machine_TableSql = """CREATE TABLE Machine(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(100) NOT NULL,
ROOM_ID INT(20),
FOREIGN KEY(ROOM_ID) REFERENCES Room(ID) ON DELETE CASCADE ON UPDATE CASCADE,
#FOREIGN KEY REFERENCES Room(ID),
#BUILDING_ID INT(20),
#DEPT_NAME VARCHAR(100),
DEL BOOLEAN DEFAULT FALSE)"""


if not table_exists("Building",cursor):
	cursor.execute(Building_TableSql)
	print("Building table created")

if not table_exists("Room",cursor):
	cursor.execute(Room_TableSql)
	print("Room table created")

if not table_exists("Doctor",cursor):
	cursor.execute(Doctor_TableSql)
	print("Doctor table created")

if not table_exists("Report",cursor):
	cursor.execute(Report_TableSql)
	print("Report table created")


if not table_exists("Patient_Outdoor",cursor):
	cursor.execute(Patient_Outdoor_TableSql)
	print("Patient Outdoor table created")

if not table_exists("Patient_Emergency",cursor):
	cursor.execute(Patient_Emergency_TableSql)
	print("Patient Emergency table created")

if not table_exists("Patient_Admission",cursor):
	cursor.execute(Patient_Admission_TableSql)
	print("Patient Admission table created")

if not table_exists("Staff",cursor):
	cursor.execute(Staff_TableSql)
	print("Staff table created")

if not table_exists("Vehicle",cursor):
	cursor.execute(Vehicle_TableSql)
	print("Vehicle table created")

if not table_exists("Medicine",cursor):
	cursor.execute(Medicine_TableSql)
	print("Medicine table created")

if not table_exists("Machine",cursor):
	cursor.execute(Machine_TableSql)
	print("Machine table created")


"""insert= "INSERT INTO Patient_Outdoor(NAME, AGE, SEX, ADDRESS, SYMPTOMPS, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME, VISIT_DATE)\
	VALUES('Saidul Kabir',23,'MALE','126/1,WAPDA ROAD,RAMPURA,DHAKA','FEVER,COUGH','CORONA','NAPA','01910399849','DR ABCD','2020-2-21');"
cursor.execute(insert)
insert= "INSERT INTO Patient_Emergency(NAME, AGE, SEX, ADDRESS, EMERGENCY, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME, VISIT_DATE)\
	VALUES('Saidul Kabir',23,'MALE','126/1,WAPDA ROAD,RAMPURA,DHAKA','ACCIDENT','CORONA','NAPA','01910399849','DR ABCD','2020-2-21');"
cursor.execute(insert)
insert= "INSERT INTO Patient_Admission(NAME, AGE, SEX, ADDRESS, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME, ADMIT_DATE,BUILDING_NO,WARD,ROOM_NO,BED_NO)\
	VALUES('Saidul Kabir',23,'MALE','126/1,WAPDA ROAD,RAMPURA,DHAKA','CANCER','NAPA','01910399849','DR ABCD','2020-2-21',5,'CANCER',102,5);"
cursor.execute(insert)"""

insert = "INSERT INTO Report"
connection.commit()
connection.close()