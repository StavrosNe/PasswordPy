import sqlite3
from sqlite3 import Error
from encryption import hash
from encryption import create_salt
from encryption import create_pepper

class ChangePassword():
    def __init__(self,username:str,new:str,database:str):
        """
        this class has the methods
        needed to change password
        """
        
        # must store new password hashed
        self.username = username
        self.database = database

        self.salt = create_salt(32)
        self.pepper = create_pepper()
        recipe = self.salt+new+self.pepper
        self.new_password = hash(recipe)

    def commit_change(self):
        def create_connection():
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(self.database)
            except Error as e:
                print(e)

            return conn
        
        def update(conn):
            c = conn.cursor()
            sql = 'UPDATE users SET password=?,salt=? WHERE username=?'
            c.execute(sql, (self.new_password, self.salt,self.username))
            conn.commit()
        
        conn = create_connection()

        try:
            with conn:
                update(conn)
            conn.close()
        except Exception as error:
            print(error)
            conn.close()
            
    
