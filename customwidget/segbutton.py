import customtkinter as ctk


class SegButton(ctk.CTkFrame):
    def __init__(self, ratio1: int , ratio2: int , text1:str,text2:str,
                 master: any, width: int = 300, 
                 height: int=40, corner_radius: int=10,
                 **kwargs):
        
        super().__init__(master,width,height,
                         corner_radius,
                         **kwargs)

        self.configure(fg_color = 'transparent')
        #self.configure(border_color = '#251351')
        #self.configure(border_width = height/20)

        self.border = height/6
        
        self.btn_width1 = (ratio1*width)-2*self.border
        self.btn_width2 = (ratio2*width)-2*self.border

        self.button1 = ctk.CTkButton(master=self,width=self.btn_width1,
                                    height=height,font=("Roboto",18),
                                    text=text1,corner_radius=10)
        
        self.button2 = ctk.CTkButton(master=self,width=self.btn_width2,
                                    height=height,font=("Roboto",18),
                                    text=text2,corner_radius=10)
        
    
        self.button1.place(relx=0 ,rely=0.5,anchor='w')

        self.button2.place(relx=1 ,rely=0.5,anchor='e')