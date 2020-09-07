
# coding: utf-8

# In[ ]:



import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import chi2
import os
import sys
import math
from scipy import stats
from operator import truediv
import statistics 
import xlsxwriter 

import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 



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
    
def chi_sq():

    print('How would you like to enter the input data?')
    print()
    print('''
    1. Excel - Enter in samplez sheet in folder
    2. Input here now (separated by space) 
    ''')
    choice = int(input('Enter Choice '))
    
    if choice ==1:
        print('Using the data in the excel')
        O = pd.read_excel("samplez.xlsx",sheet_name="Chi_Sheet")

        B = np.array([O.iloc[0]['A_converted'], O.iloc[1]['A_converted'], O.iloc[0]['A_drops'], O.iloc[1]['A_drops']])
        A = np.array([O.iloc[0]['converted'], O.iloc[1]['converted'], O.iloc[0]['drops'], O.iloc[1]['drops']])
        n_d     = int(input('Enter the number of days '))
         
    else:
        
        a_visit = int(input('Enter the number of visitors for test A    '))
        b_visit = int(input('Enter the number of visitors for test B    '))
        a_conv  = int(input('Enter the number of conversions for test A '))
        b_conv  = int(input('Enter the number of conversions for test B '))
        n_d     = int(input('Enter the number of days '))
    
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
    
    
    workbook = xlsxwriter.Workbook('pval.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.insert_image('B2', 'plot.png')

def chi_sq2():
   
    print('Please enter 7 days data for test pre-evaluation. How would you like to enter the input data?')
    print()
    print('''
    1. Excel - Enter in samplez sheet in folder
    2. Input here now (separated by space)
    ''')
    choice = int(input('Enter Choice '))
    
    if choice ==1:
        print('Using the data in the excel')
        O = pd.read_excel("samplez.xlsx",sheet_name="Chi_Sheet")

        A = np.array([O.iloc[0]['converted'], O.iloc[1]['converted'], O.iloc[0]['drops'], O.iloc[1]['drops']])
        n_d     = int(input('Enter 7 to confirm you have entered last seven days data '))
#         print(A)
        visit=A[0]+A[2]
        
        conv=A[0]
        
        user_uplift = str(input('The default uplifts have been taken as 5%, 10% and 20%, Do you wish to input expected uplift? (Yes/No)  '))

        if user_uplift == 'No':
             uplift = [5,10,20]
        else :
            user_value = float(input('Please enter the expected uplift value you want to test it for by replacing the 20% uplift '))
            uplift = [5,10,user_value]
        print("")    
        print("Please enter the test percentage between 1 and 100")
        visit_ratio = int(input('Please enter the value '))
        print("Please enter the control percentage between 1 and 100")
        visit_ratio1 = int(input('Please enter the value '))

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
            p_val = pval.iloc[0,0]
            p_val1 = p_val/100

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
            p_val = pval.iloc[0,0]
            p_val1 = p_val/100

            ndt = ((n_d*95)/(100-round(p_val,2)))-n_d

            # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.

            print("The P-value for "+str(i)+ "% uplift is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")

            if (100-round(p_val,2) < 95) and (ndt >= 0):
                print('More days to reach 95% confidence level: ' +str(round(ndt)))
            else:
                print('Test has already reached 95% confidence level')



    #         pval.to_excel("pval.xlsx")


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


    else:
        
        visit = int(input('Enter the number of visitors on test page/s    '))
        conv  = int(input('Enter the number of conversions from test page/s '))
        n_d     = int(input('Enter 7 to confirm you have entered last seven days data '))


        user_uplift = str(input('The default uplifts have been taken as 5%, 10% and 20%, Do you wish to input another one? (Yes/No)  '))

        if user_uplift == 'No':
             uplift = [5,10,20]
        else :
            user_value = float(input('Please enter the uplift value you want to test it for by replacing the 20% uplift '))
            uplift = [5,10,user_value]
        
        print("")    
        print("Please enter the test percentage between 1 and 100")
        visit_ratio = int(input('Please enter the value '))
        print("Please enter the control percentage between 1 and 100")
        visit_ratio1 = int(input('Please enter the value '))

        
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


def z_t():
    
    def foo(Ao,A):
        try:
            return (ai/bi for ai,bi in zip(Ao,A))
        except ZeroDivisionError:
            return 0
    
    
    
    print('How would you like to enter the input data')
    print()
    print('''
    1. Excel - Enter in samplez sheet in folder
    2. Input here now (separated by space)
    ''')
    choice = int(input('Enter Choice '))
    
    if choice ==1:
        print('Using the data in the excel')
        A = pd.read_excel("samplez.xlsx",sheet_name = "ZTestA")
        B = pd.read_excel("samplez.xlsx",sheet_name = "ZTestB")
        n_d     = int(input('Enter the number of days of input data '))
        
        #mean avg. time of test observations
        m_A = A.mean()[1]
        m_B = B.mean()[1]

        #std dev of avg. time
        std_A = A.std()[1]
        std_B = B.std()[1]
        n_A = len(A)
        n_B = len(B)
#         print(std_A)
#         print(std_B)
        #Z score
        Z = (m_B - m_A)/np.sqrt((std_B**2)/n_B + (std_A**2)/n_A)
        pvalue = norm.sf(Z)
        #n_d = len(A)
        
        pval = []
        pval.append(pvalue)
        pval = pd.DataFrame(pval)*100
        p_val = pval.iloc[0,0]
        p_val1 = p_val/100
        ndt = ((n_d*95)/(100-round(p_val,2)))-n_d
        conf = str(100-round(p_val,2))
        print("the p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
        print('the Confidence is '+"\033[1m" + left(conf,5) + "%" + "\033[0m")
        pval.to_excel("pval.xlsx")
       
    
        if (100-round(p_val,2) < 95) and (ndt >= 0):
            print('More days to reach 95% confidence level: ' +str(round(ndt)))
        else:
            print('The test has already reached 95% confidence level')


        #Plotting results: choose range by rounding off z score to upper number
        z = np.arange(-3, 3, 0.1)
        plt.plot(z, norm.pdf(z), color = 'grey')
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.fill_between(z[z<=Z], norm.pdf(z[z<=Z]), color = 'blue', label = 'Confidence', alpha = 0.05)
        plt.fill_between(z[z>Z], norm.pdf(z[z>Z]), color = 'blue', label = 'p_val', alpha = 0.4)
        plt.legend(loc='right')
        
        plt.title('The P-value is '+ str(round(p_val/100,2)) +'  ' +'and the present Confidence level is ' + left(conf,5) + "%")
#         plt.suptitle('the Confidence is ' +str(100-round(p_val,2))+ "%")
        if (100-round(p_val,2) < 95) and (ndt >= 0):
            plt.suptitle('More days to reach 95% condfidence level: ' +str(round(ndt)) )
        else :
            plt.suptitle('The test has already reached 95% confidence level' )
        plt.savefig('plot.png')
        # Read Images 
        img = mpimg.imread('plot.png')  
        os.system('plot.png')

        workbook = xlsxwriter.Workbook('pval.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.insert_image('B2', 'plot.png')

    else:
        A = [int(A) for A in input("Enter daily traffic on A: ").split()] 
        #     print("Number of list A are: ", A)  
        At =[int(At) for At in input("Enter daily time spent on A: ").split()] 
        #     print("Number of list At are: ", At)  
        Ao =[int(Ao) for Ao in input("Enter daily orders on A: ").split()] 
        #     print("Number of list Ao are: ", Ao)  
        B = [int(B) for B in input("Enter daily traffic on B: ").split()] 
        #     print("Number of list B are: ", B)  
        Bt =[int(Bt) for Bt in input("Enter daily time spent on B: ").split()] 
        #     print("Number of list Bt are: ", Bt)  
        Bo =[int(Bo) for Bo in input("Enter daily orders on B: ").split()] 
        #     print("Number of list Bo are: ", Bo) 
        n_d = int(input('Enter the number of days of input data '))
        if len(A) != len(B) != len(At) != len(Ao) != len(Bt) != len(Bo):
            sys.exit('number of rows in variables do not match')
        Ac = foo(Ao,A)    
        Bc = foo(Bo,B)
        m_A = mean_fun(At)
        m_B = mean_fun(Bt)
        std_A = std_fun(At)
        std_B = std_fun(Bt)

        n_A = len(A)
        n_B = len(B)

        #Z score
        Z = (m_B - m_A)/np.sqrt((std_B**2)/n_B + (std_A**2)/n_A)
        pvalue = 2*norm.sf(Z)

        
        #pval
        pval = []
        pval.append(pvalue)
        pval = pd.DataFrame(pval)*100
        p_val = pval.iloc[0,0]
        p_val1 = p_val/100
        ndt = ((n_d*95)/(100-round(p_val,2)))-n_d
        conf = str(100-round(p_val,2))
        print("The p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
        print('The Confidence is '+"\033[1m" + left(conf,5) + "%" + "\033[0m")

        if (100-round(p_val,2) < 95) and (ndt >= 0):
            print('More days to reach 95% confidence level: ' +str(round(ndt)))
        else:
            print('The test has already reached 95% confidence level')

        #pval.to_excel("pval.xlsx")


        #Plotting results: choose range by rounding off z score to upper number
        z = np.arange(-3, 3, 0.1)
        plt.plot(z, norm.pdf(z), color = 'grey')
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.fill_between(z[z<=Z], norm.pdf(z[z<=Z]), color = 'blue', label = 'Confidence', alpha = 0.05)
        plt.fill_between(z[z>Z], norm.pdf(z[z>Z]), color = 'blue', label = 'p_val', alpha = 0.4)
        plt.legend(loc='right')
        plt.title('The P-value is '+ str(round(p_val/100,2)) , loc='left')
        plt.title('The present Confidence is ' + left(conf,5) + "%",loc = 'right')
#         plt.suptitle('the Confidence is ' +str(100-round(p_val,2))+ "%")
        if (100-round(p_val,2) < 95) and (ndt >= 0):
            plt.suptitle('More days to reach 95% condfidence level: ' +str(round(ndt)) )
        else:
            plt.suptitle('The test has already reached 95% confidence')
        plt.savefig('plot.png')
        # Read Images 
        img = mpimg.imread('plot.png')  
        os.system('plot.png')

        workbook = xlsxwriter.Workbook('pval.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.insert_image('B2', 'plot.png')

