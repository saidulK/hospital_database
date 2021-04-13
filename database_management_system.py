import mysql.connector

from database_python import *


connection,cursor = connect2server("medical database")
view = get_login_info()
while True:
	print("\nEnter Operation: \n1) C for Create \n2) R for Retrieve \n3) U for Update \n4) D for Delete \n5) E for Exit\n")
	op = input()
	if op == "E" or op == "e":
		break
	elif op =="C" or op == "c":
		print("\nSelect Table: ")
		
	elif op == "R" or op =="r":
		print("\nSelect Table: ")
	elif op == "U" or op =="u":
		print("\nSelect Table: ")
	elif op == "D" or op == "d":
		print("\nSelect Table: ")
	else:
		print("\nInvalid Command")

#create("Patient_Admission",connection,cursor)
#retrieve("Patient_Outdoor",connection,cursor)
#update("Patient_Admission",connection,cursor)
#delete("Patient_Outdoor",connection,cursor)

connection.close()