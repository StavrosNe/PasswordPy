import customtkinter as ctk
from login import LoginWin

def main():
    app = LoginWin()
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
    
if __name__ == '__main__':
    main()


