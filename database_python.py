import mysql.connector
from mysql.connector import FieldType


CONDITION_FIELDS = ["LONG","DATE","TIME"]

#"Patient_Outdoor":, "Patient_Emergency": , "Patient_Admission":, "Report":, "Doctor":, "Staff":, "Vehicle":, "Medicine":, "Building":, "Room":, "Machines":
TABLE_NAMES = ["Patient_Outdoor", "Patient_Emergency", "Patient_Admission", "Report", "Doctor", "Staff", "Vehicle", "Medicine", "Building", "Room", "Machines"]
#"Patient_Outdoor": [1,1,1,1,0,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,0,1,0,1,1,0], "Patient_Admission":[1,1,1,1,0,1,1,1,1,1,1,1,1,0],
TABLE_ACCESS = {"doctor_view":{"C":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,1,0], "Patient_Admission": [1,1,1,1,1,1,1,1,1,1,1,1,0],"Medicine":[1,1,1,1,1,0],"Report":[1,1,1,1,1,0]}
				,"R":{"Patient_Outdoor": [1,1,1,1,0,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,0,1,1,1,1,1,0], "Patient_Admission":[1,1,1,1,0,1,1,1,1,1,1,1,0], "Medicine":[1,1,1,1,1,0],"Report":[1,1,1,1,1,0],"Doctor":[1,1,1,1,0,1,1,1,0,0], "Staff":[1,1,1,0,0,0,1,1,0,0], "Building":[1,1,0,0,0,0,1,0], "Room":[1,1,1,0,0,0], "Machines": [0,1,1,0]}
				,"U":{"Patient_Outdoor": [1,0,0,0,0,1,0,1,0,0], "Patient_Emergency":[1,0,0,0,0,1,0,1,1,0,0], "Patient_Admission":[1,0,0,0,0,0,1,1,1,1,1,1,0], "Medicine":[1,1,1,1,1,0],"Report":[1,1,1,1,1,0]}
				,"D":["Medicine","Report"]}
				,"staff_view":{"C":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,1,0], "Patient_Admission": [1,1,1,1,1,1,1,1,1,1,1,1,0],"Report":[1,1,0,0,0,0]}
				,"R":{"Patient_Outdoor":[1,1,1,1,0,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,0,1,1,1,1,1,0], "Patient_Admission": [1,1,1,1,1,1,1,1,1,1,1,1,0],"Medicine": [1,1,1,1,1,0],"Report": [1,1,0,0,1,0],"Doctor": [1,1,1,1,0,1,1,1,0,0], "Staff":[1,1,1,0,0,0,1,1,0,0], "Building":[1,1,0,0,0,0,1,0], "Room":[1,1,1,1,1,0], "Machines": [0,1,1,0]}
				,"U":{"Patient_Outdoor":[1,0,0,0,0,1,1,1,1,0], "Patient_Emergency":[1,0,0,0,0,1,1,1,1,1,0], "Patient_Admission": [1,0,0,0,0,1,1,1,1,0,1,1,0],"Report": [1,1,0,0,0,0],"Doctor": [1,0,0,0,0,1,1,1,0,0], "Staff":[1,1,1,0,0,0,1,1,0,0]}
				,"D":["Patient_Outdoor", "Patient_Emergency", "Patient_Admission", "Medicine","Report"]}
				,"patient_view":{"C":{}
				,"R":{"Patient_Outdoor":[0,1,0,1,0,0,1,0,1,0], "Patient_Emergency":[0,1,0,1,0,1,0,0,1,0,0], "Patient_Admission": [0,1,0,1,0,0,0,0,1,0,1,0,0],"Building":[1,1,0,0,0,0,1,0],"Report":[1,1,0,0,1,0]} #,"Report":[1,1,0,0,1,0]
				,"U":{"Patient_Outdoor":[0,1,1,1,1,0,1,0,0,0], "Patient_Emergency":[0,1,1,1,1,0,1,0,0,0,0], "Patient_Admission": [0,1,1,1,1,0,0,0,0,1,0,0,0]}
				,"D":[]}
				,"management_view":{"C":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,1,0], "Patient_Admission":[1,1,1,1,1,1,1,1,1,1,1,1,0], "Report":[1,1,1,1,1,0], "Doctor": [1,1,1,1,1,1,1,1,1,0], "Staff":[1,1,1,1,1,1,1,1,1,0], "Vehicle":[1,1,1,1,1,0], "Medicine":[1,1,1,1,1,0], "Building":[1,1,1,1,1,1,1,0], "Room":[1,1,1,1,1,0], "Machines": [1,1,1,0]}
				,"R":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,0], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,1,0], "Patient_Admission":[1,1,1,1,1,1,1,1,1,1,1,1,0], "Report":[1,1,1,1,1,0], "Doctor": [1,1,1,1,1,1,1,1,1,0], "Staff": [1,1,1,1,1,1,1,1,1,0], "Vehicle":[1,1,1,1,1,0], "Medicine": [1,1,1,1,1,0], "Building":[1,1,1,1,1,1,1,0], "Room":[1,1,1,1,1,0], "Machines":[1,1,1,0]}
				,"U":{"Patient_Outdoor":[1,1,1,1,1,1,1,1,1,1], "Patient_Emergency":[1,1,1,1,1,1,1,1,1,1,1], "Patient_Admission":[1,1,1,1,1,1,1,1,1,1,1,1,1], "Report":[1,1,1,1,1,1], "Doctor": [1,1,1,1,1,1,1,1,1,1], "Staff": [1,1,1,1,1,1,1,1,1,1], "Vehicle":[1,1,1,1,1,1], "Medicine": [1,1,1,1,1,1], "Building":[1,1,1,1,1,1,1,1], "Room":[1,1,1,1,1,1], "Machines":[1,1,1,1]}
				,"D":["Patient_Outdoor", "Patient_Emergency", "Patient_Admission", "Report", "Doctor", "Staff", "Vehicle", "Medicine", "Building", "Room", "Machines"]}}

