# import module as md
try:
    import Tkinter as tk
except:
    import tkinter as tk

import tkinter.messagebox as tm

import argparse
import csv
# from tabulate import tabulate
from tkinter.filedialog import askopenfilename
from tkinter import *
import pandas as pd 
import numpy    

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


def chi_sq2(visit,conv,visit_ratio,visit_ratio1,user_value):
    
        

    n_d     = 7
    uplift = [5,10,user_value]
    visit= int(visit)
    conv = int(conv)
    visit_ratio1 = int(visit_ratio1)
    visit_ratio = int(visit_ratio)
    uplift = int(uplift)

        
    for i in uplift:
            
        a_visit=visit*visit_ratio1/100
        a_conv=conv*visit_ratio1/100
            
        a_conv_rate = a_conv/a_visit
            
        b_visit = visit*visit_ratio/100
        b_conv = conv*visit_ratio/100
        b_conv_rate = a_conv_rate*(1+(i/100))
        b_conv = b_visit*b_conv_rate
            
        drops_a = a_visit-a_conv
        drops_b = b_visit-b_conv

        a_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*a_visit
        b_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*b_visit

        a_dps   = a_visit-a_comvc
        b_dps   = b_visit-b_comvc




        B = np.array([a_comvc, b_comvc, a_dps,b_dps])
        A = np.array([a_conv, b_conv, drops_a,drops_b])

            #Chi sq Distance

        D = np.sum(np.square(B-A)/B)

        pval = [chi2.sf(D, df=1)]
        pval = pd.DataFrame(pval)*100
        pval.to_csv("pval.csv")

        ndt = ((n_d*95)/(100-round(p_val,2)))-n_d
            #Plot p-value

        d = np.arange(0, 5, 0.1)
        plt.plot(d, chi2.pdf(d, df=1))
        plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1))
        plt.savefig('plot.png')
            #Test & Control

        B = np.array([a_comvc, b_comvc, a_dps,b_dps])
        A = np.array([a_conv, b_conv, drops_a,drops_b])

            #Chi sq Distance

        D = np.sum(np.square(B-A)/B)

        pval = [chi2.sf(D, df=1)]
        pval = pd.DataFrame(pval)*100

        ndt = ((n_d*95)/(100-round(p_val,2)))-n_d

            # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.
        p_val = pval.iloc[0,0]
        p_val1 = p_val/100

        print("The P-value for "+str(i)+ "% uplift is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")

        if (100-round(p_val,2) < 95) and (ndt >= 0):
            print('More days to reach 95% confidence level: ' +str(round(ndt)))



        pval.to_excel("pval.xlsx")


        d = np.arange(0, 5, 0.1)
        plt.plot(d, chi2.pdf(d, df=1), color = "grey")
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1), label = [round(p_val),str(round(ndt))])

        plt.legend(loc='upper right')
        plt.title('The P-value and the number of days are given for each in the legend ')




        plt.savefig('plot.png')

        img = mpimg.imread('plot.png')  
    #         os.system('plot.png')

    
    
def chi_sq(a_visit,b_visit,a_conv,b_conv,n_d):

    
        
#     a_visit = int(input('Enter the number of visitors for test A    '))
#     b_visit = int(input('Enter the number of visitors for test B    '))
#     a_conv  = int(input('Enter the number of conversions for test A '))
#     b_conv  = int(input('Enter the number of conversions for test B '))
#     n_d     = int(input('Enter the number of days '))
    a_visit = int(a_visit)
    b_visit = int(b_visit)
    a_conv  = int(a_conv)
    b_conv  = int(b_conv)
    n_d     = int(n_d)
    
    drops_a = a_visit-a_conv
    drops_b = b_visit-b_conv
    a_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*a_visit
    b_comvc = ((a_conv+b_conv)/(a_visit+b_visit))*b_visit
    a_dps   = a_visit-a_comvc
    b_dps   = b_visit-b_comvc
    
    
    
    
    B = np.array([a_comvc, b_comvc, a_dps,b_dps])
    A = np.array([a_conv, b_conv, drops_a,drops_b])

    #Chi sq Distance

    D = np.sum(np.square(B-A)/B)

    pval = [chi2.sf(D, df=1)]
    pval = pd.DataFrame(pval)*100
    #pval.to_csv("pval.csv")

    #Plot p-value

    d = np.arange(0, 5, 0.1)
    plt.plot(d, chi2.pdf(d, df=1))
    plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1))
    plt.savefig('plot.png')
    #Test & Control


    
    #Chi sq Distance

    D = np.sum(np.square(B-A)/B)
    print("the Chi-sq Distance is "+str(round(D)))
    pval = [chi2.sf(D, df=1)]
    pval = pd.DataFrame(pval)*100
    p_val = pval.iloc[0,0]
    p_val1 = p_val/100
    ndt = ((n_d*95)/(100-round(p_val,2)))-n_d
    
    # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.
    
    

    print("The p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
    print('The Confidence level is '+"\033[1m" +str(100-round(p_val,2))+ "%" + "\033[0m")
    if (100-round(p_val,2) < 95) and (ndt >= 0):
        print('More days to reach 95% confidence level: ' +str(round(ndt)))
    else:
        print('Test has already reached 95% confidence level')

    

    #Plot p-value

    
    d = np.arange(0, 5, 0.1)
    plt.plot(d, chi2.pdf(d, df=1), color = "grey")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1), color = 'blue', label = 'p_val', alpha = 0.4)
    plt.fill_between(d[d<=D], chi2.pdf(d[d<=D], df=1), color = 'blue', label = 'confidence', alpha = 0.1)
    plt.legend(loc='right')

    plt.title('The p-value is '+ str(round(p_val/100,2)))
    if  (100-round(p_val,2) < 95) and (ndt >= 0):
        plt.suptitle('Number of days to reach 95% condfidence level: ' + str(round(ndt)) + '\n'+ '\n' + '\n'+ 'The present Confidence level is ' +str(100-round(p_val,2))+ "%")
    else :
        plt.suptitle('The present Confidence is ' +str(100-round(p_val,2))+ "%" +' The test has already reached 95% confidence level ')
        
    
    
    plt.savefig('plot.png')
    
    img = mpimg.imread('plot.png') 
    
    os.system('plot.png')
    
    
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
        tk.Label(self, text="Significance tool", font=('Helvetica', 25, "bold")).grid(row=1,column = 1,ipadx ="10",pady="30")
        tk.Label(self, text="Which evaluation would you like to do?", font=('Helvetica', 10, "bold")).grid(row=2,column = 1,ipadx ="10",pady="10")
        tk.Button(self, text="Test for conversions",
                  command=lambda: master.switch_frame(PageOne)).grid(row=4,column = 1,ipadx ="10",pady="10")
        tk.Button(self, text="Test for a time based evaluation",
                  command=lambda: master.switch_frame(PageTwo)).grid(row=5,column = 1,ipadx ="10",pady="10")
        

