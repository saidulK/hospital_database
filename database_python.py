import mysql.connector
from mysql.connector import FieldType


CONDITION_FIELDS = ["LONG","DATE","TIME"]

#"Patient_Outdoor":, "Patient_Emergency": , "Patient_Admission":, "Report":, "Doctor":, "Staff":, "Vehicle":, "Medicine":, "Building":, "Room":, "Machines":
TABLE_NAMES = ["Patient_Outdoor", "Patient_Emergency", "Patient_Admission", "Report", "Doctor", "Staff", "Vehicle", "Medicine", "Building", "Room", "Machines"]
#"Patient_Outdoor": [1,1,1,1,0,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,0,1,0,1,1,0], "Patient_Admission":[1,1,1,1,0,1,1,1,1,1,1,1,1,0],
TABLE_ACCESS = {"doctor_view":{"C":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,0], "Patient_Admission": [1,1,1,1,1,1,1,1,1,1,1,1,1,0],"Medicine":[1,1,1,1,1,0],"Report":[1,1,1,1,1,1,1,1,1,1,0]}
				,"R":{"Patient_Outdoor": [1,1,1,1,0,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,0,1,0,1,1,0], "Patient_Admission":[1,1,1,1,0,1,1,1,1,1,1,1,1,0], "Medicine":[1,1,1,1,1,0],"Report":[1,1,1,1,1,1,1,1,1,1,0],"Doctor":[1,1,1,1,0,1,1,1,1,0,0], "Staff":[1,1,1,0,0,0,1,1,0,0], "Building":[1,1,0,0,0,0,1,0], "Room":[1,1,1,0,0,0], "Machines": [0,1,0,1,1,0]}
				,"U":{"Patient_Outdoor": [1,1,1,1,0,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,0,1,0,1,1,0], "Patient_Admission":[1,1,1,1,0,1,1,1,1,1,1,1,1,0], "Medicine":[1,1,1,1,1,0],"Report":[1,1,1,1,1,1,1,1,1,1,0]}
				,"D":["Medicine","Report"]}
				,"staff_view":{"C":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,0], "Patient_Admission": [1,1,1,1,1,1,1,1,1,1,1,1,1,0], "Medicine":[1,1,1,1,1,0],"Report":[1,1,1,1,1,1,0,0,0,0,0]}
				,"R":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,0], "Patient_Admission": [1,1,1,1,1,1,1,1,1,1,1,1,1,0],"Medicine": [1,1,1,1,1,0],"Report": [1,1,1,1,1,1,0,0,0,0,0],"Doctor": [1,1,1,1,0,1,1,1,1,0,0], "Staff":[1,1,1,0,0,0,1,1,0,0], "Building":[1,1,0,0,0,0,1,0], "Room":[1,1,1,0,0,0], "Machines": [0,1,1,1,1,0]}
				,"U":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,0], "Patient_Admission": [1,1,1,1,1,1,1,1,1,1,1,1,1,0],"Medicine": [1,1,1,1,1,0],"Report": [1,1,1,1,1,1,0,0,0,0,0],"Doctor": [1,1,1,1,0,1,1,1,1,0,0], "Staff":[1,1,1,0,0,0,1,1,0,0], "Building":[1,1,0,0,0,0,1,0], "Room":[1,1,1,0,0,0]}
				,"D":["Patient_Outdoor", "Patient_Emergency", "Patient_Admission", "Medicine","Report"]}
				,"patient_view":{"C":{}
				,"R":{}
				,"U":{"Patient_Outdoor":[0,1,1,1,1,0,1,0,0,0], "Patient_Emergency":[0,1,1,1,1,0,1,0,0,0], "Patient_Admission": [0,1,1,1,1,0,0,0,0,0,1,0,0,0]}
				,"D":[]}
				,"management_view":{"C":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,0], "Patient_Admission":[1,1,1,1,1,1,1,1,1,1,1,1,1,0], "Report":[1,1,1,1,1,1,0,0,0,0,0], "Doctor": [1,1,1,1,1,1,1,1,1,1,0], "Staff":[1,1,1,1,1,1,1,1,1,0], "Vehicle":[1,1,1,1,1,0], "Medicine":[1,1,1,1,1,0], "Building":[1,1,1,1,1,1,1,0], "Room":[1,1,1,1,1,0], "Machines": [1,1,1,1,1,0]}
				,"R":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,0], "Patient_Admission":[1,1,1,1,1,1,1,1,1,1,1,1,1,0], "Report":[1,1,1,1,1,1,0,0,0,0,0], "Doctor": [1,1,1,1,1,1,1,1,1,1,0], "Staff": [1,1,1,1,1,1,1,1,1,0], "Vehicle":[1,1,1,1,1,0], "Medicine": [1,1,1,1,1,0], "Building":[1,1,1,1,1,1,1,0], "Room":[1,1,1,1,1,0], "Machines":[1,1,1,1,1,0]}
				,"U":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,0], "Patient_Admission":[1,1,1,1,1,1,1,1,1,1,1,1,1,0], "Report":[1,1,1,1,1,1,0,0,0,0,0], "Doctor": [1,1,1,1,1,1,1,1,1,1,0], "Staff": [1,1,1,1,1,1,1,1,1,0], "Vehicle":[1,1,1,1,1,0], "Medicine": [1,1,1,1,1,0], "Building":[1,1,1,1,1,1,1,0], "Room":[1,1,1,1,1,0], "Machines":[1,1,1,1,1,0]}
				,"D":["Patient_Outdoor", "Patient_Emergency", "Patient_Admission", "Report", "Doctor", "Staff", "Vehicle", "Medicine", "Building", "Room", "Machines"]}}

