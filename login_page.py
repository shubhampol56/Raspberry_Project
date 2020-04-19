
from tkinter import *
from tkinter import ttk
#from serial_data_fetch import *
from Menu_page import *

class xyz:

    user = ' '
    passw =' '

    def __init__(self,root):

        self.root = root
        self.root.title('LOGIN SCREEN')

        Label(text = ' Username ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=3,columnspan=10)

        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=3,columnspan=10)

        ttk.Button(text='LOGIN',command=self.login_user).place(x = 80, y = 130)


    def login_user(self):

        '''Check username and password entered are correct'''
        if self.username.get() == self.user and self.password.get() == self.passw:

            # Do the work done by the main of DBMSproject.py

            #Destroy the current window
            root.destroy()
            
            #Open new window
            newroot = Tk()
            application = Menu(newroot)
            newroot.mainloop()
            
        else:
            
            '''Prompt user that either id or password is wrong'''
            self.message = Label(text = 'Username or Password incorrect. Try again!',fg = 'Red')
            self.message.place(x = 50, y = 170)

if __name__ == '__main__':

    root = Tk()
  #  root.attributes("-fullscreen",True)
  #  root.overrideredirect(True)
  #  root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.geometry('425x225')
    xyz(root)

    root.mainloop()
