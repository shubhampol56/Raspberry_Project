from tkinter import *
from tkinter import ttk
from serial_data_fetch import *
from add_customer import *
from export_data import *
from import_ratechart import *
import datetime
import time
import tkinter.messagebox

''' IMPORTING SUCCESSFUL '''

''' MENU PAGE '''


class Menu():

    def __init__(self, menu):
        self.menu = menu

       # menu.overrideredirect(True)
       # menu.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        menu.geometry('425x225')

        self.menu.title('Menu')

        frame = LabelFrame(menu, text='MENU')
        frame.place(x=30, y=50)
        self.b1 = Button(frame, text = "Collection", width = 10, height = 5, command = self.Collection)
        self.b1.grid(row=0, column=1)#pack(side=TOP, expand=YES)

        self.b2 = Button(frame, text = "Export Data", width = 10, height = 5,command=self.exportdata)
        self.b2.grid(row=0, column=2)#pack(side=TOP, expand=YES)

        self.b3 = Button(frame, text = "Add Customer", width = 10, height = 5,command = self.addcust)
        self.b3.grid(row=0, column=3)#pack(side=TOP, expand=YES)

        self.b3 = Button(frame, text = "RateChart", width = 10, height = 5,command = self.importratechart)
        self.b3.grid(row=1, column=1)#pack(side=TOP, expand=YES)

        self.b3 = Button(frame, text = "Unused", width = 10, height = 5,command = self.addcust)
        self.b3.grid(row=1, column=2)#pack(side=TOP, expand=YES)

        self.b3 = Button(frame, text = "Unused", width = 10, height = 5,command = self.addcust)
        self.b3.grid(row=1, column=3)#pack(side=TOP, expand=YES)
        '''Logo and Title'''
    def Collection(self):
       # menu.destroy()
        root2 = Toplevel(self.menu)
        MainPage(root2)
       # newroot.mainloop()
    def addcust(self):
 #       root.destroy()
        #root = Tk()
        root4 = Toplevel(self.menu)
        add_cust(root4)
        root.mainloop()
    def exportdata(self):
 #       root.destroy()
        newroot = Tk()
        export_data(newroot)
        newroot.mainloop()
    def importratechart(self):
 #       root.destroy()
        root3 = Toplevel(self.menu)
        import_ratechart(root3)
    #    newroot.mainloop()
    
'''MAIN'''

if __name__ == '__main__':
    root = Tk()
    menu = Menu(root)
    root.mainloop()
    
