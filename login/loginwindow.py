import customtkinter as ctk
import os
from encryption import hash
import register 
from PIL import Image
from app import Application
from dbops.usersdb import UsersDb 

class LoginWin(ctk.CTk):
    def __init__(self):
        """
        Class that inherits 
        from ctk.CTk class
        """
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color = '#0D0D0D')
        self.title('Log in')
        
        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        #database
        db_filepath = os.path.join(project_directory,"databases","unp.db")
        self.database = str(db_filepath)

        show_filepath = os.path.join(project_directory, "assets","show.png")
        show_img = Image.open(show_filepath)
        show = ctk.CTkImage(show_img,size=(30, 30))

        bg_img_filepath = os.path.join(project_directory, "assets","rt5.jpg")

        bg_img = Image.open(bg_img_filepath)
        w  = 1280
        h = 720
        background = ctk.CTkImage(bg_img,size=(w*0.6, h))

        arrow_filepath = os.path.join(project_directory, "assets","arrow.png")
        arrow_img = Image.open(arrow_filepath)
        self.arrow = ctk.CTkImage(arrow_img,size=(30, 30))

        # create database object to abstract database operations
        self.db = UsersDb(database = self.database)

        self.label = ctk.CTkLabel(master = self,image = background,text='')

        self.frame = ctk.CTkFrame(master = self, width=450, 
                         height=450,corner_radius=20,
                         border_color = '#251351' , border_width = 3)

        self.titlelabel = ctk.CTkLabel(master=self.frame ,
                                        text = 'Password manager', 
                                        font=("Helvetica",36))

        self.username_entry = ctk.CTkEntry(master=self.frame,
                                    width = 300,height=40,
                                    placeholder_text="Username",
                                    font=("Roboto",18),corner_radius=10)
        
        self.password_entry = ctk.CTkEntry(master=self.frame,
                                    width = 300,height=40,
                                    placeholder_text="Password",
                                    font=("Roboto",18),corner_radius=10,
                                    show='*')

        self.login_btn = ctk.CTkButton(master=self.frame,
                                    width = 200,height=40,
                                    text="Log in",
                                    font=("Roboto",18),corner_radius=10,
                                    command = self.login)
        
        self.signup_btn = ctk.CTkButton(master=self.frame,
                                    width = 200,height=40,
                                    text="Sign up",
                                    font=("Roboto",18),corner_radius=10,
                                    command = self.signup)
        
        self.forgot_password = ctk.CTkButton(master=self.frame,
                                    width = 0,height=0,
                                    text="forgot password?",
                                    font=("Roboto",15,'underline'),
                                    corner_radius=0,
                                    fg_color='transparent',
                                    hover_color='#505050' , 
                                    command=self.change_pass)
        
        self.show_btn = ctk.CTkButton(master=self.frame,
                                    height = 40,width = 40,
                                    text="",
                                    fg_color='transparent',
                                    image = show,
                                    hover=False)
                                    
        self.message = ctk.CTkLabel(master=self.frame ,
                                        text = '', 
                                        font=("Roboto",18))
        
        self.usernamemessage = ctk.CTkLabel(master=self.frame ,
                                        text = '', 
                                        font=("Roboto",14))
        
        self.passwordmessage = ctk.CTkLabel(master=self.frame ,
                                        text = '', 
                                        font=("Roboto",14))
        
        self.label.place(relx = 0 , rely = 0 , anchor = 'nw')
        
        self.frame.place(relx=0.8 ,rely=0.5 ,anchor='center')
                                                     
        self.titlelabel.place(anchor = 'n' , relx = 0.5 , rely = 0.05)

        self.usernamemessage.place(anchor = 'n' , relx = 0.5 , rely = 0.17)
        
        self.username_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.24)

        self.password_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.38)

        self.forgot_password.place(anchor = 'n' , relx = 0.32 , rely = 0.48)

        self.login_btn.place(anchor = 'n' , relx = 0.5 , rely = 0.64)

        self.signup_btn.place(anchor = 'n' , relx = 0.5 , rely = 0.78)

        self.message.place(anchor = 'n' , relx = 0.5 , rely = 0.9)

        self.show_btn.place(anchor = 'n' , relx = 0.9 , rely = 0.38)

        self.show_btn.bind('<ButtonPress-1>',self.show)
        self.show_btn.bind('<ButtonRelease-1>',self.hide)

    def show(self,event):
        self.password_entry.configure(show='')

    def hide(self,event):
        self.password_entry.configure(show='*')  

    def validate(self,username,password):
        user_data = self.db.fetch_user(username)
        correct_password = True
        correct_username = True
        empty_database = self.db.database_empty()

        if empty_database:
            self.message.configure(text = 'Did you sign up?')

        else:
            if user_data is None:
                correct_username = False
                self.usernamemessage.configure(text = '*wrong username')
                self.passwordmessage.configure(text = '')
                self.message.configure(text = 'Unsuccessful authentication')
            else:
                stored_password = user_data[0]
                email = user_data[1]
                salt = user_data[2]
                valid = self.db.authenticate(salt=salt,stored_hash=stored_password,password=password)
                if not valid:
                    self.passwordmessage.place(anchor = 'n' , relx = 0.5 , rely = 0.335)
                    self.message.configure(text = 'Unsuccessful authentication')
                    self.passwordmessage.configure(text = '*wrong password')
                    self.usernamemessage.configure(text = '')
                    self.password_entry.place(anchor = 'n',relx = 0.5,rely = 0.4)
                    self.forgot_password.place(anchor = 'n',relx = 0.32,rely = 0.5)
                    self.show_btn.place(anchor = 'n' , relx = 0.9 , rely = 0.4)

                    correct_password = False
                else:
                    self.message.configure(text = 'Successful authentication')
                    self.reset()


        def eval(correct_password,correct_username,
                 empty_database):
            if correct_password == False:
                return False
            elif correct_username == False:
                return False
            elif empty_database == False:
                return False
            return True
        
        isvalid = eval(correct_password,correct_username,empty_database)

        return isvalid
                
    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        def check_len():
            len1 = len(self.username)
            len2 = len(self.password)

            if len1>=1 and len2>=1:
                return True
            else:
                return False
            
        check = check_len()
        try:
            assert check == True
            try:
                isvalid = self.validate(self.username,self.password)
                assert isvalid == True

            except AssertionError:
                pass
        
        except AssertionError:
            self.message.configure(text = 'Please fill out all fields')


    def change_pass(self):
        pass

    def reset(self):
        self.password_entry.place(anchor = 'n',relx = 0.5,rely = 0.38)
        self.forgot_password.place(anchor = 'n',relx = 0.32,rely = 0.48)
        self.show_btn.place(anchor = 'n' , relx = 0.9 , rely = 0.38)
        self.passwordmessage.configure(text = '')
        self.passwordmessage.place_forget()
        self.usernamemessage.configure(text = '')
        self.usernamemessage.place_forget()
        self.login_btn.configure(text = 'Continue',
                                 image = self.arrow,
                                 compound= 'right',
                                 command=self.continue_to_app)

    def continue_to_app(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        def main():
            app = Application(username,password)
            #getting screen width and height of display
            ws= app.winfo_screenwidth()
            hs= app.winfo_screenheight()
            
            # width and height of app
            w = 1280
            h = 720
            
            # coordiantes on where the app opens
            x = (ws/2) - (w/2)
            y  = (hs/2) - (h/2)
            
            #setting tkinter window size
            app.geometry('%dx%d+%d+%d' % (w,h,x,y))
            
            app.maxsize(1280, 720)

            app.resizable(False, False) 

            app.mainloop()
    
        self.destroy()
        main()


    def signup(self):
        def main():
            app = register.RegisterWin(self.database)
            #getting screen width and height of display
            ws= app.winfo_screenwidth()
            hs= app.winfo_screenheight()
            
            # width and height of app
            w = 1280
            h = 720
            
            # coordiantes on where the app opens
            x = (ws/2) - (w/2)
            y  = (hs/2) - (h/2)
            
            #setting tkinter window size
            app.geometry('%dx%d+%d+%d' % (w,h,x,y))
            
            app.maxsize(1280, 720)

            app.resizable(False, False) 
        
            app.mainloop()
    
        self.destroy()
        main()


