import sqlite3
from sqlite3 import Error
from encryption import Encrypt,Decrypt
from encryption import hash
from encryption import create_salt
from encryption import create_pepper

# check if salt changes something
class ChangeEncryption():
    def __init__(self,current:str,username:str,new:str,database:str):

        self.oldpassword = current
        self.username=username
        self.newpassword = new
        self.database = database
        self.current = current


    def fetch_data(self):

        def fetch(conn):
            cursor = conn.cursor()
            
            sql = f'''SELECT application,username,password,email FROM {self.username}'''
        
            cursor.execute(sql)
            rows = cursor.fetchall()
            apps = [row for row in rows]

            return apps
        
        def create_connection():
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(self.database)
            except Error as e:
                print(e)

            return conn
        
        conn = create_connection()

        try:
            with conn:
                apps = fetch(conn)
            conn.close()
            return apps
        except Exception as error:
            print(error)
            conn.close()

    
    def temp_storage(self):
        def decrypt(message):
            return Decrypt(key=self.oldpassword,message=message).decrypt()
    
        data_list = self.fetch_data() # list containing tuples
        
        if data_list is not None:
            decrypted_data = [tuple(map(decrypt,tup)) for tup in data_list]
            return decrypted_data
       
        else:
            return None
        

    
    def encrypt_temp_data(self):
        def encrypt(message):
            return Encrypt(key=self.newpassword,message=message).encrypt()

        decrypted_data = self.temp_storage()

        if decrypted_data is not None:
            encrypted_data = [tuple(map(encrypt,tup)) for tup in decrypted_data]
            
            return encrypted_data
        else:
            return None
    

    def add2database(self,tuple,database):

        application = tuple[0]
        username = tuple[1]
        password = tuple[2]
        email = tuple[3]

        def create_connection():
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(database)
            except Error as e:
                print(e)

            return conn
        
        def create_table(conn):
                        
            table_schema = f'''CREATE TABLE IF NOT EXISTS {self.username}(
            application TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
            );'''
            
            cur = conn.cursor()
            cur.execute(table_schema)
            conn.commit()


        def create_app(conn, app):
                    
            sql = f'''INSERT INTO {self.username}(application,username,password,email)
                      VALUES(?,?,?,?);'''
            
            cur = conn.cursor()
            cur.execute(sql, app)
            conn.commit()

        conn = create_connection()
        
        try:
            with conn:
                # create table
                create_table(conn)
                # create a new app
                app = (application,username,password,email)
                create_app(conn, app)
                conn.close()
        except Exception as error:
            print(error)
            conn.close()

    def drop_table(self,database):
        def create_connection():
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(database)
            except Error as e:
                print(e)

            return conn
        
        def drop(conn):
            cursor = conn.cursor()
            cursor.execute(f"DROP TABLE {self.username}")
            conn.commit()

        conn = create_connection()

        try:
            with conn:
                drop(conn)
            conn.close()

        except Exception as error:
            print(error)
            conn.close()

    def commit_change(self):
        encrypted_data = self.encrypt_temp_data()
        self.drop_table(self.database)
        self.current = self.newpassword

        if encrypted_data is not None:
            for tup in encrypted_data:
                self.add2database(tup,self.database)


class ChangePassword():
    def __init__(self,username:str,new:str,database:str):
        
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
            
    
