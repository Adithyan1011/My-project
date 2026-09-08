import mysql.connector
class connectdb:
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

class GymMemberManager(connectdb):
    def get_object(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

connection_instance=connectdb
connection_instance.get_connection()