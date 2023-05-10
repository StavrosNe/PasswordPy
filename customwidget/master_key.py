import customtkinter as ctk
import os
import re
from PIL import Image


class MasterKey(ctk.CTkFrame):
    def __init__(self,master,width,height,entrywidth):
        super().__init__(master=master,width=width,height=height,
                         corner_radius=20)

        project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        key_filepath = os.path.join(project_directory, "assets","key.png")
        key_img = Image.open(key_filepath)
        key = ctk.CTkImage(key_img,size=(30, 30))

        
        show_filepath = os.path.join(project_directory, "assets","show.png")
        show_img = Image.open(show_filepath)
        show = ctk.CTkImage(show_img,size=(30, 30))
        
        self.entrywidth = entrywidth

        self.key_entry = ctk.CTkEntry(master=self,width = self.entrywidth,
                                    height = 40,
                                    placeholder_text = 'Enter encryption key',
                                    font = ('Roboto',18),show = '*',
                                    corner_radius=10)
        
        self.key_btn = ctk.CTkButton(master=self,image = key,
                                     width=30,height=30,
                                     fg_color='transparent',
                                     hover_color='#505050',
                                     corner_radius=30,
                                     text = '')
        
        self.show_btn = ctk.CTkButton(master=self,image = show,
                                     width=30,height=30,
                                     fg_color='transparent',
                                     hover = False,
                                     corner_radius=30,
                                     text = '')
                                

        self.key_entry.place(rely = 0.5, relx=0.5 ,anchor = 'center')
        self.key_btn.place(rely = 0.5, relx=0.1 ,anchor = 'w')
        self.show_btn.place(rely = 0.5, relx=0.9 ,anchor = 'e')

        self.show_btn.bind('<ButtonPress-1>',self.show)
        self.show_btn.bind('<ButtonRelease-1>',self.hide)


    def show(self,event):
        self.key_entry.configure(show='')

    def hide(self,event):
        self.key_entry.configure(show='*') 
    

    def strong_key(self,password):
        letter_regex = r'[a-z]'
        capital_letter_regex = r'[A-Z]'
        number_regex = r'\d'
        space_regex = r'\s'
        special_char_regex = r'[!@#$%&.?+-]'
        condition1 = re.search(capital_letter_regex, password)
        condition2 = re.search(number_regex, password)
        condition3 = re.search(space_regex, password)
        condition4 = re.search(special_char_regex, password)
        condition5 = len(password) >= 12
        condition6 = re.search(letter_regex,password)
        if  (condition1 and condition2 and not condition3 
             and condition4 and condition5 and condition6):
            return True
        else:
            return False
        
    def get_key(self):
        return self.key_entry.get()