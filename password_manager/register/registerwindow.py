import customtkinter as ctk
import os
import login
from PIL import Image
import re
from dbops.usersdb import UsersDb

class RegisterWin(ctk.CTk):
    def __init__(self,db_filepath):
        """
        Class that inherits 
        from ctk.CTk class
        """
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color = '#0D0D0D')
        self.title('Sign up')

        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # import images
        show_filepath = os.path.join(project_directory, "images","show.png")
        show_img = Image.open(show_filepath)
        show = ctk.CTkImage(show_img,size=(30, 30))

        bg_img_filepath = os.path.join(project_directory, "images","rt5.jpg")
        bg_img = Image.open(bg_img_filepath)
        w  = 1280
        h = 720
        background = ctk.CTkImage(bg_img,size=(w*0.6, h))

        arrow_filepath = os.path.join(project_directory, "images","arrow.png")
        arrow_img = Image.open(arrow_filepath)
        self.arrow = ctk.CTkImage(arrow_img,size=(30, 30))

        # create database object to abstract database operations
        self.database = db_filepath
        self.db = UsersDb(database = self.database)

        # create widgets
        self.label = ctk.CTkLabel(master = self,image = background,text='')

        self.frame = ctk.CTkFrame(master = self, width=450, 
                         height=500,corner_radius=20,
                         border_color = '#251351' , border_width = 3)

        self.titlelabel = ctk.CTkLabel(master=self.frame ,
                                        text = 'Sign up', 
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
        
        self.password_entry_rep = ctk.CTkEntry(master=self.frame,
                                    width = 300,height=40,
                                    placeholder_text="Confirm Password",
                                    font=("Roboto",18),corner_radius=10,
                                    show='*')
        
        self.email_entry = ctk.CTkEntry(master=self.frame,
                                    width = 300,height=40,
                                    placeholder_text="Email Adress",
                                    font=("Roboto",18),corner_radius=10)
        
        self.submit_btn = ctk.CTkButton(master=self.frame,
                                    width = 200,height=40,
                                    text="Sign up",
                                    font=("Roboto",18),corner_radius=10,
                                    command = self.register)
        
        self.show_btn = ctk.CTkButton(master=self.frame,
                                    height = 40,width = 40,
                                    text="",
                                    fg_color='transparent',
                                    image = show,
                                    hover=False)
        
        self.usernamemessage = ctk.CTkLabel(master=self.frame ,
                                        text = '', 
                                        font=("Roboto",14))
        
        self.passwordmessage = ctk.CTkLabel(master=self.frame ,
                                        text = '', 
                                        font=("Roboto",14))
        
        self.emailmessage = ctk.CTkLabel(master=self.frame ,
                                        text = '', 
                                        font=("Roboto",14))

        self.message = ctk.CTkLabel(master=self.frame ,
                                        text = '', 
                                        font=("Roboto",18))
        
        # place widgets
        self.label.place(relx = 0 , rely = 0 , anchor = 'nw')
        
        self.frame.place(relx=0.8 ,rely=0.5 ,anchor='center')
        
        self.titlelabel.place(anchor = 'n' , relx = 0.5 , rely = 0.05)

        self.username_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.2)

        self.password_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.32)

        self.password_entry_rep.place(anchor = 'n' , relx = 0.5 , rely = 0.44)

        self.email_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.56)

        self.submit_btn.place(anchor = 'n' , relx = 0.5 , rely = 0.68)

        self.show_btn.place(anchor='center', relx = 0.9, rely = 0.36)

        self.message.place(anchor = 'n' , relx = 0.5 , rely = 0.8)

        self.usernamemessage.place(anchor = 'n' , relx = 0.5 , rely = 0.14)

        # bind show button to either show or hide password
        self.show_btn.bind('<ButtonPress-1>',self.show)
        self.show_btn.bind('<ButtonRelease-1>',self.hide)

    def show(self,event):
        self.password_entry.configure(show='')

    def hide(self,event):
        self.password_entry.configure(show='*')  

    def password_strength(self,password):
        capital_letter_regex = r'[A-Z]'
        number_regex = r'\d'
        space_regex = r'\s'
        special_char_regex = r'[!@#$%&.?+-]'
        space_regex = r'\s'
        condition1 = re.search(capital_letter_regex, password)
        condition2 = re.search(number_regex, password)
        condition3 = re.search(space_regex, password)
        condition4 = re.search(special_char_regex, password)
        condition5 = len(password) >= 8
        condition6 = re.search(space_regex, password)
        if  (condition1 and condition2 and not condition3 
             and condition4 and condition5 and not condition6):
            return True
        else:
            return False
        
    def validate_email(self,email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email) is not None:
            return True
        else:
            return False 
            
    def username_taken(self,username):
        usernames = self.db.fetch_usernames()
        if usernames is None:
            return False
        else:
            if username in usernames:
                return True
            else:
                return False

    def validate(self,username,password,password_rep,email):
        
        username_valid = True
        password_valid = True
        email_valid  = True
        passwords_match = True
        # check if username is taken
        if self.username_taken(username):
            username_valid = False
        # check if password matches requirements
        if not self.password_strength(password):
             password_valid = False
        # check if password equals username
        if password == username:
            password_valid = False
        # check if password and password repeated match
        if password!=password_rep:
            passwords_match = False
        # check if email is valid
        if not self.validate_email(email):
            email_valid = False

        # apply changes to widgets
        if username_valid == False:
            string = '*username already in use'
            self.usernamemessage.configure(text = string)
        if email_valid == False:
            string = '*invalid email'
            self.emailerror(string)
        if password_valid==False:
            string = '*weak password'
            self.passworderror(string)
        if passwords_match==False:
            string = '*passwords dont match'
            self.passworderror(string)
        if email_valid==False and password_valid==False:
            string1 = '*weak password'
            string2 = '*invalid email'
            self.doublerror(string1,string2)
        if email_valid==False and passwords_match==False:
            string1 = '*passwords dont match'
            string2 = '*invalid email'
            self.doublerror(string1,string2)
        if password_valid==False and passwords_match==False:
            string = '*passwords dont match and weak password'
            self.passworderror(string)
        if password_valid==False and passwords_match==False and email_valid==False:
            string1 = '*passwords dont match and weak password'
            string2 = '*invalid email'
            self.doublerror(string1,string2)

        def eval(password_valid,email_valid,
                passwords_match,username_valid):
            if password_valid == False:
                return False
            elif username_valid == False:
                return False
            elif passwords_match == False:
                return False
            elif email_valid == False:
                return False
            return True
        
        isvalid = eval(password_valid,email_valid,
                       passwords_match,username_valid)
        
        return isvalid

        
    def register(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.password_rep = self.password_entry_rep.get()
        self.email = self.email_entry.get()

        def entries_filled():
            len1 = len(self.username)
            len2 = len(self.password)
            len3 = len(self.password_rep)
            len4 = len(self.email)
            if len1>=1 and len2>=1 and len3>=1 and len4>=1:
                return True
            else:
                return False
            
        # check if all entries have been filled
        check = entries_filled()
        try:
            assert check==True
            isvalid = self.validate(self.username,self.password,
                                    self.password_rep,self.email)
            try:
                assert isvalid == True
                self.db.add_user(self.username,self.password,self.email)
                self.reset_entries()
            except AssertionError:
                self.message.configure(text = 'Unable to register user')

        except AssertionError:
            self.message.configure(text = 'Please fill out all fields')

    
    def passworderror(self,string):
        self.usernamemessage.configure(text = '')
        self.emailmessage.configure(text = '')
        self.passwordmessage.configure(text = '')
        self.passwordmessage.configure(text = string)

        self.username_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.2)

        self.passwordmessage.place(anchor = 'n' , relx = 0.5 , rely = 0.305)

        self.password_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.37)

        self.show_btn.place(anchor='center', relx = 0.9, rely = 0.41)

        self.password_entry_rep.place(anchor = 'n' , relx = 0.5 , rely = 0.49)

        self.email_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.61)

        self.submit_btn.place(anchor = 'n' , relx = 0.5 , rely = 0.73)

        self.message.place(anchor = 'n' , relx = 0.5 , rely = 0.85)

    def emailerror(self,string):
        self.usernamemessage.configure(text = '')
        self.emailmessage.configure(text = '')
        self.passwordmessage.configure(text = '')
        self.emailmessage.configure(text = string)

        self.titlelabel.place(anchor = 'n' , relx = 0.5 , rely = 0.05)

        self.username_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.2)

        self.password_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.32)

        self.show_btn.place(anchor='center', relx = 0.9, rely = 0.36)

        self.password_entry_rep.place(anchor = 'n' , relx = 0.5 , rely = 0.44)

        self.emailmessage.place(anchor = 'n' , relx = 0.5 , rely = 0.545)

        self.email_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.61)

        self.submit_btn.place(anchor = 'n' , relx = 0.5 , rely = 0.73)

        self.message.place(anchor = 'n' , relx = 0.5 , rely = 0.85)

    def doublerror(self,string1,string2):
        self.usernamemessage.configure(text = '')
        self.emailmessage.configure(text = '')
        self.passwordmessage.configure(text = '')
        self.passwordmessage.configure(text = string1)
        self.emailmessage.configure(text = string2)

        self.titlelabel.place(anchor = 'n' , relx = 0.5 , rely = 0.05)

        self.username_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.2)

        self.passwordmessage.place(anchor = 'n' , relx = 0.5 , rely = 0.305)

        self.password_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.37)

        self.show_btn.place(anchor='center', relx = 0.9, rely = 0.41)

        self.password_entry_rep.place(anchor = 'n' , relx = 0.5 , rely = 0.49)

        self.emailmessage.place(anchor = 'n' , relx = 0.5 , rely = 0.595)

        self.email_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.66)

        self.submit_btn.place(anchor = 'n' , relx = 0.5 , rely = 0.78)

        self.message.place(anchor = 'n' , relx = 0.5 , rely = 0.9)


    def reset_entries(self):
        self.message.configure(text = 'User registered')
        self.emailmessage.configure(text = '')
        self.passwordmessage.configure(text = '')
        self.usernamemessage.configure(text = '')
        self.emailmessage.place_forget()
        self.passwordmessage.place_forget()
        self.usernamemessage.place_forget()
        
        self.submit_btn.configure(text = 'Continue',
                                  image = self.arrow,
                                  compound= 'right',
                                  command = self.login)
                                  
        self.username_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.2)

        self.password_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.32)

        self.show_btn.place(anchor='center', relx = 0.9, rely = 0.36)

        self.password_entry_rep.place(anchor = 'n' , relx = 0.5 , rely = 0.44)

        self.email_entry.place(anchor = 'n' , relx = 0.5 , rely = 0.56)

        self.submit_btn.place(anchor = 'n' , relx = 0.5 , rely = 0.68)

        self.message.place(anchor = 'n' , relx = 0.5 , rely = 0.8)

    def login(self):
        def main():
            ctk.set_default_color_theme("dark-blue")
            app = login.LoginWin()
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
        

        
