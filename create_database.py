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

Patient_Outdoor_TableSql = """CREATE TABLE Patient_Outdoor(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  VARCHAR(100) NOT NULL,
AGE INT(3),
SEX CHAR(10),
ADDRESS VARCHAR(100),
SYMPTOMPS TEXT,
DIAGNOSIS TEXT,
MEDICINE TEXT,
CONTACT VARCHAR(15),
DOC_NAME VARCHAR(100),
VISIT_DATE DATE, 
DEL BOOLEAN DEFAULT FALSE)"""

Patient_Emergency_TableSql = """CREATE TABLE Patient_Emergency(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  VARCHAR(100) NOT NULL,
AGE INT(3),
SEX CHAR(10),
ADDRESS VARCHAR(100),
EMERGENCY TEXT,
DIAGNOSIS TEXT,
MEDICINE TEXT,
CONTACT VARCHAR(15),
DOC_NAME VARCHAR(100),
VISIT_DATE DATE, 
DEL BOOLEAN DEFAULT FALSE)"""

Patient_Admission_TableSql = """CREATE TABLE Patient_Admission(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
NAME  VARCHAR(100) NOT NULL,
AGE INT(3),
SEX CHAR(10),
ADDRESS VARCHAR(100),
WARD TEXT,
BUILDING_NO INT(11),
ROOM_NO INT(11),
BED_NO INT(11),
DIAGNOSIS TEXT,
MEDICINE TEXT,
CONTACT VARCHAR(15),
DOC_NAME VARCHAR(100),
ADMIT_DATE DATE, 
DEL BOOLEAN DEFAULT FALSE)"""

if not table_exists("Patient_Outdoor",cursor):
	cursor.execute(Patient_Outdoor_TableSql)
	print("Patient Outdoor table created")

if not table_exists("Patient_Emergency",cursor):
	cursor.execute(Patient_Emergency_TableSql)
	print("Patient Emergency table created")

if not table_exists("Patient_Admission",cursor):
	cursor.execute(Patient_Admission_TableSql)
	print("Patient Admission table created")

insert= "INSERT INTO Patient_Outdoor(NAME, AGE, SEX, ADDRESS, SYMPTOMPS, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME, VISIT_DATE)\
	VALUES('Saidul Kabir',23,'MALE','126/1,WAPDA ROAD,RAMPURA,DHAKA','FEVER,COUGH','CORONA','NAPA','01910399849','DR ABCD','2020-2-21');"
cursor.execute(insert)
insert= "INSERT INTO Patient_Emergency(NAME, AGE, SEX, ADDRESS, EMERGENCY, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME, VISIT_DATE)\
	VALUES('Saidul Kabir',23,'MALE','126/1,WAPDA ROAD,RAMPURA,DHAKA','ACCIDENT','CORONA','NAPA','01910399849','DR ABCD','2020-2-21');"
cursor.execute(insert)
insert= "INSERT INTO Patient_Admission(NAME, AGE, SEX, ADDRESS, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME, ADMIT_DATE,BUILDING_NO,WARD,ROOM_NO,BED_NO)\
	VALUES('Saidul Kabir',23,'MALE','126/1,WAPDA ROAD,RAMPURA,DHAKA','CANCER','NAPA','01910399849','DR ABCD','2020-2-21',5,'CANCER',102,5);"
cursor.execute(insert)
connection.commit()
connection.close()