#         Label(master, text='Which of the following would you like to do? ')
def getExcel ():
        global df

        import_file_path = filedialog.askopenfilename()
        df = pd.read_excel (import_file_path)
 


class PageOne(tk.Frame):
    global dateCol_var,daysNum_var
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Evaluation for Conversions", font=('Helvetica', 15, "bold")).grid(row=1,column = 1,columnspan= 2,ipadx ="10",pady="10")
        v = tk.IntVar()
        tk.Radiobutton(self, text='Pre-Test Evlauaiton', variable=v,value =1 ).grid(row=2,column = 0,columnspan = 2,ipadx ="10",pady="10")
        tk.Radiobutton(self, text='Test Evaluation', variable=v,value=2).grid(row=2,column = 2,columnspan=2,ipadx ="10",pady="10")
        

        tk.Label(self, text="Page traffic", font=('Helvetica', 10, "bold")).grid(row=4,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="Page orders", font=('Helvetica', 10, "bold")).grid(row=5,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="Test%", font=('Helvetica', 10, "bold")).grid(row=6,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="Control%", font=('Helvetica', 10, "bold")).grid(row=7,column = 0,ipadx ="10",pady="10")
        
        tk.Label(self, text="Expected Uplift", font=('Helvetica', 10, "bold")).grid(row=8,column = 0,ipadx ="10",pady="10")
        
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
        

    
        
        PT = Page_traffic.get()
        PO = Page_orders.get()
        TP = Test_p.get()
        CP = Control_p.get()
        UP = Uplift_p.get()
        
    
    
        tk.Label(self, text="A traffic", font=('Helvetica', 10, "bold")).grid(row=4,column = 2,ipadx ="10",pady="10")
        
        tk.Label(self, text="A orders", font=('Helvetica', 10, "bold")).grid(row=5,column = 2,ipadx ="10",pady="10")
        
        tk.Label(self, text="B Traffic", font=('Helvetica', 10, "bold")).grid(row=6,column = 2,ipadx ="10",pady="10")
        
        tk.Label(self, text="B orders", font=('Helvetica', 10, "bold")).grid(row=7,column = 2,ipadx ="10",pady="10")
        
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
        AT = A_traffic.get()
        AO = A_orders.get()
        BT = B_traffic.get()
        BO = B_orders.get()
        ND = n_days.get()
        

        
        
#         chi_sq(e1,e2,e4)
#         e6.grid(row=9, column=2,ipadx ="10",pady="10",padx="10")
#         e7.grid(row=10, column=2,ipadx ="10",pady="10",padx="10")
#         e8.grid(row=11, column=2,ipadx ="10",pady="10",padx="10")     
        
        def choice():
            if v==2 :
#                 print(v)
#                 A_traffic = A_traffic.get()
#                 A_orders = A_orders.get()
#                 B_traffic = B_traffic.get()
#                 B_orders = B_orders.get()
#                 n_days = n_days.get()
                        
                chi_sq(AT,BT,AO,BO,ND)
                
            else :
#                 Page_traffic = Page_traffic.get()
#                 Page_orders = Page_orders.get()
#                 Test_p = Test_p.get()
#                 Control_p = Control_p.get()
#                 Uplift_p = Uplift_p.get() 

                
                chi_sq2(PT,PO,TP,CP,UP)
#                 return 0
        
    
    
        tk.Button(self, text="Evaluate",
                  command=choice()
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
        tk.Label(self, text="Evaluation for Time (Test-evaluation)", font=('Helvetica', 15, "bold")).grid(row=1,column = 1,ipadx ="10",pady="10")
        
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
