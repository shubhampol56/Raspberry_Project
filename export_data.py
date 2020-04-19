from tkcalendar import DateEntry
from tkinter import *
import datetime
import time
import mysql.connector
import csv
import os
from ftplib import FTP

class export_data():

    def __init__(self, root):
        self.root = root

       # root.overrideredirect(True)
       # root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.geometry('425x225')

        self.root.title('Export Data')

        frame = LabelFrame(root, text='Export Data')
        frame.place(x=30, y=50)
        Label(frame, text='Date').grid(row=0,column=0)
        self.cal = DateEntry(frame, width=12,date_pattern='y-mm-dd', year=2020, month=4, day=4, 
        background='darkblue', foreground='white', borderwidth=2)
        self.cal.grid(row=0, column=1)
        Label(frame, text='Session').grid(row=2,column=0)
        Label(frame, text='Location').grid(row=3,column=0)
        self.n=StringVar()
        self.sessionchosen = ttk.Combobox(frame, width = 20, textvariable = self.n) 

        # Adding combobox drop down list 
        self.sessionchosen['values'] = ('Morning',  
                          'Evening')
        self.sessionchosen.current(0)
        self.sessionchosen.grid(row=2,column=1)

        self.l=StringVar()
        self.location = ttk.Combobox(frame, width = 20, textvariable = self.l) 

        # Adding combobox drop down list 
        self.location['values'] = ('FTP',  
                          'Flashdrive')
        self.location.current(0)
        self.location.grid(row=3,column=1)

        
        self.b3 = Button(frame, text='Export', command = self.Export)
        self.b3.grid(row=4,column=1)

    def Export(self):
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        os.chdir('/media/pi')
        stream = os.popen('ls')
        output=stream.read()
        output=str(output.replace("\n",""))
        name=output
        #print(name)

        
        
        print(name)
        os.chdir('..')
        os.chdir('..')

        os.chdir('..')
        os.chdir('/home/pi/tkinter code\'s_modified')
        print(os.getcwd())
        #print('Exporting '+self.cal.get()+' datetime '+datetime.date())
        session=""
        if(self.sessionchosen.get() == "Morning"):
            session="m"
        elif(self.sessionchosen.get() == "Evening"):
            session="e"
        if(self.location.get()=="Flashdrive"):
            print(session)
            mydb = mysql.connector.connect(host="localhost",database="SC001",user="root",passwd="pi")
            cursor = mydb.cursor()
            cursor_1=mydb.cursor()
            cursor_1.execute('select * from Cust_Info')
            result=cursor_1.fetchall()
            query='select * from Milk_Collection where Date=%s and Session=%s'
            
            parameters=(self.cal.get(),session)
            cursor.execute(query,parameters)
            path=str("/media/pi/"+name+"/Reports")
            #path=path.replace('\n',"")
            #print("path: ",path)
            try:
                if not os.path.exists(path):
                    os.makedirs(path)
                    print('directory made')
            except OSError:
                print("Error Creating Directory ",path)
            filename=str(path+"/"+self.cal.get()+"_"+self.sessionchosen.get()+".csv")
            
            with open(filename, 'w+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Cust_ID", "Name", "Milk Type","Fat","Snf","Added Water","Quantity","Rate","Session","Date","Time"])
                
                for i in cursor:
                    name=""
                    for j in result:
                        if i[0]==j[0]:
                            name=j[1]
                            break
                    date=i[10].now.strftime('%d-%m-%Y')
                    print("Date"+date)
                    writer.writerow([i[0], name, i[1],i[2],i[3],i[4],i[7],i[8],i[9],str(date),i[11]])

        else:
            print(session)
            mydb = mysql.connector.connect(host="localhost",database="SC001",user="root",passwd="pi")
            cursor = mydb.cursor()
            cursor_1=mydb.cursor()
            cursor_1.execute('select * from Cust_Info')
            result=cursor_1.fetchall()
            query='select * from Milk_Collection where Date=%s and Session=%s'
            
            parameters=(self.cal.get(),session)
            cursor.execute(query,parameters)
            filename=str(self.cal.get()+"_"+self.sessionchosen.get()+".csv")
            
            with open(filename, 'w+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Cust_ID", "Name", "Milk Type","Fat","Snf","Added Water","Quantity","Rate","Session","Date","Time"])
                
                for i in cursor:
                    name=""
                    for j in result:
                        if i[0]==j[0]:
                            name=j[1]
                            break
                    date=i[9].strftime('%d-%m-%Y')
                    print("Date"+date)
                    writer.writerow([i[0], name, i[1],i[2],i[3],i[4],i[6],i[7],i[8],str(date),i[10]])
            ftp=FTP('shubhamcomputech.co.in')
            ftp.login(user="demoftp@shubhamcomputech.co.in",passwd="demoftp@1000")
            ftp.cwd('/')
            ftp.storbinary('STOR '+filename,open(filename,'rb'))
            ftp.quit()
    
'''MAIN'''

if __name__ == '__main__':
    root = Tk()
   # root.attributes("-fullscreen",True)

    export_data(root)
    root.mainloop()
