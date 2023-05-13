from login import LoginWin
import os

def main():
    # Get the current directory of the script
    dir_path = os.path.dirname(os.path.abspath(__file__))
    # Create the 'databases' folder in the current directory
    # if it doesnt exist already
    databases_dir = os.path.join(dir_path, 'databases')
    if not os.path.exists(databases_dir):
        os.mkdir(databases_dir)
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


