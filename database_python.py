import mysql.connector
from mysql.connector import FieldType


ALL_VIEWS = {"Patient_Outdoor":{"doctor_view":"NAME, AGE, SEX, SYMPTOMPS, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME"
			,"staff_view":"ID, NAME, AGE, SEX, ADDRESS, CONTACT, DOC_NAME, VISIT_DATE"}
			,"Patient_Admission":{"doctor_view":"NAME, AGE, SEX, SYMPTOMPS, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME, WARD, BUILDING_NO, ROOM_NO,BED_NO"
			,"staff_view":"ID, NAME, AGE, SEX, ADDRESS, CONTACT, DOC_NAME, VISIT_DATE, WARD, BUILDING_NO, ROOM_NO, BED_NO, ADMIT_DATE"}
			,"Patient_Emergency":{"doctor_view":"NAME, AGE, SEX, SYMPTOMPS, EMERGENCY, MEDICINE, CONTACT, DOC_NAME"
			,"staff_view":"ID, NAME, AGE, SEX, ADDRESS, EMERGENCY, CONTACT, DOC_NAME, VISIT_DATE"}}

def connect2server(server_name,password=""):
	try:
		connection = mysql.connector.connect(host="localhost",user="root",passwd=password,database=server_name )
		cursor = connection.cursor(buffered = True)
		print("Welcome to Hospital Database")
	except Exception as e:
		print("Can't connect to Database: ",e)
		return None,None
	return connection,cursor

def process_long(num):
	return int(num)

def process_date(date):

	if len(date.split("-")) == 3:
		return date
	elif len(date.split("/")) == 3:
		d = date.split("/")
		return d[0]+"-"+d[1]+"-"+d[2]
	elif len(date.split(".")) == 3:
		d = date.split(".")
		return d[0]+"-"+d[1]+"-"+d[2]

def make_insert_query(table_name,COL):
	q = "("
	v = "("
	for i,column in enumerate(COL):
		if i==0:
			q = q + column
			v = v + "%s"
		else:
			q = q +","+column
			v = v +","+"%s"
	q = q + ")"
	v = v + ")"
	query = "INSERT INTO " + table_name + q + " VALUES" + v
	return query

def make_update_query(table_name,COL,key,key_value):
	#"UPDATE table_name SET field1=%s, field10=%s WHERE id=%s"
	q = ""
	for i,column in enumerate(COL):
		if i == 0:
			q = q + column+'=%s'
		else:
			q = q + ","+ column+'=%s'
	query = "UPDATE {} SET ".format(table_name) + q +" WHERE {}= {}".format(key,key_value)
	return query

def make_retrieve_query(table_name,view,key_names):
	#cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE and NAME=%s and AGE=%s and SEX=%s".format(view,table_name))
	field_conditions=""
	
	for field in key_names:
		field_conditions += " and " +field+"=%s"	
		
	query = "SELECT {} FROM {} WHERE DEL=FALSE".format(view,table_name)+field_conditions
	return query

def create(table_name,connection,cursor):
	try:
		cursor.execute("SELECT * FROM {}".format(table_name))
		columns = cursor.description
		print("Adding Entry to :"+table_name+"\n")
		print("Press Enter to skip field\n\n")
		values = []
		field_list=[]
		for column in columns[:-1]:
			#print(column[0]," ",FieldType.get_info(column[1]))
			form=""
			if FieldType.get_info(column[1]) == "DATE":
				form = "(YY-MM-DD)"
			inp = input("Input "+column[0]+"{} :".format(form))
			if inp !="" : 
				if FieldType.get_info(column[1]) == 'LONG':
					inp = process_long(inp)
				elif FieldType.get_info(column[1]) == 'DATE':
					inp = process_date(inp)			
				values.append(inp)
				field_list.append(column[0])	
		values = tuple(values)
		query = make_insert_query(table_name,field_list)

		print(query)

		cursor.execute(query,values)
		connection.commit()
		print("Entry successfully added to table: "+table_name)
	except Exception as e:
		print(e)
		connection.rollback()

