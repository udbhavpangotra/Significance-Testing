# import module as md
try:
    import Tkinter as tk
except:
    import tkinter as tk

import tkinter.messagebox as tm
from tkinter.messagebox import showerror

import argparse
import csv
# from tabulate import tabulate
from tkinter.filedialog import askopenfilename
from tkinter import *
import pandas as pd 
import numpy    
from tkinter.simpledialog import askfloat


def left(s, amount):
    return s[:amount]

def test_func():
    print("Hello!")
    
def __main__():
    chi_sq()
    z_t()
def mean_fun(lst): 
    return sum(lst) / len(lst) 
    
def std_fun(test_list):
    return statistics.pstdev(test_list)     


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Significance Calculator", font=('Helvetica', 25, "bold")).grid(row=1,column = 1,ipadx ="10",pady="30", padx="20")
        tk.Label(self, text="What kind of a Test would you like to do?", font=('Helvetica', 10, "bold")).grid(row=2,column = 1,ipadx ="10",pady="20")
        tk.Button(self, text="Test for conversions (Chi Sq Test)",
                  command=lambda: master.switch_frame(PageOne)).grid(row=4,column = 1,ipadx ="10",pady="10")
        tk.Button(self, text="Test for time spent (Z- Test)",
                  command=lambda: master.switch_frame(PageTwo)).grid(row=5,column = 1,ipadx ="10",pady="10")
        tk.Button (self, text = "Exit").grid(row=6,column=1,pady="20")
                    

#         Label(master, text='Which of the following would you like to do? ')
def getExcel ():
        global df

        import_file_path = filedialog.askopenfilename()
        df = pd.read_excel (import_file_path)
 


class PageOne(tk.Frame):
    global dateCol_var,daysNum_var
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Test for Conversions (Chi Sq Test)", font=('Helvetica', 15, "bold")).grid(row=1,column = 1,columnspan= 2,ipadx ="10",pady="10")
        v = tk.IntVar()
        tk.Radiobutton(self, text='Pre-Test Evlauaiton', variable=v,value =1 ).grid(row=2,column = 0,columnspan = 2,ipadx ="10",pady="10")
        tk.Radiobutton(self, text='Test Evaluation', variable=v,value=2).grid(row=2,column = 2,columnspan=2,ipadx ="10",pady="10")
        

        tk.Label(self, text="Page traffic", font=('Helvetica', 10, "bold")).grid(row=4,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="Page Converted", font=('Helvetica', 10, "bold")).grid(row=5,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="Test%", font=('Helvetica', 10, "bold")).grid(row=6,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="Control%", font=('Helvetica', 10, "bold")).grid(row=7,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="Expected Uplift%", font=('Helvetica', 10, "bold")).grid(row=8,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="*Enter 7 day data only", font=('Helvetica', 10)).grid(row=9,column = 1,ipadx ="10",pady="10")
        
        Page_traffic = tk.Entry(self) 
        Page_orders = tk.Entry(self) 
        Test_p = tk.Entry(self)
        Control_p = tk.Entry(self)
        Uplift_p = tk.Entry(self) 
#         e6 = tk.Entry(self) 
#         e7 = tk.Entry(self)
#         e8 = tk.Entry(self)
        Page_traffic.grid(row=4, column=1,ipadx ="10",pady="10",padx="10") 
        Page_orders.grid(row=5, column=1,ipadx ="10",pady="10",padx="10")
        Test_p.grid(row=6, column=1,ipadx ="10",pady="10",padx="10")
        Control_p.grid(row=7, column=1,ipadx ="10",pady="10",padx="10")
        Uplift_p.grid(row=8, column=1,ipadx ="10",pady="10",padx="10") 
 
        
    
    
        tk.Label(self, text="A traffic", font=('Helvetica', 10, "bold")).grid(row=4,column = 2,ipadx ="10",pady="10")
        
        tk.Label(self, text="A converted", font=('Helvetica', 10, "bold")).grid(row=5,column = 2,ipadx ="10",pady="10")
        
        tk.Label(self, text="B Traffic", font=('Helvetica', 10, "bold")).grid(row=6,column = 2,ipadx ="10",pady="10")
        
        tk.Label(self, text="B converted", font=('Helvetica', 10, "bold")).grid(row=7,column = 2,ipadx ="10",pady="10")
        
        tk.Label(self, text="Number of days", font=('Helvetica', 10, "bold")).grid(row=8,column = 2,ipadx ="10",pady="10")
        
