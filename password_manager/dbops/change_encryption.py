import sqlite3
from sqlite3 import Error
from encryption  import SafeEncrypt
from encryption import SafeDecrypt
from encryption import GenIv

class ChangeEncryption():
    def __init__(self,username:str,database:str,
                 old_key:str,new_key:str):
        self.username = username
        self.database = database
        self.old_key = old_key
        self.new_key = new_key

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
    
    def fetch_app(self,application):
    
        def unpack(message,vector):
            return SafeDecrypt(key=self.old_key,message=message,
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

    def temp_storage(self):
        appnames = self.fetch_appnames()
        app_dict = {}
        for app in appnames:
            app_dict[app] = self.fetch_app(app)

        return app_dict
    
    def add_app(self,application,username,password,email):
        
        username_iv = GenIv.iv1()
        password_iv = GenIv.iv1()
        email_iv = GenIv.iv1()

        application = application
        username_en = SafeEncrypt(key=self.new_key,message=username,
                                  iv=username_iv).encrypt()
        password_en = SafeEncrypt(key=self.new_key,message=password,
                                  iv=password_iv).encrypt()
        email_en = SafeEncrypt(key=self.new_key,message=email,
                               iv=email_iv).encrypt()
        
        app = (username_en,password_en,email_en,
                username_iv,password_iv,email_iv,
                application)
        
        print(app)

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
                    
            sql = """
            UPDATE {table}
            SET username = ?, password = ?, email = ?, username_iv = ?, password_iv = ?, email_iv = ?
            WHERE application = ?;
        """.format(table=self.username)
            cur = conn.cursor()
            cur.execute(sql, app)
            conn.commit()

        conn = create_connection()
        
        try:
            with conn:
                create_table(conn)
                create_app(conn, app)
                print('app created')
            conn.close()
        except Exception as error:
            print(error)
            conn.close()


    def commit_changes(self):
        dictionary = self.temp_storage()
        for item in dictionary.items():
            application = item[0]
            app_data  = item[1]
            username = app_data[0]
            password = app_data[1]
            email = app_data[2]
            self.add_app(application=application,
                         username=username,password=password,
                         email=email)