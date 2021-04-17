import mysql.connector

from database_python import *


connection,cursor = connect2server("medical database")
login_view = get_login_info()
if login_view is not None:
	while True:
		print("\n\n\nEnter Operation: \n1) C for Create \n2) R for Retrieve \n3) U for Update \n4) D for Delete \n5) E for Exit\n")
		op = input()
		if op.lower() == "e":
			break
		elif op.lower() == "c":
			table_list = list(TABLE_ACCESS[login_view]["C"].keys())
			if len(table_list) != 0:
				print("\nSelect Table: ")
				table_name = get_table_input(table_list)	
				create(table_name,connection,cursor,login_view)
			else:
				print("\n Operation not allowed for this user")

		elif op.lower() =="r":
			table_list = list(TABLE_ACCESS[login_view]["R"].keys())
			if len(table_list) != 0:
				print("\nSelect Table: ")
				table_name = get_table_input(table_list)
				
				retrieve(table_name,connection,cursor,login_view)

			else:
				print("\n Operation not allowed for this user")
		
		elif op.lower() =="u":
			table_list = list(TABLE_ACCESS[login_view]["U"].keys())
			if len(table_list) != 0:
				print("\nSelect Table: ")
				table_name = get_table_input(table_list)
				
				update(table_name,connection,cursor,login_view)

			else:
				print("\n Operation not allowed for this user")

		elif op.lower() == "d":
			table_list = TABLE_ACCESS[login_view]["D"]
			if len(table_list) != 0:
				print("\nSelect Table: ")
				table_name = get_table_input(table_list)

				delete(table_name,connection,cursor,login_view)

			else:
				print("\n Operation not allowed for this user")
		else:
			print("\nInvalid Command")

connection.close()