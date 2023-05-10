import customtkinter as ctk
from dbops import ChangeEncryption
from dbops import ChangePassword


class DeleteApp(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(width=400, 
                         height=200,
                         )

        self.application = None
        self.title('Delete application')

        self.attributes("-topmost", True)
        self.resizable(False, False) 
        self.protocol("WM_DELETE_WINDOW", self.cancel_command)
        self.grab_set()

        self.entry = ctk.CTkEntry(master = self,
                            width=250,height=40,corner_radius=10,
                            placeholder_text ='Enter application to delete',
                            font = ('Roboto',18))
        
        #self.after(150, lambda: self.entry.focus())
        
        self.ok_btn = ctk.CTkButton(master = self,width = 120 , height =40 ,
                                text='ok',corner_radius=10,
                                command = self.ok_command,
                                font = ('Roboto',18))
        
        self.cancel_btn = ctk.CTkButton(master = self,width = 120 , height =40 ,
                                text='cancel',corner_radius=10,
                                command = self.cancel_command,
                                font = ('Roboto',18))
        
        self.entry.bind("<Return>", self.ok_command)

        offset = 0.1875
        
        self.entry.place(relx = 0.5 , rely = 0.15 , anchor = 'n')
        self.ok_btn.place(relx = offset , rely = 0.6 , anchor = 'w')
        self.cancel_btn.place(relx = 1-offset , rely = 0.6 , anchor = 'e')

    def ok_command(self):
        self.application = self.entry.get()
        self.grab_release()
        self.destroy()

    def cancel_command(self):
        self.grab_release()
        self.destroy()

    def get_app(self):
        return self.application