JOIN_ACCESS = {"Patient_Outdoor":{"Report":["REPORT_ID","ID"],"Doctor":["DOC_ID","ID"]}
				, "Patient_Emergency":{"Report":["REPORT_ID","ID"],"Doctor":["DOC_ID","ID"]}
				, "Patient_Admission":{"Report":["REPORT_ID","ID"],"Doctor":["DOC_ID","ID"],"Room":["ROOM_NO","ID"]}
				, "Report":{"Patient_Outdoor":["ID","REPORT_ID"],"Patient_Emergency":["ID","REPORT_ID"],"Patient_Admission":["ID","REPORT_ID"]}
				, "Doctor":{"Patient_Outdoor":["ID","DOC_ID"],"Patient_Emergency":["ID","DOC_ID"],"Patient_Admission":["ID","DOC_ID"],"Room":["ROOM_NO","ID"]}
				, "Staff":{"Building":["BUILDING_ID","ID"]}
				, "Vehicle":{"Building":["BUILDING_ID","ID"]}
				, "Medicine":{}
				, "Building":{"Vehicle":["ID","BUILDING_ID"],"Staff":["ID","BUILDING_ID"],"Room":["ID","BUILDING_ID"]}
				, "Room":{"Patient_Admission":["ID","ROOM_NO"],"Doctor":["ID","ROOM_NO"],"Building":["BUILDING_ID","ID"],"Machines":["ID","ROOM_ID"]}
				, "Machines":{"Room":["ROOM_ID","ID"]}}


def connect2server(server_name,password=""):
	try:
		connection = mysql.connector.connect(host="localhost",user="root",passwd=password,database=server_name )
		cursor = connection.cursor(buffered = True)
		print("_________________________________________")
		print("\n    Welcome to DU EEE Hospital Database\n")
		print("_________________________________________")
		return connection,cursor
	except Exception as e:
		print("Can't connect to Database: ",e)
	

def get_login_info():
	print("\nLogin as: \n\n1)Enter D for Doctor \n2)Enter S for Staff\n3)Enter P for Patient\n4)Enter M for Management\n5)Enter E for Exit\n")
	inp = input()
	if inp.lower() =="d":
		return "doctor_view"
	elif inp.lower() =="s":
		return "staff_view"
	elif inp.lower() =="p":
		return "patient_view"
	elif inp.lower() =="m":
		return "management_view"
	elif inp.lower() == "e":
		return None
	else:
		print("\n\n\n________________")
		print("Invalid Command")
		print("________________")
		return get_login_info()

def get_table_input(table_list):
	if len(table_list) == 0:
		raise Exception("No Table in List!")
		return None
	for i,table in enumerate(table_list):
		print("\n{}) Enter {} for {}".format(i+1,i+1,table))
	inp = input("\n")
	try:
		inp = int(inp)-1
		if inp in list(range(len(table_list))):
			return table_list[inp]
		else:
			raise Exception("\n\nInvalid Input!")
	except Exception as e:
		print(e)
		return get_table_input(table_list)

def get_input(field_name,field_type,tag="",func=None,end=""):
	form=""
	if field_type == "DATE":
		form = "(YY-MM-DD)"
	elif field_type == "BOOLEAN":
		form = "(TRUE/FALSE,1/0)"
	inp = input(tag+" "+field_name+"{} :".format(form)+end)
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
			print("\n\n")
			for field,field_value in zip(field_list,row):
				print(field," : ",field_value," || ",end ="",sep="")
			print("\n\n")	


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

