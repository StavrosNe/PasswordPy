import customtkinter as ctk
import os
from PIL import Image
from app.add import AddData
from app.query import QuerryData
from dbops import ApplicationsDb
from admin import ManageUser
from app.delete import DeleteApp
from customwidget import MasterKey

class Application(ctk.CTk):
    def __init__(self,username,password):
        """
        Class that inherits 
        from ctk.CTk class
        """
        super().__init__()

        # appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color = '#0D0D0D')

        # title
        self.title('Password Manager')

        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # database
        db_filepath = os.path.join(project_directory,"databases","applications.db")
        self.database = str(db_filepath)

        # images
        trash_filepath = os.path.join(project_directory, "assets","trash.png")
        trash_img = Image.open(trash_filepath)
        trash = ctk.CTkImage(trash_img,size=(30, 30))

        users_filepath = os.path.join(project_directory, "assets","user.png")
        users_img = Image.open(users_filepath)
        user = ctk.CTkImage(users_img,size=(30, 30))

        add_filepath = os.path.join(project_directory, "assets","plus.png")
        add_img = Image.open(add_filepath)
        add = ctk.CTkImage(add_img,size=(30, 30))

        query_filepath = os.path.join(project_directory, "assets","loupe.png")
        query_img = Image.open(query_filepath)
        query = ctk.CTkImage(query_img,size=(30, 30))


        key_filepath = os.path.join(project_directory, "assets","key.png")
        key_img = Image.open(key_filepath)
        key = ctk.CTkImage(key_img,size=(30, 30))

        self.username = username
        self.password = password
        self.key = 'key'

        greetmsg = 'user : '+self.username

        self.frame = ctk.CTkFrame(master = self,
                                  width=1180,height=720,
                                  fg_color ="#0D0D0D",
                                  corner_radius=0)
        
        self.frameutils = ctk.CTkFrame(master = self,
                                  width=100,height=720,
                                  corner_radius=0)

        self.greetlabel = ctk.CTkLabel(master=self.frame ,
                                        text = greetmsg, 
                                        font=("Helvetica",20,'bold'))
        
        self.keyframe = MasterKey(master = self.frame,width = 500 , 
                                  height = 60 , entrywidth = 200)
        
        self.delete_app_btn = ctk.CTkButton(master=self.frameutils,text='',
                                            width=60,height=60,
                                            corner_radius=60,
                                            command=self.delete_app,
                                            image=trash,
                                            fg_color='transparent',
                                            hover_color='#505050',
                                            state='disabled')
                                            
        
        self.manage_btn = ctk.CTkButton(master=self.frameutils,text='',
                                    width=60,height=60,
                                    corner_radius=60,
                                    command=self.manage_account,
                                    image=user,
                                    fg_color='transparent',
                                    hover_color='#505050')
        
        self.add_btn = ctk.CTkButton(master=self.frameutils,text='',
                                    width=60,height=60,
                                    corner_radius=60,
                                    command=self.show_add_frame,
                                    image=add,
                                    fg_color='transparent',
                                    hover_color='#505050',
                                    state='disabled')
        
        self.query_btn = ctk.CTkButton(master=self.frameutils,text='',
                                    width=60,height=60,
                                    corner_radius=60,
                                    command=self.show_query_frame,
                                    image=query,
                                    fg_color='transparent',
                                    hover_color='#505050',
                                    state='disabled')
        
        self.key_btn = ctk.CTkButton(master=self.frameutils,text='',
                                    width=60,height=60,
                                    corner_radius=60,
                                    command=self.show_key,
                                    image=key,
                                    fg_color='transparent',
                                    hover_color='#505050',
                                    state='disabled')
                                    
        self.addframe = AddData(master=self.frame)
        self.queryframe = QuerryData(master=self.frame)
        
        self.addframe.add_btn.configure(command = self.add_app)
        self.segbutton = self.queryframe.segbutton
        self.segbutton.button1.configure(command = self.query_app)
        self.segbutton.button2.configure(command = self.show_names)
        
        self.greetlabel.place(anchor = 'nw' , relx = 0.012 , rely = 0.02)

        self.frame.place(relx = 1 , rely = 0 , anchor = 'ne')

        self.keyframe.place(anchor = 's' , relx = 0.5 , rely = 0.1)

        self.frameutils.place(relx = 0 , rely = 0 , anchor = 'nw')

        self.manage_btn.place(relx = 0.5 , rely = 0.005 , anchor = 'n')

        self.add_btn.place(relx=0.5 ,rely = 0.14 ,anchor='n')

        self.query_btn.place(relx=0.5 ,rely = 0.28 ,anchor='n')

        self.key_btn.place(relx=0.5 ,rely = 0.42 ,anchor='n')

        self.delete_app_btn.place(relx=0.5 ,rely = 0.56 ,anchor='n')

        self.start1 = 0

        self.start2 = 0
    
        self.keyframe.key_btn.configure(command=self.key_command)

    def key_command(self):
        def insert_key():
            entered = self.keyframe.key_entry.get()

            valid_key = self.keyframe.strong_key(entered)

            if valid_key  == True:
                self.key_btn.configure(state='normal')
                self.add_btn.configure(state='normal')
                self.query_btn.configure(state='normal')
                self.delete_app_btn.configure(state='normal')
                self.key = entered
                return True
            elif valid_key  == False:
                return False
        def hide_key():
            self.start2 = 0
            y = self.start1
            if y <80:
                y += 1
                self.keyframe.place(anchor='s', relx=0.5, rely=(0.1 - 0.00125 * y))
                self.start1 = y
                self.after(10,hide_key)
                
        valid_key = insert_key()
        if valid_key == True:
            hide_key()
            self.db = ApplicationsDb(database=self.database,
                                     username=self.username,key=self.key)
        else:
            pass

    def show_key(self):
        self.start1 = 0
        y = self.start2
        if y <80:
            y += 1
            self.keyframe.place(anchor='s', relx=0.5, rely=(0 + 0.00125 * y))
            self.start2 = y
            self.after(10,self.show_key)
        
    def show_query_frame(self):
        self.queryframe.place(relx=0.5 ,rely = 0.15 , anchor = 'n')
        try:
            self.addframe.place_forget()
        except:
            pass
        try:
            self.hide_names2()
        except:
            pass
        self.addframe.reset2()

    def show_add_frame(self):
        self.addframe.place(relx=0.5 ,rely = 0.15 , anchor = 'n')
        try:
            self.queryframe.place_forget()
        except:
            pass
        try:
            self.hide_names2()
        except:
            pass
        self.queryframe.reset2()

    def show_names(self):
        self.update_appbox() # modify textbox with text_box method
        self.textbox.place(relx=0.55 , rely = 0.15 , anchor='nw')
        self.queryframe.place(relx=0.5 ,rely = 0.15 , anchor = 'ne')
        self.segbutton.button2.configure(text='Hide Apps',
                                       command = self.hide_names)

    def hide_names(self):
        self.textbox.place_forget()
        self.queryframe.place(relx=0.5 ,rely = 0.15 , anchor = 'n')
        self.segbutton.button2.configure(text='Show Apps',
                                       command = self.show_names)
    
    def hide_names2(self):
        self.textbox.place_forget()
        self.segbutton.button2.configure(text='Show Apps',
                                       command = self.show_names)

    def update_appbox(self):
        self.textbox = ctk.CTkTextbox(master=self.frame, width=280,
                                    height=80,
                                    corner_radius=20,fg_color="gray8",
                                    font =("Roboto",18),
                                    #border_color = '#251351',
                                    border_width = 3,wrap = None)

        def textbox_height(decrypted_app_names):
            length = len(decrypted_app_names)
            if length<=3:
                height = 80
            elif length>3 and length<=28:
                height=70+length*15
            elif length>28:
                height=500
    
            return height

        decrypted_app_names = self.db.fetch_appnames()
        if decrypted_app_names is not None:
            self.textbox.configure(state='normal')  
            height = textbox_height(decrypted_app_names)
            self.textbox.configure(height=height)
            for app in decrypted_app_names:
                self.textbox.insert("0.0", f'{app}\n')
            self.textbox.configure(state='disabled')  
        else:
            pass
    
    def add_app(self):
        application = self.addframe.application_entry.get()
        username = self.addframe.username_entry.get()
        password = self.addframe.password_entry.get()
        email = self.addframe.email_entry.get()

        decrypted_app_names = self.db.fetch_appnames()
        
        try:
            validate = self.addframe.validate(decrypted_app_names)
            assert validate==True
            self.db.add_app(application,username,
                            password,email)
            self.addframe.reset()
        
        except Exception as error:
            print(error)

    def query_app(self):
        application = self.queryframe.application_entry.get()
        decrypted_app_names = self.db.fetch_appnames()

        try:           
            validate = self.queryframe.validate(decrypted_app_names)
            assert validate==True
            self.queryframe.reset()
            decrypted_data = self.db.fetch_app(application)

            self.queryframe.username_entry.insert(0,decrypted_data[0])
            self.queryframe.password_entry.insert(0,decrypted_data[1])
            self.queryframe.email_entry.insert(0,decrypted_data[2])

        except Exception as error:
            print(error)

    def delete_app(self):
        dialog = ctk.CTkInputDialog(text="Enter app to delete:", title="Delete")
        app = dialog.get_input()  # waits for input
        try:
            assert app is not None
            self.db.delete_app(app)

        except Exception as error:
            print(error)


    def manage_account(self):
        def main():
            app = ManageUser(password = self.password, 
                             username = self.username)
            #getting screen width and height of display
            ws= app.winfo_screenwidth()
            hs= app.winfo_screenheight()
            
            # width and height of app
            w = 500
            h = 500
            
            # coordiantes on where the app opens
            x = (ws/2) - (w/2)
            y  = (hs/2) - (h/2)
            
            #setting tkinter window size
            app.geometry('%dx%d+%d+%d' % (w,h,x,y))
            app.mainloop()
        main()

        
