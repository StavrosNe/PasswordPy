import sqlite3
from sqlite3 import Error
from encryption import hash
from encryption import create_salt
from encryption import create_pepper

class UsersDb():
    def __init__(self,database) -> None:
        self.database = database
    
    def fetch_usernames(self):

        def fetch(conn):
            cur = conn.cursor()
            cur.execute("SELECT username FROM users")

            rows = cur.fetchall()

            usernames = [row[0] for row in rows]

            return usernames
        
        
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
                usernames = fetch(conn)
            conn.close()
            return usernames
        except Exception as error:
            print(error)
            conn.close()

    
    def add_user(self,username,password,email):
        # salt is 32 digit string
        salt = create_salt(32)
        pepper = create_pepper()

        def create_connection():
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(self.database)
            except Error as e:
                print(e)

            return conn
        
        def create_table(conn):      
            table_schema = '''CREATE TABLE IF NOT EXISTS users(
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            salt TEXT NOT NULL
            );'''
            
            cur = conn.cursor()
            cur.execute(table_schema)
            conn.commit()


        def create_user(conn, user):
                    
            sql = ''' INSERT INTO users(username,password,email,salt)
                    VALUES(?,?,?,?);'''
            
            cur = conn.cursor()
            cur.execute(sql, user)
            conn.commit()

        conn = create_connection()
        
        try:
            with conn:
                # create table
                create_table(conn)
                # create a new user
                recipe = salt+password+pepper
                password = hash(recipe)
                user = (username,password,email,salt)
                create_user(conn, user)
            conn.close()

        except Exception as error:
            print(error)
            conn.close()
    
    def authenticate(self,salt,stored_hash,password):
        pepper_list = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
        flag = False
        for pepper in pepper_list:
            recipe = salt+password+pepper
            new_hash = hash(recipe)
            if new_hash == stored_hash:
                flag = True
                break
            else:
                pass

        return flag

    def database_empty(self):
        def create_connection():
            """ create a database connection to a SQLite database """
            conn = None
            try:
                conn = sqlite3.connect(self.database)
            except Error as e:
                print(e)

            return conn

        def table_exists(conn):
            cursor = conn.cursor()
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='users' ")
            return cursor.fetchone() is not None

        def check(conn):
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM users')
            count = cursor.fetchone()[0]
            if count==0:
                return True
            else:
                return False
            
        conn = create_connection()

        if table_exists(conn):
            try:
                with conn:
                    conn.close()
                    return check(conn)
            except Exception as error:
                print(error)
                conn.close()
        else:
            conn.close()
            return True
            
        
    
    def fetch_user(self,username):

        def fetch(conn):
            cursor = conn.cursor()
            sql = '''SELECT password, email ,salt FROM users WHERE username = ?'''
            cursor.execute(sql, (username,))
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
            conn.close()
            return user_data
        except Exception as error:
            print(error)
            conn.close()
    
