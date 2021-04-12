import mysql.connector

from database_python import *


connection,cursor = connect2server("medical database")


create("Patient_Admission",connection,cursor)
#retrieve("Patient_Outdoor",connection,cursor)
#update("Patient_Admission",connection,cursor)
#delete("Patient_Outdoor",connection,cursor)

connection.close()