ALL_VIEWS = {"Patient_Outdoor":{"doctor_view":"ID, NAME, AGE, SEX, SYMPTOMPS, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME"
			,"staff_view":"ID, NAME, AGE, SEX, ADDRESS, CONTACT, DOC_NAME, VISIT_DATE"}
			,"Patient_Admission":{"doctor_view":"ID,NAME, AGE, SEX, DIAGNOSIS, MEDICINE, CONTACT, DOC_NAME, WARD, BUILDING_NO, ROOM_NO,BED_NO"
			,"staff_view":"ID, NAME, AGE, SEX, ADDRESS, CONTACT, DOC_NAME, ADMIT_DATE, WARD, BUILDING_NO, ROOM_NO, BED_NO"}
			,"Patient_Emergency":{"ID,doctor_view":"NAME, AGE, SEX, SYMPTOMPS, EMERGENCY, MEDICINE, CONTACT, DOC_NAME"
			,"staff_view":"ID, NAME, AGE, SEX, ADDRESS, EMERGENCY, CONTACT, DOC_NAME, VISIT_DATE"}}

def connect2server(server_name,password=""):
	try:
		connection = mysql.connector.connect(host="localhost",user="root",passwd=password,database=server_name )
		cursor = connection.cursor(buffered = True)
		print("Welcome to Hospital Database")
	except Exception as e:
		print("Can't connect to Database: ",e)

	return connection,cursor

def get_login_info():
	print("\nLogin as: \n1)Enter D for Doctor \n2)Enter S for Staff\n3)Enter P for Patient\n4)Enter M for Management\n")
	inp = input()
	if inp.lower() =="d":
		return "doctor_view"
	elif inp.lower() =="s":
		return "staff_view"
	elif inp.lower() =="p":
		return "patient_view"
	elif inp.lower() =="m":
		return "management_view"
	else:
		print("Invalid Command")
		return get_login_info()

def get_table_input(table_list):
	
	for i,table in enumerate(table_list):
		print("\n{}) Enter {} for {}".format(i+1,i+1,table))
	inp = input("\n")
	try:
		inp = int(inp)-1
		print(inp, list(range(len(table_list))))

		if inp in list(range(len(table_list))):
			return table_list[inp]
		else:
			raise Exception("\n\nInvalid Input!")
	except Exception as e:
		print(e)
		return get_table_input(table_list)

def get_input(field_name,field_type,tag="",func=None):
	form=""
	if field_type == "DATE":
		form = "(YY-MM-DD)"
	inp = input(tag+" "+field_name+"{} :".format(form))
	try:
		if inp =="":
			return inp
		elif inp =="<" or inp==">" and (field_type in CONDITION_FIELDS) and func == "retrieve":
			return inp
		elif field_type == 'LONG':
			inp = process_long(inp)
			return inp
		elif field_type == 'DATE':
			inp = process_date(inp)
			return inp
		elif field_type == "BOOLEAN":
			inp = process_boolean(inp)
			return inp
		else:
			return inp
	except:
		print("Error! Please Input Again\n")
		return get_input(field_name,field_type)

def get_view(field_list,view_fields):
	view = ""
	for field,select in zip(field_list,view_fields):
		if select == 1:
			view += field[0]+","
	return view[:-1] 


def print_table_data(field_list,data):
	if len(data) == 0 :
		print("No data to print")
	elif len(data) == 1:
		for i,d in zip(field_list,data[0]):
			print(i," :",d)
	else:
		for row in data:
			print("\n")
			for field,field_value in zip(field_list,row):
				print(field," : ",field_value," ",end ="",sep="")


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
	else:
		raise Exception("Wrong format")

def process_boolean(boolean):
	if boolean == "1" or boolean.lower() =="true" or boolean.lower() =="t":
		return "TRUE"
	elif boolean == "0" or boolean.lower() =="false" or boolean.lower() =="f":
		return "FALSE"
	else:
		raise Exception("Wrong format")


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

