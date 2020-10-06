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
                    

    def getExcel ():
            global df

            import_file_path = filedialog.askopenfilename()
            df = pd.read_excel (import_file_path)


class PageOne(tk.Frame):
    global dateCol_var,daysNum_var,Page_traffic,Page_orders,Tese_p,Control_p,Uplift_p,A_traffic,A_orders,B_traffic,B_orders,n_days
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
     
        A_traffic = tk.Entry(self)
        A_orders = tk.Entry(self) 
        B_traffic = tk.Entry(self)
        B_orders = tk.Entry(self)
        n_days = tk.Entry(self) 
        

        A_traffic.grid(row=4, column=3,ipadx ="10",pady="10",padx="10") 
        A_orders.grid(row=5, column=3,ipadx ="10",pady="10",padx="10")
        B_traffic.grid(row=6, column=3,ipadx ="10",pady="10",padx="10")
        B_orders.grid(row=7, column=3,ipadx ="10",pady="10",padx="10")
        n_days.grid(row=8, column=3,ipadx ="10",pady="10",padx="10")
        
        
        
    
    
        tk.Button(self, text="Evaluate",
                  command=self.chi_sq
                 ).grid(row=10,column = 1,columnspan =2, ipadx ="10",pady="10")

        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=11,column = 1,columnspan =2, ipadx ="10",pady="10")
    
    def chi_sq(self):
    
        print("check1")

        
        
# problem is the code block below not working!!
# error recieved 

# AttributeError: 'PageOne' object has no attribute 'A_traffic'




#         a_visit = int(self.A_traffic.get())
#         b_visit = int(self.B_traffic.get())
#         a_conv  = int(self.A_orders.get())
#         b_conv  = int(self.B_orders.get())
#         n_d     = int(self.n_d.get())

#         drops_a = a_visit-a_conv
#         drops_b = b_visit-b_conv
#         a_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*a_visit
#         b_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*b_visit
#         a_dps   = a_visit-a_comvc
#         b_dps   = b_visit-b_comvc




#         B = np.array([a_comvc, b_comvc, a_dps,b_dps])
#         A = np.array([a_conv, b_conv, drops_a,drops_b])

#         #Chi sq Distance

#         D = np.sum(np.square(B-A)/B)

#         pval = [chi2.sf(D, df=1)]
#         pval = pd.DataFrame(pval)*100
#         #pval.to_csv("pval.csv")

#         #Plot p-value

#         d = np.arange(0, 5, 0.1)
#         plt.plot(d, chi2.pdf(d, df=1))
#         plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1))
#         plt.savefig('plot.png')
#         #Test & Control



#         #Chi sq Distance

#         D = np.sum(np.square(B-A)/B)
#         print("the Chi-sq Distance is "+str(round(D)))
#         pval = [chi2.sf(D, df=1)]
#         pval = pd.DataFrame(pval)*100
#         p_val = pval.iloc[0,0]
#         p_val1 = p_val/100
#         ndt = ((n_d*95)/(100-round(p_val,2)))-n_d

#         # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.



#         print("The p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
#         print('The Confidence level is '+"\033[1m" +str(100-round(p_val,2))+ "%" + "\033[0m")
#         if (100-round(p_val,2) < 95) and (ndt >= 0):
#             print('More days to reach 95% confidence level: ' +str(round(ndt)))
#         else:
#             print('Test has already reached 95% confidence level')



#         #Plot p-value


#         d = np.arange(0, 5, 0.1)
#         plt.plot(d, chi2.pdf(d, df=1), color = "grey")
#         plt.gca().spines['top'].set_visible(False)
#         plt.gca().spines['right'].set_visible(False)
#         plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1), color = 'blue', label = 'p_val', alpha = 0.4)
#         plt.fill_between(d[d<=D], chi2.pdf(d[d<=D], df=1), color = 'blue', label = 'confidence', alpha = 0.1)
#         plt.legend(loc='right')

#         plt.title('The p-value is '+ str(round(p_val/100,2)))
#         if  (100-round(p_val,2) < 95) and (ndt >= 0):
#             plt.suptitle('Number of days to reach 95% condfidence level: ' + str(round(ndt)) + '\n'+ '\n' + '\n'+ 'The present Confidence level is ' +str(100-round(p_val,2))+ "%")
#         else :
#             plt.suptitle('The present Confidence is ' +str(100-round(p_val,2))+ "%" +' The test has already reached 95% confidence level ')



#         plt.savefig('plot.png')

#         img = mpimg.imread('plot.png') 

#         os.system('plot.png')
        
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
            A = pd.read_excel(filename,sheet_name = "ZTestA")
            B = pd.read_excel(filename,sheet_name = "ZTestB")
            A.head()
        
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Test for time spent (Z- Test)", font=('Helvetica', 15, "bold")).grid(row=1,column = 1,ipadx ="10",pady="10")
        
        entry = Entry(self, width=40) 
        entry.grid(row=3,column=1)
        
        

        tk.Label(self, text="Please use the excel to enter the data for the Z-test", font=('Helvetica', 10)).grid(row=2,column = 1,ipadx ="10",pady="10")
        tk.Label(self, text="Excel file", font=('Helvetica', 10, "bold")).grid(row=3,column = 0,ipadx ="10",pady="10")
        
        browseButton_Excel = tk.Button(self, text='Browse File', width=25, bg = "light grey",   
                             fg = "black", command=button_browse_callback).grid(row=3, column=2,ipadx ="10",pady="10", padx="10")
        
        GoButton_Excel = tk.Button(self, text='Go', width=25, bg = "light grey",   
                             fg = "black", command=button_go_callback).grid(row=3, column=3,ipadx ="10",pady="10", padx="10")

        tk.Label(self, text="Number of days", font=('Helvetica', 10, "bold")).grid(row=4,column = 0,columnspan=1,ipadx ="10",pady="10")
        e1 = tk.Entry(self) 
        e1.grid(row=4, column=1,ipadx ="10",pady="10",padx="10") 
        
        
        tk.Button(self, text="Evaluate").grid(row=10,column = 1 ,ipadx ="10",pady="10")

        tk.Button(self, text="Go back to start page",
                      command=lambda: master.switch_frame(StartPage)).grid(row=11,column = 1,ipadx ="10",pady="10")

        
if __name__ == "__main__":
    app = SampleApp()
    
    app.mainloop()
