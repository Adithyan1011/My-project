import mysql.connector
class db_connect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Adithyan@123",
                database="companydb"
            )
            return self.connection
        except Exception as e:
            return None