def make_retrieve_query(table_name,view,key_names,conditions):
	#cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE and NAME=%s and AGE=%s and SEX=%s".format(view,table_name))
	field_conditions=""
	
	for field in key_names:
		field_conditions += " and " +field+"=%s"	

	for condition in conditions:
		condition_type = condition[0]
		field = condition[1]
		#value = condition[2]
		field_conditions += " and " +field+ condition_type + "%s" #"{}".format(value)

	query = "SELECT {} FROM {} WHERE DEL=FALSE".format(view,table_name)+field_conditions
	return query

def create(table_name,connection,cursor,log_view):
	try:
		#cursor.execute("SELECT * FROM {}".format(table_name))
		#columns = cursor.description
		print("\n\nAdding Entry to :"+table_name+"\n")
		print("Press Enter to skip field\n\n")
		values = []
		field_list=[]

		#columns = ALL_VIEWS[table_name][log_view].split(",")
		
		cursor.execute("SELECT * FROM {}".format(table_name))
		columns = cursor.description
		columns = get_view(columns,TABLE_ACCESS[log_view]["C"][table_name])
		columns = columns.split(",")

		for column in columns:
			cursor.execute("SELECT {} FROM {}".format(column,table_name))
			field_type = FieldType.get_info(cursor.description[0][1])
			field_name = cursor.description[0][0]
			inp = get_input(field_name,field_type)
			if inp != "":
				values.append(inp)
				field_list.append(column)
		values = tuple(values)
		query = make_insert_query(table_name,field_list)
		cursor.execute(query,values)
		connection.commit()
		print("Entry successfully added to table: "+table_name)

	except Exception as e:
		print(e)
		connection.rollback()

def retrieve(table_name,connection,cursor,log_view):
	try:
		print("\n\nRetrieving data from: {}".format(table_name))
		cursor.execute("SHOW KEYS FROM {} WHERE Key_name = 'PRIMARY'".format(table_name))
		primary_keys = cursor.fetchall()
		primary_key_name = primary_keys[0][4]

		#view = ALL_VIEWS[table_name][log_view]
		cursor.execute("SELECT * FROM {}".format(table_name))
		columns = cursor.description
		view = get_view(columns,TABLE_ACCESS[log_view]["R"][table_name])

		#print("VIEW:",view)	
		key_name = input("\n* Press Enter to view whole table \n\n* Enter 1 to search with primary key value \n\n* Enter something else to search with multiple key values:\n")

		if key_name =="":
			cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE".format(view,table_name))
			data = cursor.fetchall()
			if len(data) == 0:
				raise Exception("Data doesn't Exist")
			field_list = view.split(",")
			print_table_data(field_list,data)	
			#print(view)

			#for d in data:
			#	print(d)

		elif key_name == "1": 
			key_value = input("\nEnter {} value: ".format(primary_key_name))
			cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE and {}={}".format(view,table_name,primary_key_name,key_value))
			data = cursor.fetchall()
			if len(data) == 0:
				raise Exception("Data doesn't Exist")
			field_list = view.split(",")

			print("\n\n Data for {} = {}:\n".format(primary_key_name,key_value))
			print_table_data(field_list,data)	
			#print("\n\n Data for {} = {}:\n".format(primary_key_name,key_value))	
			#for i,d in zip(field_list,data[0]):
			#	print(i," :",d)
		else:	
			print("\n\nEnter key values: \n\n* Press Enter if you want to skip key\n\n* Enter < or > to set range\n")
			key_names = []
			key_values = []
			conditions = []
			condition_values = []
			for key_name in view.split(","):
				cursor.execute("SELECT {} FROM {}".format(key_name,table_name))
				field_name = cursor.description[0][0]
				field_type = FieldType.get_info(cursor.description[0][1])
				key = get_input(field_name,field_type,func="retrieve")
				
				if key != "":			
					if field_type in CONDITION_FIELDS and key =="<" :
						key = get_input(field_name,field_type,tag="\nMAX VALUE of ")
						conditions.append(("<",field_name))
						condition_values.append(key)
						key = get_input(field_name,field_type,tag="\nMIN VALUE of ")
						if key !="":
							conditions.append((">",field_name))
							condition_values.append(key)
					elif field_type in CONDITION_FIELDS and key ==">" :
						key = get_input(field_name,field_type,tag="\nMIN VALUE of ")
						conditions.append((">",field_name))
						condition_values.append(key)
						key = get_input(field_name,field_type,tag="\nMAX VALUE of ")
						if key !="":
							conditions.append(("<",field_name))
							condition_values.append(key)
					else:
						key_names.append(key_name)
						key_values.append(key)
			query = make_retrieve_query(table_name,view,key_names,conditions)
			key_values = key_values + condition_values
			key_values = tuple(key_values)
			cursor.execute(query,key_values)
			data = cursor.fetchall()

			if len(data) == 0:
				raise Exception("\n\nData doesn't Exist")
			field_list = view.split(",")
			print_table_data(field_list,data)
			#print(view)
			#for d in data:
			#	print(d)
	except Exception as e:
		print(e)