def make_join_query(table_name,join_table,table_view,join_table_view,foreign_keys):
	#SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
	fields =""
	for field in table_view.split(","):
		fields += table_name+"."+field+","
	
	for field in join_table_view.split(","):
		fields += join_table+"."+field+","
	fields = fields[:-1]
	query = "SELECT " + fields + " FROM " + table_name+" LEFT JOIN "+join_table+" ON "+ table_name+"."+foreign_keys[0]+"="+join_table+"."+foreign_keys[1]
	query += " and "+table_name+".DEL = FALSE"+" and "+join_table+".DEL = FALSE"
	return query,fields

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
		
		print("\nAdd this entry?(Y/N):")
		inp = input()
		if inp.lower() == "y":
			cursor.execute(query,values)
			connection.commit()
			print("\n\nEntry successfully added to table: "+table_name)
		else:
			print("\n\nEntry was not added\n")
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
		option_name = input("\n\n* Press Enter to view whole table \n\n* Enter 1 to JOIN Tables \n\n* Enter 2 to search with primary key value \n\n* Enter 3 to search with multiple key values\n\n* Enter anything else to exit\n\n")

		if option_name =="":
			cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE".format(view,table_name))
			data = cursor.fetchall()
			if len(data) == 0:
				raise Exception("\nData doesn't Exist")
			field_list = view.split(",")
			print_table_data(field_list,data)	
			#print(view)

			#for d in data:
			#	print(d)
		elif option_name =="1":
			#{"Patient_Outdoor":{"Report":["REPORT_ID","ID"],"Doctor":["DOC_ID","ID"]}
			#print(list(JOIN_ACCESS[table_name].keys()))
			#SELECT Orders.OrderID, Customers.CustomerName FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
			join_table_list = list(JOIN_ACCESS[table_name].keys())

			if len(join_table_list) == 0:	
				print("\n\nNo Connected Table Found!")
			else:
				join_table = get_table_input(join_table_list)
				if join_table not in list(TABLE_ACCESS[log_view]["R"].keys()):
					print("\n\nUser doesn't have access to Table\n")
				elif len(join_table_list) == 0:
					print("\n\nTables are not related\n")
				else:
					cursor.execute("SELECT * FROM {}".format(join_table))
					columns = cursor.description
					join_table_view = get_view(columns,TABLE_ACCESS[log_view]["R"][join_table])
					foreign_keys = JOIN_ACCESS[table_name][join_table]
					query,field_list = make_join_query(table_name,join_table,view,join_table_view,foreign_keys)
					
					cursor.execute(query)
					data = cursor.fetchall()
					if len(data) == 0:
						raise Exception("\n\nData doesn't Exist")
					field_list = field_list.split(",")
					print_table_data(field_list,data)
		

		elif option_name == "2": 
			key_value = input("\nEnter {} value: ".format(primary_key_name))
			cursor.execute("SELECT {} FROM {} WHERE DEL=FALSE and {}={}".format(view,table_name,primary_key_name,key_value))
			data = cursor.fetchall()
			if len(data) == 0:
				raise Exception("\n\nData doesn't Exist")
			field_list = view.split(",")

			print("\n\n Data for {} = {}:\n".format(primary_key_name,key_value))
			print_table_data(field_list,data)	
			#print("\n\n Data for {} = {}:\n".format(primary_key_name,key_value))	
			#for i,d in zip(field_list,data[0]):
			#	print(i," :",d)
		elif option_name == "3":	
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
						conditions.append(("<=",field_name))
						condition_values.append(key)
						key = get_input(field_name,field_type,tag="\nMIN VALUE of ")
						if key !="":
							conditions.append((">=",field_name))
							condition_values.append(key)
					elif field_type in CONDITION_FIELDS and key ==">" :
						key = get_input(field_name,field_type,tag="\nMIN VALUE of ")
						conditions.append((">=",field_name))
						condition_values.append(key)
						key = get_input(field_name,field_type,tag="\nMAX VALUE of ")
						if key !="":
							conditions.append(("<=",field_name))
							condition_values.append(key)
					else:
						key_names.append(key_name)
						key_values.append(key)

			if len(key_names)!=0 or len(conditions)!=0:
				query = make_retrieve_query(table_name,view,key_names,conditions)
				key_values = key_values + condition_values
				key_values = tuple(key_values)
				cursor.execute(query,key_values)
				data = cursor.fetchall()

				if len(data) == 0:
					raise Exception("\n\nData doesn't Exist")
				field_list = view.split(",")
				print_table_data(field_list,data)
			else:
				print("\n\nNo Fields selected")
			#print(view)
			#for d in data:
			#	print(d)
	except Exception as e:
		print(e)