#         tk.Label(self, text="Enter 7 day data only", font=('Helvetica', 10)).grid(row=9,column = 1,ipadx ="10",pady="10")
        
        A_traffic = tk.Entry(self)
#         float(A_traffic.get())
        A_orders = tk.Entry(self) 
        B_traffic = tk.Entry(self)
        B_orders = tk.Entry(self)
        n_days = tk.Entry(self) 
        

        A_traffic.grid(row=4, column=3,ipadx ="10",pady="10",padx="10") 
        A_orders.grid(row=5, column=3,ipadx ="10",pady="10",padx="10")
        B_traffic.grid(row=6, column=3,ipadx ="10",pady="10",padx="10")
        B_orders.grid(row=7, column=3,ipadx ="10",pady="10",padx="10")
        n_days.grid(row=8, column=3,ipadx ="10",pady="10",padx="10")
        
        
        A_traffic = A_traffic.get()
        A_orders = A_orders.get()
        B_traffic = B_traffic.get()
        B_orders = B_orders.get()
        n_days = n_days.get()
        

    
        tk.Button(self, text="Evaluate",
#                   command=choice()
                 ).grid(row=10,column = 1,columnspan =2, ipadx ="10",pady="10")

        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=11,column = 1,columnspan =2, ipadx ="10",pady="10")

class PageTwo(tk.Frame):
    def __init__(self, master):
        
        def button_browse_callback():
            """ What to do when the Browse button is pressed """
            filename = askopenfilename()
            print(entry)
            entry.delete(0, END)
            entry.insert(0, filename)
        
        
        def button_go_callback():
            """ what to do when the "Go" button is pressed """
            input_file = entry.get()
            filename = input_file
#             df = import_csv_data(input_file)
            A = pd.read_excel(filename,sheet_name = "ZTestA")
            B = pd.read_excel(filename,sheet_name = "ZTestB")
            A.head()
        
        tk.Frame.__init__(self, master)
#         tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Test for time spent (Z- Test)", font=('Helvetica', 15, "bold")).grid(row=1,column = 1,ipadx ="10",pady="10")
        
        entry = Entry(self, width=40) #Entry widget is used to accept single-line text strings from a user.
        entry.grid(row=3,column=1)
        
        
#         entry.grid(row=4, column=3,ipadx ="10",pady="10",padx="10")
        tk.Label(self, text="Please use the excel to enter the data for the Z-test", font=('Helvetica', 10)).grid(row=2,column = 1,ipadx ="10",pady="10")
        tk.Label(self, text="Excel file", font=('Helvetica', 10, "bold")).grid(row=3,column = 0,ipadx ="10",pady="10")
        
        browseButton_Excel = tk.Button(self, text='Browse File', width=25, bg = "light grey",   
                             fg = "black", command=button_browse_callback).grid(row=3, column=2,ipadx ="10",pady="10", padx="10")
        
        GoButton_Excel = tk.Button(self, text='Go', width=25, bg = "light grey",   
                             fg = "black", command=button_go_callback).grid(row=3, column=3,ipadx ="10",pady="10", padx="10")
#         print(df)
        tk.Label(self, text="Number of days", font=('Helvetica', 10, "bold")).grid(row=4,column = 0,columnspan=1,ipadx ="10",pady="10")
        e1 = tk.Entry(self) 
        e1.grid(row=4, column=1,ipadx ="10",pady="10",padx="10") 
        
        
        tk.Button(self, text="Evaluate",
#                   add function
                 ).grid(row=10,column = 1 ,ipadx ="10",pady="10")

        tk.Button(self, text="Go back to start page",
                      command=lambda: master.switch_frame(StartPage)).grid(row=11,column = 1,ipadx ="10",pady="10")
if __name__ == "__main__":
    app = SampleApp()
    
    app.mainloop()
