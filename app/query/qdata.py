import customtkinter as ctk
from customwidget import SegButton
import os
from PIL import Image
from webops import Website
import pyperclip

class QuerryData(ctk.CTkFrame):

    def __init__(self,
                 master: any,
                 **kwargs):    
        """
        Class that inherits 
        from ctk.CTkFrame
        """
        super().__init__(master=master, 
                         width=500, 
                         height=500,
                         corner_radius=20,
                         **kwargs)
        
        ctk.set_default_color_theme("dark-blue")
 
        project_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # import images
        globe_filepath = os.path.join(project_directory, "images","globe.png")
        globe_img = Image.open(globe_filepath)
        globe = ctk.CTkImage(globe_img,size=(30, 30))

        copy_filepath = os.path.join(project_directory, "images","copying.png")
        copy_img = Image.open(copy_filepath)
        copy = ctk.CTkImage(copy_img,size=(30, 30))

        # create widgets
        self.segbutton = SegButton(ratio1=0.6,ratio2=0.4,text1='Query App',
                                   text2='Show Apps', 
                                   master=self)
        
        self.titlelabel = ctk.CTkLabel(master=self,
                                        text = 'Query App', 
                                        font=("Helvetica",36))
        
        self.application_entry = ctk.CTkEntry(master=self,
                                    width = 300,height=40,
                                    placeholder_text="Application name",
                                    font=("Roboto",18),corner_radius=10)
        
        self.username_entry = ctk.CTkEntry(master=self,
                                    width = 300,height=40,
                                    placeholder_text="Username",
                                    font=("Roboto",18),corner_radius=10)
        
        self.password_entry = ctk.CTkEntry(master=self,
                                    width = 300,height=40,
                                    placeholder_text="Password",
                                    font=("Roboto",18),corner_radius=10)
        
        self.email_entry = ctk.CTkEntry(master=self,
                                    width = 300,height=40,
                                    placeholder_text="Email",
                                    font=("Roboto",18),corner_radius=10)
        
        self.message = ctk.CTkLabel(master=self ,
                                    text = '', 
                                    font=("Roboto",18))
        
        self.globe_btn = ctk.CTkButton(master=self,
                                        height = 40,width = 40,
                                        text="",
                                        fg_color='transparent',
                                        image = globe,
                                        hover=False,
                                        command = self.open_website)
        self.copy_btn1 = ctk.CTkButton(master=self,
                                        height = 40,width = 40,
                                        text="",
                                        fg_color='transparent',
                                        image = copy,
                                        hover=False,
                                        command = self.copy_username)                      
        
        self.copy_btn2 = ctk.CTkButton(master=self,
                                        height = 40,width = 40,
                                        text="",
                                        fg_color='transparent',
                                        image = copy,
                                        hover=False,
                                        command = self.copy_password)
        
        # place widgets
        self.titlelabel.place(anchor = 'n' , relx = 0.5 , rely = 0.03)
        self.application_entry.place(anchor='n',relx = 0.5,rely = 0.15)
        self.globe_btn.place(anchor = 'n' , relx = 0.9 , rely = 0.15)
        self.username_entry.place(anchor='n',relx = 0.5,rely = 0.3)
        self.copy_btn1.place(anchor = 'n' , relx = 0.9 , rely = 0.3)
        self.password_entry.place(anchor='n',relx = 0.5,rely = 0.45)
        self.copy_btn2.place(anchor = 'n' , relx = 0.9 , rely = 0.45)
        self.email_entry.place(anchor='n',relx = 0.5,rely = 0.6)
        self.segbutton.place(anchor='n',relx = 0.5,rely = 0.75)
        self.message.place(anchor='n',relx = 0.5,rely = 0.9)

    def reset_entries(self):
        self.message.configure(text='')  
        w2 = self.username_entry.get()
        self.username_entry.delete(0,(len(w2)))

        w3 = self.password_entry.get()
        self.password_entry.delete(0,(len(w3)))

        w4 = self.email_entry.get()
        self.email_entry.delete(0,(len(w4)))

    def switch_frame(self):
        self.message.configure(text='')
        w1 = self.application_entry.get()
        self.application_entry.delete(0,(len(w1)))

        w2 = self.username_entry.get()
        self.username_entry.delete(0,(len(w2)))

        w3 = self.password_entry.get()
        self.password_entry.delete(0,(len(w3)))

        w4 = self.email_entry.get()
        self.email_entry.delete(0,(len(w4)))

    def validate(self,app_list):
        self.message.configure(text='')
        app = self.application_entry.get()

        validation = True
        if app_list is not None:
            if app not in app_list :
                validation =  False
    
            elif app.isspace() or len(app)==0 :
                validation =  False
        else:
            if app.isspace() or len(app)==0 :
                validation =  False

        if validation == False:
            self.reset_entries()
            self.message.configure(text='Unable to query app')

        return validation
    
    def open_website(self):
        app_name = self.application_entry.get()
        if app_name.isspace() or len(app_name)==0:
            pass
        else:
            website = Website(app_name=app_name)
            website.open()

    def copy_username(self):
        username = self.username_entry.get()
        pyperclip.copy(username)

    def copy_password(self):
        password = self.password_entry.get()
        pyperclip.copy(password)
    


