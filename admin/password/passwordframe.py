import customtkinter as ctk
from dbops import ChangeEncryption
from dbops import ChangePassword
import re
import os

class Passframe(ctk.CTkFrame):
    def __init__(self,master:any,password:str,username:str):

        super().__init__(master=master,
                         width=420, 
                         height=500,
                         corner_radius=0)

        self.password = password
        self.username = username

        self.configure(fg_color ="transparent")

        project_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        db_filepath1 = os.path.join(project_directory,"databases","unp.db")
        self.usersdb = str(db_filepath1)

        db_filepath2 = os.path.join(project_directory,"databases","applications.db")
        self.appsdb = str(db_filepath2)
        
        self.titlelabel =  ctk.CTkLabel(master=self,width =300,
                                        height=60,
                                        font=("Roboto",22),
                                        text = 'Change password')
        
        self.label1 = ctk.CTkLabel(master=self,width =300,
                                    height=40,
                                    font=("Roboto",18),
                                    text = 'Current password')
        
        self.oldpasswordentry = ctk.CTkEntry(master = self,
                                            width = 300,height=40,
                                            placeholder_text="Current password",
                                            font=("Roboto",18),corner_radius=10)
        
        self.label2 = ctk.CTkLabel(master=self,width =300,
                                    height=40,
                                    font=("Roboto",18),
                                    text = 'New password')
        
        self.newpasswordentry = ctk.CTkEntry(master = self,
                                        width = 300,height=40,
                                        placeholder_text="New Password",
                                        font=("Roboto",18),corner_radius=10)
        
        self.label3 = ctk.CTkLabel(master=self,width =300,
                                    height=40,
                                    font=("Roboto",18),
                                    text ='Confirm password')
        
        self.confirmentry = ctk.CTkEntry(master = self,
                                        width = 300,height=40,
                                        placeholder_text="Confirm password",
                                        font=("Roboto",18),corner_radius=10)
        

        self.change_password = ctk.CTkButton(master=self,width=100,height=40,
                                             font=('Roboto',18),
                                             text='Apply chnages',
                                             corner_radius=10,
                                             command = self.apply_password_change,
                                             )
        
        self.message =  ctk.CTkLabel(master=self,width =300,
                                           height=40,
                                           font=("Roboto",14),
                                           text = '')

        self.titlelabel.place(relx = 0.5 , rely = 0, anchor='n' )
        self.label1.place(relx = 0.5 , rely = 0.14, anchor='n')
        self.oldpasswordentry.place(relx = 0.5 , rely = 0.2, anchor='n' )
        self.label2.place(relx = 0.5 , rely = 0.34, anchor='n')
        self.newpasswordentry.place(relx = 0.5 , rely = 0.4, anchor='n' )
        self.label3.place(relx = 0.5 , rely = 0.54, anchor='n')
        self.confirmentry.place(relx = 0.5 , rely = 0.6, anchor='n' )
        self.change_password.place(relx = 0.5 , rely = 0.75, anchor='n' )
        self.message.place(relx = 0.5 , rely = 0.85, anchor='n' )

    def password_strength(self,password):
        capital_letter_regex = r'[A-Z]'
        number_regex = r'\d'
        space_regex = r'\s'
        special_char_regex = r'[!@#$%&.?+-]'
        condition1 = re.search(capital_letter_regex, password)
        condition2 = re.search(number_regex, password)
        condition3 = re.search(space_regex, password)
        condition4 = re.search(special_char_regex, password)
        condition5 = len(password) >= 8 
        if  (condition1 and condition2 and not condition3 
             and condition4 and condition5):
            return True
        else:
            return False

    def apply_password_change(self):
        oldpassword = self.password
        provided_old_password =  self.oldpasswordentry.get()
        newpassword = self.newpasswordentry.get()
        confirm = self.confirmentry.get()

        condition1 = oldpassword==provided_old_password
        condition2 = self.password_strength(newpassword)
        condition3 = newpassword==confirm

        try:
            assert condition1==True, "Have you forgotten your password?"
            assert condition2==True, "Invalid password"
            assert condition3==True, "Unable to confirm password"

            change_password = ChangePassword(username = self.username,
                                             new = newpassword,
                                             database = self.usersdb)
            change_password.commit_change()

            self.confirmed_new_password = newpassword

            self.message.configure(text='Changes applied successfully')

        except AssertionError as error:
            self.message.configure(text=error)
        
