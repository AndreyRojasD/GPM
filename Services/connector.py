import mysql.connector as connect
from dotenv import load_dotenv
import os
# This function retrieves connection credentials and establishes a connection with MySQL database
class dbconnector():
        def __init__(self):
            try:
                load_dotenv()
                USER = os.getenv('MYSQLUSER')
                PASSWORD = os.getenv('MYSQLPASSWORD')
                self.cnx = connect.connect(user=USER, password=PASSWORD,
                                    host='127.0.0.1', database='GPM')
                self.cursor = self.cnx.cursor()
            except Exception as e:
                return f"An error has occurred in the database connection. Please review the 'Services/connector.py' and '.env' files. Error: {str(e)}"
        def __enter__(self):
            return self.cursor

        def __exit__(self,exec_type, exec_val, exec_tb):
             self.cnx.commit()
             self.cursor.close()
             self.cnx.close()
