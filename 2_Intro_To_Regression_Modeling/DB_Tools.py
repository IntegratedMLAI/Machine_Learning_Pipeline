import pyodbc
import platform


class DB:
    """ A small class to connect to and provide the cursor to a database """
    def __init__(self, database='my_database_name'):
        self.database = database
        computer_name = platform.node()
        if computer_name == 'computer_name_1':
            self.conn = pyodbc.connect(
                driver='{SQL Server Native Client 11.0}', server='server_1',
                database=self.database,
                user='db_admin_username', password='db_admin_password')
        elif computer_name == 'computer_name_2':
            self.conn = pyodbc.connect(
                driver='{SQL Server Native Client 11.0}', server='server_2',
                database=self.database,
                trusted_connection='yes')

        self.cursor = self.conn.cursor()


db = DB()
# now you can use db.cursor and pass it around inside your app