def retrieve(table_name,connection,cursor,all_views=ALL_VIEWS):
	try:
		cursor.execute("SHOW KEYS FROM {} WHERE Key_name = 'PRIMARY'".format(table_name))
		primary_keys = cursor.fetchall()
		primary_key_name = primary_keys[0][4]

		doctor_view = False
		print("Press 1 to view as Doctor and 2 to view as Staff:")
		view_type = input()
		try:
			if view_type == "1":
				doctor_view = True	
			elif view_type != "2":
				raise Exception("Invalid Input")
		except Exception as e:
			print(e)
			retrieve(table_name,connection,cursor)
			return None
		#print(columns)
		if doctor_view:
			view = all_views[table_name]["doctor_view"] 
		else:
			view = all_views[table_name]["staff_view"]	

		print("VIEW:",view)	
		key_name = input("\n* Press Enter to view whole table \n\n* Enter 1 to search with primary key value \n\n* Enter something else to search with multiple key values:\n")

		if key_name =="":
			cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE".format(view,table_name))
			data = cursor.fetchall()
			if len(data) == 0:
				raise Exception("Data doesn't Exist")
			for d in data:
				print(d)

		elif key_name == "1": 
			key_value = input("Enter {} value: ".format(primary_key_name))
			key_value = process_long(key_value)
			cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE and {}={}".format(view,table_name,primary_key_name,key_value))
			data = cursor.fetchall()
			if len(data) == 0:
				raise Exception("Data doesn't Exist")
			for d in data:
				print(d)
		else:	
			print("\n\nEnter key value \n\nPress Enter if you want to skip key")
			#cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE and NAME=%s and AGE=%s and SEX=%s".format(view,table_name),("Saidul Kabir",23,"MALE"))
			key_names = []
			key_values = []

			for key_name in view.split(","):
				key = input(key_name+":  ")
				if key != "":
					cursor.execute("SELECT {} FROM {}".format(key_name,table_name))
					data_type = cursor.description[0][1]
					if FieldType.get_info(data_type) == 'LONG':
						key = process_long(key)
					elif FieldType.get_info(data_type) == 'DATE':
						key = process_date(key)		
					key_names.append(key_name)
					key_values.append(key)
			query = make_retrieve_query(table_name,view,key_names)
			key_values = tuple(key_values)
			cursor.execute(query,key_values)
			data = cursor.fetchall()
			print(view)
			if len(data) == 0:
				raise Exception("Data doesn't Exist")
			for d in data:
				print(d)
	except Exception as e:
		print(e)

def update(table_name,connection,cursor):	
	try:
		cursor.execute("SHOW KEYS FROM {} WHERE Key_name = 'PRIMARY'".format(table_name))
		primary_keys = cursor.fetchall()
		key_name = primary_keys[0][4]
		key_value = input("Input "+key_name+" of row you want to update: ")

		cursor.execute("SELECT * FROM {} WHERE {} = {}".format(table_name,key_name,key_value))
		if len(cursor.fetchall()) == 0:
			raise Exception("Data doesn't exist")
		cursor.execute("SELECT * FROM {}".format(table_name))
		columns = cursor.description		
		print("Press Enter if you don't want to change a field")
		values = []
		field_col = []
		for column in columns[1:-1]:
			form=""
			if FieldType.get_info(column[1]) == "DATE":
				form = "(YY-MM-DD)"
			inp = input("Input "+column[0]+"{} :".format(form))
			if inp !="":
				if FieldType.get_info(column[1]) == 'LONG':
					inp = process_long(inp)
				elif FieldType.get_info(column[1]) == 'DATE':
					inp = process_date(inp)			
				values.append(inp)
				field_col.append(column[0])	
		values = tuple(values)
		query = make_update_query(table_name,field_col,key_name,key_value)
		print(query)
		cursor.execute(query,values)
		connection.commit()
		print("Entry successfully updated in table: "+table_name)
		#"UPDATE table_name SET field1=%s, field10=%s WHERE id=%s", (var1,... var10, id)
	except Exception as e:
		print(e)
		connection.rollback()

def delete(table_name,connection,cursor):
	try:
		cursor.execute("SHOW KEYS FROM {} WHERE Key_name = 'PRIMARY'".format(table_name))
		primary_keys = cursor.fetchall()
		key_name = primary_keys[0][4]
		key_value = input("Input "+key_name+" of row you want to delete: ")
		soft_delete = True

		query = "SELECT * FROM {} WHERE {} = {}".format(table_name,key_name,key_value)	
		cursor.execute(query)
		data = cursor.fetchall()
		if len(data) == 0:
			raise Exception("Data doesn't exist")

		del_type = input("Enter 1 for Soft Delete and 2 for Hard Delete: ")
		try:
			if del_type == "2":
				soft_delete = False
			elif del_type != "1":
				raise Exception("Invalid Input")
		except Exception as e:
			print(e)
			delete(table_name,connection,cursor)
			return None

		if soft_delete:		
			print("Do you want to delete the Entry: (Y/N)")
			print(data[0])
			ans = input()
			if ans == "Y" or ans =="y" :
				query = "UPDATE {} SET DEL=TRUE WHERE {}={}".format(table_name,key_name,key_value)
				cursor.execute(query)
				connection.commit()
				print("Entry deleted successfully")
			else:
				print("Entry was not deleted")
		else:
			print("Do you want to permanently delete the Entry: (Y/N)")
			print(data[0])
			ans = input()
			if ans == "Y" or ans =="y" :
				query = "DELETE FROM {} WHERE {}={}".format(table_name,key_name,key_value)
				cursor.execute(query)
				connection.commit()
				print("Entry deleted successfully")
			else:
				print("Entry was not deleted")

	except Exception as e:
		print(e)
		connection.rollback()

if __name__ == "__main__":
	connection,cursor = connect2server("medical database")

	create("Patient_Admission",connection,cursor)
	#retrieve("Patient_Outdoor",connection,cursor)
	#update("Patient_Admission",connection,cursor)
	#delete("Patient_Outdoor",connection,cursor)

	connection.close()

