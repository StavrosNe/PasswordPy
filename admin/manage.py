import customtkinter as ctk
import os
from admin.password import Passframe
from PIL import Image

class ManageUser(ctk.CTkToplevel):
    def __init__(self,password:str,username:str):

        super().__init__()

        # appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color = '#0D0D0D')

        self.password = password
        self.username = username

        self.flag = ''

        self.attributes("-topmost", True)

        self.title('Manage Account')

        self.resizable(False, False)
        self.after(150, lambda: self.focus()) 

        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        pass_filepath = os.path.join(project_directory, "assets","padlock.png")
        pass_img = Image.open(pass_filepath)
        padlock = ctk.CTkImage(pass_img,size=(30, 30))

        email_filepath = os.path.join(project_directory, "assets","email.png")
        email_img = Image.open(email_filepath)
        email = ctk.CTkImage(email_img,size=(30, 30))

        info_filepath = os.path.join(project_directory, "assets","info.png")
        info_img = Image.open(info_filepath)
        information = ctk.CTkImage(info_img,size=(30, 30))
        #-------------------------------------------------------------

        self.frame1 = ctk.CTkFrame(master=self,width = 80,height=500,
                                   corner_radius=0 )

        self.frame2 = ctk.CTkFrame(master=self,width = 420,height=500,
                                   corner_radius=0,fg_color ="#0D0D0D")


        self.frame1.place(relx=0, rely=0 ,anchor = 'nw')

        self.frame2.place(relx=1, rely=0 ,anchor = 'ne')

        #-------------------------------------------------------------
        self.change_password = ctk.CTkButton(master=self.frame1,width=80,height=60,
                                             image = padlock,
                                             text = '',
                                             fg_color='transparent',
                                             hover_color='#505050',
                                             corner_radius=0,
                                             command = self.change_pass_command)
        
        self.change_email = ctk.CTkButton(master=self.frame1,width=80,height=60,
                                            image = email,
                                            text = '',
                                            fg_color='transparent',
                                            hover_color='#505050',
                                            corner_radius=0,
                                            command = self.change_email_command)
        
        self.info = ctk.CTkButton(master=self.frame1,width=80,height=60,
                                            image = information,
                                            text = '',
                                            fg_color='transparent',
                                            hover_color='#505050',
                                            corner_radius=0,
                                            command = self.info_command)
        #-------------------------------------------------------------

        self.change_password.place(relx=0.5,rely=0,anchor='n')

        self.change_email.place(relx=0.5,rely=0.15,anchor='n')

        self.info.place(relx=0.5,rely=0.3,anchor='n')

        #-------------------------------------------------------------
        self.password_frame = Passframe(master=self.frame2,
                                        password=self.password,
                                        username=self.username)
        #-------------------------------------------------------------

        self.email_frame = ctk.CTkFrame(master=self.frame2,width =420,
                                        height=600,corner_radius=0,
                                        fg_color='transparent')

        self.titlelabel2 =  ctk.CTkLabel(master=self.email_frame,width =300,
                                        height=60,
                                        font=("Roboto",22),
                                        text = 'Change Email')
        
        self.titlelabel2.place(relx = 0.5 , rely = 0, anchor='n' )

        #-------------------------------------------------------------
        
        self.info_frame = ctk.CTkFrame(master=self.frame2,width =420,
                                    height=600,corner_radius=0,
                                    fg_color='transparent')

        self.titlelabel3 =  ctk.CTkLabel(master=self.info_frame,width =300,
                                        height=60,
                                        font=("Roboto",22),
                                        text = 'User Info')
        
        self.titlelabel3.place(relx = 0.5 , rely = 0, anchor='n' )

        #-------------------------------------------------------------

    def change_pass_command(self):

        if self.flag=='':
            pass
        elif self.flag == 'email':
            self.email_frame.pack_forget()
        elif self.flag == 'info':
            self.info_frame.pack_forget()
        
        self.flag = 'password'

        self.password_frame.pack()

    def change_email_command(self):
        if self.flag=='':
            pass
        elif self.flag == 'password':
            self.password_frame.pack_forget()
        elif self.flag == 'info':
            self.info_frame.pack_forget()
        
        self.flag = 'email'

        self.email_frame.pack()

    def info_command(self):
        if self.flag=='':
            pass
        elif self.flag == 'password':
            self.password_frame.pack_forget()
        elif self.flag == 'email':
            self.email_frame.pack_forget()
        
        self.flag = 'info'

        self.info_frame.pack()
        









