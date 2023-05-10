import sqlite3
from sqlite3 import Error
from encryption  import SafeEncrypt
from encryption import SafeDecrypt
from encryption import GenIv

class ApplicationsDb():
    def __init__(self,database:str,username:str,key:str) -> None:
        self.database = database
        self.key = key
        self.username = username
    
    def add_app(self,application,username,password,email):
        
        username_iv = GenIv.iv1()
        password_iv = GenIv.iv1()
        email_iv = GenIv.iv1()

        application = application
        username_en = SafeEncrypt(key=self.key,message=username,
                                  iv=username_iv).encrypt()
        password_en = SafeEncrypt(key=self.key,message=password,
                                  iv=password_iv).encrypt()
        email_en = SafeEncrypt(key=self.key,message=email,
                               iv=email_iv).encrypt()
        
        app = (application,username_en,password_en,email_en,
                username_iv,password_iv,email_iv)

        def create_connection():
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(self.database)
            except Error as e:
                print(e)

            return conn
        
        def create_table(conn):
                        
            table_schema = f'''CREATE TABLE IF NOT EXISTS {self.username}(
            application TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            username_iv BLOB,
            password_iv BLOB,
            email_iv BLOB
            );'''
            
            cur = conn.cursor()
            cur.execute(table_schema)
            conn.commit()

        def create_app(conn, app):
                    
            sql = f'''INSERT INTO {self.username}(application,username,password,email,username_iv,password_iv,email_iv)
                      VALUES(?,?,?,?,?,?,?);'''
            
            cur = conn.cursor()
            cur.execute(sql, app)
            conn.commit()

        conn = create_connection()
        
        try:
            with conn:
                create_table(conn)
                create_app(conn, app)
            conn.close()
        except Exception as error:
            print(error)
            conn.close()


    def fetch_app(self,application):
    
        def unpack(message,vector):
            return SafeDecrypt(key=self.key,message=message,
                               iv=vector).decrypt()

        def fetch(conn):
            cursor = conn.cursor()
            sql = f'SELECT username,password,email,username_iv,password_iv,email_iv FROM {self.username} WHERE application = ?'
            cursor.execute(sql, (application,))
            user_data = cursor.fetchone()
            return user_data
        
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
                user_data = fetch(conn)
                app_data = user_data[0:3]
                ivs = user_data[3:6]
                decrypted_data = list(map(unpack,app_data,ivs))
            conn.close()
            return decrypted_data
        except Exception as error:
            print(error)
            conn.close()



    def fetch_appnames(self):

        def fetch(conn):
            cursor = conn.cursor()
            
            sql = f'''SELECT application FROM {self.username}'''
        
            cursor.execute(sql)
            rows = cursor.fetchall()
            apps = [row[0] for row in rows]

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
        

        
    def delete_app(self,application):
        
        def create_connection():
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(self.database)
            except Error as e:
                print(e)

            return conn

        def delete_credentials(conn):
            cursor = conn.cursor()
            sql = f'DELETE FROM {self.username} WHERE application=?'
            cursor.execute(sql,(application,))
            conn.commit()

        conn = create_connection()
        try:
            with conn:
                delete_credentials(conn)
            conn.close()
        except Exception as error:
            print(error)
            conn.close()


    