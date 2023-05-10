import customtkinter as ctk

class AddData(ctk.CTkFrame):

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
        '''
        self.configure(border_color = '#251351')
        self.configure(border_width=3)
        '''
        self.titlelabel = ctk.CTkLabel(master=self,
                                        text = 'Add App', 
                                        font=("Helvetica",36))
        
        
        self.add_btn = ctk.CTkButton(master=self, 
                                     width=200,height=40,
                                     text='Add App',
                                     font=("Roboto",18),corner_radius=10)

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

        self.titlelabel.place(anchor = 'n' , relx = 0.5 , rely = 0.03)

        self.application_entry.place(anchor='n',relx = 0.5,rely = 0.15)

        self.username_entry.place(anchor='n',relx = 0.5,rely = 0.3)

        self.password_entry.place(anchor='n',relx = 0.5,rely = 0.45)

        self.email_entry.place(anchor='n',relx = 0.5,rely = 0.6)

        self.add_btn.place(anchor='n',relx = 0.5,rely = 0.75)

        self.message.place(anchor='n',relx = 0.5,rely = 0.9)


    def reset(self):
        w1 = self.application_entry.get()
        self.application_entry.delete(0,(len(w1)))

        w2 = self.username_entry.get()
        self.username_entry.delete(0,(len(w2)))

        w3 = self.password_entry.get()
        self.password_entry.delete(0,(len(w3)))

        w4 = self.email_entry.get()
        self.email_entry.delete(0,(len(w4)))

    def reset2(self):
        self.message.configure(text='')

    
    def validate(self,app_list):
        self.message.configure(text='')
        app = self.application_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        validation = True
        if app_list is not None:
            if app in app_list :
                validation =  False
            elif app.isspace() or len(app)==0 :
                validation =  False
            elif len(username)==0 :
                validation =  False
            elif len(password)==0:
                validation =  False
        else:
            if app.isspace() or len(app)==0 :
                validation =  False
            elif len(username)==0 :
                validation =  False
            elif len(password)==0:
                validation =  False

        if validation == False:
            self.message.configure(text='Unable to add app')
        elif validation == True:
            self.message.configure(text='App added succesfully')

        return validation