def update(table_name,connection,cursor,log_view):	
	try:
		print("\nUpdating in: "+table_name)
		cursor.execute("SHOW KEYS FROM {} WHERE Key_name = 'PRIMARY'".format(table_name))
		primary_keys = cursor.fetchall()
		key_name = primary_keys[0][4]
		key_value = input("\n\nInput "+key_name+" of row you want to update: ")
		cursor.execute("SELECT * FROM {} WHERE {} = {}".format(table_name,key_name,key_value))
		if len(cursor.fetchall()) == 0:
			raise Exception("Data doesn't exist")		
		print("\nPress Enter if you don't want to change a field")

		cursor.execute("SELECT * FROM {}".format(table_name))
		columns = cursor.description
		columns = get_view(columns,TABLE_ACCESS[log_view]["U"][table_name]).split(",")
		
		#columns = ALL_VIEWS[table_name][log_view].split(",")
		values = []
		field_list = []
		for column in columns:
			cursor.execute("SELECT {} FROM {}".format(column,table_name))
			field_type = FieldType.get_info(cursor.description[0][1])
			field_name = cursor.description[0][0]
			inp = get_input(column,field_type)
			if inp !="":			
				values.append(inp)
				field_list.append(column)	
		values = tuple(values)
		query = make_update_query(table_name,field_list,key_name,key_value)
		cursor.execute(query,values)
		connection.commit()
		print("Entry successfully updated in table: "+table_name)
		
	except Exception as e:
		print(e)
		connection.rollback()

def delete(table_name,connection,cursor,log_view):
	try:
		print("\n\nDeleting from {}: ".format(table_name))
		cursor.execute("SHOW KEYS FROM {} WHERE Key_name = 'PRIMARY'".format(table_name))
		primary_keys = cursor.fetchall()
		key_name = primary_keys[0][4]

		key_value = input("\n\nInput "+key_name+" of row you want to delete: ")
		query = "SELECT * FROM {} WHERE {} = {}".format(table_name,key_name,key_value)	
		cursor.execute(query)
		data = cursor.fetchall()
		if len(data) == 0:
			raise Exception("Data doesn't exist")

		soft_delete = True

		if log_view == "management_view": 
			while True:	
				del_type = input("\nEnter 1 for Soft Delete and 2 for Hard Delete: \n")
				if del_type == "2":
					soft_delete = False
					break
				elif del_type == "1":
					break
				else:
					print("\nInvalid Input. Enter Again\n")
		

		if soft_delete:	
			query = "SELECT * FROM {} WHERE {} = {} and DEL=FALSE".format(table_name,key_name,key_value)	
			cursor.execute(query)
			data = cursor.fetchall()
			if len(data) == 0:
				raise Exception("Data doesn't exist")
			cursor.execute("SELECT * FROM {}".format(table_name))
			columns = cursor.description
			columns = get_view(columns,TABLE_ACCESS[log_view]["R"][table_name])
			field_list = columns.split(",")

			#field_list = ALL_VIEWS[table_name][log_view].split(",")

			print("\n\n")
			for i,d in zip(field_list,data[0]):
				print(i," : ",d)
			print("Do you want to delete the Entry: (Y/N)")
			ans = input()
			if ans == "Y" or ans =="y" :
				query = "UPDATE {} SET DEL=TRUE WHERE {}={}".format(table_name,key_name,key_value)
				cursor.execute(query)
				connection.commit()
				print("Entry deleted successfully")
			else:
				print("Entry was not deleted")
		else:
			query = "SELECT * FROM {} WHERE {} = {}".format(table_name,key_name,key_value)	
			cursor.execute(query)
			data = cursor.fetchall()
			
			cursor.execute("SELECT * FROM {}".format(table_name))
			columns = cursor.description
			columns = get_view(columns,TABLE_ACCESS[log_view]["R"][table_name])
			field_list = columns.split(",")

			field_list = ALL_VIEWS[table_name][log_view].split(",")
			print("\n\n")
			for i,d in zip(field_list,data[0]):
				print(i," :",d)
			print("\nDo you want to permanently delete the Entry: (Y/N): ")
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

	#create("Patient_Admission",connection,cursor,"doctor_view")
	#retrieve("Patient_Outdoor",connection,cursor,"staff_view")
	#update("Patient_Admission",connection,cursor,"staff_view")
	#delete("Patient_Outdoor",connection,cursor,"doctor_view")

	connection.close()

