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
  
def test_func():
    print("Hello!")
    
def __main__():
    chi_sq()

def mean_fun(lst): 
    return sum(lst) / len(lst) 
    
def std_fun(test_list):
    return statistics.pstdev(test_list)     
    
def chi_sq():

    print('Where would you like to enter the input data')
    print()
    print('''
    1. Excel - already entered
    2. Input here now 
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
    
    ndt = ((n_d*2.706)/D)-n_d
    
    # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.
    p_val = pval.iloc[0,0]
    p_val1 = p_val/100

    print("The p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
    print('The Confidence is '+"\033[1m" +str(100-round(p_val,2))+ "%" + "\033[0m")
    
    if (100-round(p_val,2) < 90) and (ndt >= 1):
        print('The days to reach 90% conf is ' +str(round(ndt)))

    

    #Plot p-value

    
    d = np.arange(0, 5, 0.1)
    plt.plot(d, chi2.pdf(d, df=1), color = "grey")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.fill_between(d[d>D], chi2.pdf(d[d>D], df=1), color = 'blue', label = 'p_val', alpha = 0.4)
    plt.fill_between(d[d<=D], chi2.pdf(d[d<=D], df=1), color = 'blue', label = 'confidence', alpha = 0.1)
    plt.legend(loc='right')

    plt.title('The p-value is '+ str(round(p_val/100,2)))
    if  (100-round(p_val,2) < 90) and (ndt >= 1):
        plt.suptitle('The number of days to reach condfidence of 90% is ' + str(round(ndt)) + '\n'+ '\n' + '\n'+ 'The present Confidence is ' +str(100-round(p_val,2))+ "%")
    else :
        plt.suptitle('The present Confidence is ' +str(100-round(p_val,2))+ "%" +' The test has already reached significance ')
        
    
    
    plt.savefig('plot.png')
    
    img = mpimg.imread('plot.png') 
    
    os.system('plot.png')
    
    
    workbook = xlsxwriter.Workbook('pval.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.insert_image('B2', 'plot.png')

def chi_sq2():
   
    print('Where would you like to enter the input data')
    print()
    print('''
    1. Excel - already entered
    2. Input here now 
    ''')
    choice = int(input('Enter Choice '))
    
    if choice ==1:
        print('Using the data in the excel')
        O = pd.read_excel("samplez.xlsx",sheet_name="Chi_Sheet")

        A = np.array([O.iloc[0]['converted'], O.iloc[1]['converted'], O.iloc[0]['drops'], O.iloc[1]['drops']])
        n_d     = int(input('Enter the number of days '))
#         print(A)
        a_visit=A[0]+A[2] 
        a_conv=A[0]
        user_uplift = str(input('The default uplifts have been taken as 5%, 10% and 20%, Do you wish to input another one? (Yes/No)  '))

        if user_uplift == 'No':
             uplift = [5,10,20]
        else :
            user_value = float(input('Please enter the uplift value you want to test it for by replacing the 20% uplift '))
            uplift = [5,10,user_value]

        for i in uplift:
            a_conv_rate = a_conv/a_visit
            b_conv_rate = a_conv_rate*(1+(i/100))
            b_visit = a_visit
            b_conv  = b_conv_rate*b_visit
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

            ndt = ((n_d*2.706)/D)-n_d
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

            ndt = (n_d*2.706)/D

            # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.
            p_val = pval.iloc[0,0]
            p_val1 = p_val/100

            print("The P-value for "+str(i)+ "% uplift is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")

            if 100-round(p_val,2) < 90 and ndt >= 1:
                print('The number of days the test will take to reach 90% confidence is ' +str(round(ndt)))



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
        
        a_visit = int(input('Enter the number of visitors for test A    '))
        a_conv  = int(input('Enter the number of conversions for test A '))
        n_d     = int(input('Enter the number of days '))


        user_uplift = str(input('The default uplifts have been taken as 5%, 10% and 20%, Do you wish to input another one? (Yes/No)  '))

        if user_uplift == 'No':
             uplift = [5,10,20]
        else :
            user_value = float(input('Please enter the uplift value you want to test it for by replacing the 20% uplift '))
            uplift = [5,10,user_value]

        for i in uplift:
            a_conv_rate = a_conv/a_visit
            b_conv_rate = a_conv_rate*(1+(i/100))
            b_visit = a_visit
            b_conv  = b_conv_rate*b_visit
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

            ndt = ((n_d*2.706)/D)-n_d
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

            ndt = (n_d*2.706)/D

            # instead of pval in the datafrome print the value in the 4th quad as a percentage out of 100.
            p_val = pval.iloc[0,0]
            p_val1 = p_val/100

            print("The P-value for "+str(i)+ "% uplift is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")

            if 100-round(p_val,2) < 90 and ndt >= 1:
                print('The number of days the test will take to reach 90% confidence is ' +str(round(ndt)))



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