def update(table_name,connection,cursor,log_view):	
	try:
		print("\n\nUpdating in: "+table_name)
		cursor.execute("SHOW KEYS FROM {} WHERE Key_name = 'PRIMARY'".format(table_name))
		primary_keys = cursor.fetchall()
		key_name = primary_keys[0][4]
		key_value = input("\n\nInput "+key_name+" of row you want to update: ")
		cursor.execute("SELECT * FROM {} WHERE {} = {}".format(table_name,key_name,key_value))
		if len(cursor.fetchall()) == 0:
			raise Exception("\n\nData doesn't exist")		
		print("\nPress Enter if you don't want to change a field")

		cursor.execute("SELECT * FROM {}".format(table_name))
		columns = cursor.description
		columns = get_view(columns,TABLE_ACCESS[log_view]["U"][table_name]).split(",")
		
		#columns = ALL_VIEWS[table_name][log_view].split(",")
		values = []
		field_list = []
		for column in columns:
			cursor.execute("SELECT {} FROM {} WHERE {} = {}".format(column,table_name,key_name,key_value))
			field_type = FieldType.get_info(cursor.description[0][1])
			field_name = cursor.description[0][0]
			field_data = cursor.fetchall()[0][0]

			inp = get_input(column,field_type,end=" {}  New Value:  ".format(field_data))
			if inp !="":			
				values.append(inp)
				field_list.append(column)
		if len(field_list)!=0:	
			values = tuple(values)
			query = make_update_query(table_name,field_list,key_name,key_value)

			print("\nUpdate this entry?(Y/N):")
			inp = input()
			if inp.lower() == "y":
				cursor.execute(query,values)
				connection.commit()
				print("\n\nEntry successfully updated in table: "+table_name)
			else:
				print("\n\nEntry was not updated\n")
		else:
			print("\n\nNo Field Selected")		

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
			raise Exception("\n\nData doesn't exist")

		soft_delete = True

		if log_view == "management_view": 
			while True:	
				del_type = input("\n\nEnter 1 for Soft Delete and 2 for Hard Delete: \n")
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
				raise Exception("\n\nData doesn't exist")
			cursor.execute("SELECT * FROM {}".format(table_name))
			columns = cursor.description
			columns = get_view(columns,TABLE_ACCESS[log_view]["R"][table_name])
			field_list = columns.split(",")

			#field_list = ALL_VIEWS[table_name][log_view].split(",")

			print("\n\n")
			for i,d in zip(field_list,data[0]):
				print(i," : ",d)
			print("\n\nDo you want to delete the Entry: (Y/N)")
			ans = input()
			if ans.lower()=="y" :
				query = "UPDATE {} SET DEL=TRUE WHERE {}={}".format(table_name,key_name,key_value)
				cursor.execute(query)
				connection.commit()
				print("\n\nEntry deleted successfully")
			else:
				print("\n\nEntry was not deleted")
		else:
			query = "SELECT * FROM {} WHERE {} = {}".format(table_name,key_name,key_value)	
			cursor.execute(query)
			data = cursor.fetchall()
			
			cursor.execute("SELECT * FROM {}".format(table_name))
			columns = cursor.description
			columns = get_view(columns,TABLE_ACCESS[log_view]["R"][table_name])
			field_list = columns.split(",")

			#field_list = ALL_VIEWS[table_name][log_view].split(",")
			print("\n\n")
			for i,d in zip(field_list,data[0]):
				print(i," :",d)
			print("\nDo you want to permanently delete the Entry: (Y/N): ")
			ans = input()
			if ans.lower() =="y" :
				query = "DELETE FROM {} WHERE {}={}".format(table_name,key_name,key_value)
				cursor.execute(query)
				connection.commit()
				print("\n\nEntry deleted successfully")
			else:
				print("\n\nEntry was not deleted")

	except Exception as e:
		print(e)
		connection.rollback()

if __name__ == "__main__":
	connection,cursor = connect2server("medical database")

	for view in list(TABLE_ACCESS.keys()):
		for action in ["C","R","U"]:
			for table in list(TABLE_ACCESS[view][action].keys()):
				cursor.execute("SELECT * FROM {}".format(table))
				columns = cursor.description
				cols = get_view(columns,TABLE_ACCESS[view][action][table])
				print(view,action,table,"       ",cols)#,"       ",TABLE_ACCESS[view][action][table]) 

			print("\n\n")
	#create("Patient_Admission",connection,cursor,"doctor_view")
	#retrieve("Report",connection,cursor,"staff_view")
	#update("Patient_Admission",connection,cursor,"staff_view")
	#delete("Patient_Outdoor",connection,cursor,"doctor_view")

	connection.close()

