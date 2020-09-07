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

def mean_fun(lst): 
    return sum(lst) / len(lst) 
    
def std_fun(test_list):
    return statistics.pstdev(test_list) 

def z_t():
    
    def foo(Ao,A):
        try:
            return (ai/bi for ai,bi in zip(Ao,A))
        except ZeroDivisionError:
            return 0
    
    
    print('Where would you like to enter the input data')
    print()
    print('''
    1. Excel - already entered
    2. Input here now 
    ''')
    choice = int(input('Enter Choice '))
    
    if choice ==1:
        print('Using the data in the excel')
        A = pd.read_excel("samplez.xlsx",sheet_name = "Sheet1")
        B = pd.read_excel("samplez.xlsx",sheet_name = "Sheet2")
        n_d     = int(input('Enter the number of days '))
        
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
            #pval
        n_d = len(A)
        ndt = ((n_d*1.645)/Z)-n_d
        pval = []
        pval.append(pvalue)
        pval = pd.DataFrame(pval)*100
        p_val = pval.iloc[0,0]
        p_val1 = p_val/100
        print("the p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
        print('the Confidence is '+"\033[1m" +str(100-round(p_val,2))+ "%" + "\033[0m")
        pval.to_excel("pval.xlsx")
       
    
        if 100-round(p_val,2) < 90 and ndt >= 1:
            print('The number of days the test will take to reach 90% confidence is ' +str(round(ndt)))


        #Plotting results: choose range by rounding off z score to upper number
        z = np.arange(-3, 3, 0.1)
        plt.plot(z, norm.pdf(z), color = 'grey')
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.fill_between(z[z<=Z], norm.pdf(z[z<=Z]), color = 'blue', label = 'Confidence', alpha = 0.05)
        plt.fill_between(z[z>Z], norm.pdf(z[z>Z]), color = 'blue', label = 'p_val', alpha = 0.4)
        plt.legend(loc='right')
        
        plt.title('The P-value is '+ str(round(p_val/100,2)) +'  ' +'and the present Confidence is ' + str(100-round(p_val,2)) + "%")
#         plt.suptitle('the Confidence is ' +str(100-round(p_val,2))+ "%")
        if 100-round(p_val,2) < 90 and ndt >= 1:
            plt.suptitle('The number of days to reach condfidence of 90% is ' +str(round(ndt)) )
        else :
            plt.suptitle('The test has already reached significance' )
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
        if len(A) != len(B) != len(At) != len(Ao) != len(Bt) != len(Bo) != 7:
            sys.exit('number of rows in variable do not match')
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
        pvalue = norm.sf(Z)

        #test days
        n_d = len(A)
        ndt = ((n_d*1.645)/Z)-n_d

        #pval
        pval = []
        pval.append(pvalue)
        pval = pd.DataFrame(pval)*100
        p_val = pval.iloc[0,0]
        p_val1 = p_val/100
        print("The p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
        print('The Confidence is '+"\033[1m" +str(100-round(p_val,2))+ "%" + "\033[0m")

        if 100-round(p_val,2) < 90 and ndt >= 1:
            print('The number of days the test will take to reach 90% confidence is ' +str(round(ndt)))

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
        plt.title('The present Confidence is ' + str(100-round(p_val,2)) + "%",loc = 'right')
#         plt.suptitle('the Confidence is ' +str(100-round(p_val,2))+ "%")
        if 100-round(p_val,2) < 90 and ndt >= 1:
            plt.suptitle('The number of days to reach condfidence of 90% is ' +str(round(ndt)) )
        else:
            plt.suptitle('The test has already reached significance')
        plt.savefig('plot.png')
        # Read Images 
        img = mpimg.imread('plot.png')  
        os.system('plot.png')

        workbook = xlsxwriter.Workbook('pval.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.insert_image('B2', 'plot.png')


def z_t2():
    print()

    temp = [1,2,3,4,5,6,7]


    print('The Z-test needs 7 days of data')
    def foo(Ao,A):
        try:
            return (ai/bi for ai,bi in zip(Ao,A))
        except ZeroDivisionError:
            return 0
    

    print('Where would you like to enter the input data')
    print()
    print('''
    1. Excel - already entered
    2. Input here now 
    ''')
    choice = int(input('Enter Choice '))
    
    if choice ==1:
        print('Using the data in the excel')
        A = pd.read_excel("samplez.xlsx",sheet_name = "Sheet1")
        B= A.iloc[:,0:4]
        B.columns = ['B', 'Bt', 'Bo', 'Bc']
#         print(A)
#         print(B)
        
        n_d     = int(input('Enter the number of days '))
       
    
        user_uplift = str(input('The default uplifts have been taken as 5%, 10% and 20%, Do you wish to input another one? (Yes/No)  '))
    
        if user_uplift == 'No':
            uplift = [5,10,20]
        else :
            user_value = float(input('Please enter the uplift value you want to test it for by replacing the 20% uplift '))
            uplift = [5,10,user_value]
#         print(A)
#         print(B)
        
        for j in uplift:
            B.iloc[:,1] = A.iloc[:,1]*(1+j/100)
            
            
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
                #pval
            n_d = len(A)
            ndt = ((n_d*1.645)/Z)-n_d
            pval = []
            pval.append(pvalue)
            pval = pd.DataFrame(pval)*100
            p_val = pval.iloc[0,0]
            p_val1 = p_val/100
            print("the p- value is "+"\033[1m"  + str(round(p_val1,2))+ "\033[0m")
            print('the Confidence is '+"\033[1m" +str(100-round(p_val,2))+ "%" + "\033[0m")
            pval.to_excel("pval.xlsx")


            if 100-round(p_val,2) < 90 and ndt >= 1:
                print('The number of days the test will take to reach 90% confidence is ' +str(round(ndt)))


            #Plotting results: choose range by rounding off z score to upper number
            z = np.arange(-3, 3, 0.1)
            plt.plot(z, norm.pdf(z), color = 'grey')
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.fill_between(z[z<=Z], norm.pdf(z[z<=Z]), color = 'blue', label = 'Confidence', alpha = 0.05)
            plt.fill_between(z[z>Z], norm.pdf(z[z>Z]), color = 'blue', label = 'p_val', alpha = 0.4)
            plt.legend(loc='right')

            plt.title('The P-value is '+ str(round(p_val/100,2)) +'  ' +'and the present Confidence is ' + str(100-round(p_val,2)) + "%")
    #         plt.suptitle('the Confidence is ' +str(100-round(p_val,2))+ "%")
            if 100-round(p_val,2) < 90 and ndt >= 1:
                plt.suptitle('The number of days to reach condfidence of 90% is ' +str(round(ndt)) )
            else :
                plt.suptitle('The test has already reached significance' )
            plt.savefig('plot.png')
            # Read Images 
            img = mpimg.imread('plot.png')  
            os.system('plot.png')

            workbook = xlsxwriter.Workbook('pval.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.insert_image('B2', 'plot.png')

    else :
        user_uplift = str(input('The default uplifts have been taken as 5%, 10% and 20%, Do you wish to input another one? (Yes/No)  '))
    
        if user_uplift == 'No':
            uplift = [5,10,20]
        else :
            user_value = float(input('Please enter the uplift value you want to test it for by replacing the 20% uplift '))
        
        uplift = [5,10,user_value]
        
        A = [int(A) for A in input("Enter daily traffic on A: ").split()] 
        #     print("Number of list A are: ", A)  
        At =[int(At) for At in input("Enter daily time spent on A: ").split()] 
        #     print("Number of list At are: ", At)  
        Ao =[int(Ao) for Ao in input("Enter daily orders on A: ").split()] 

        
        
        for k in uplift:
            B = A
            print(A)
            Bt = []
    #         Bt = time
    #         Bo = orders
    #         B = traffic
            for k in At:
                k = k*(1+k/100)
                Bt.append(round(k))
            #print (Bt)
            Bo = Ao

            Ac = foo(Ao,A)    
            Bc = foo(Bo,B)
            def mean_fun(lst): 
                return sum(lst) / len(lst) 

            def std_fun(test_list):
                return statistics.pstdev(test_list) 



            #mean avg. time of test observations
            m_A = mean_fun(At)
            m_B = mean_fun(Bt)


            #std dev of avg. time
            std_A = std_fun(At)
            std_B = std_fun(Bt)

            #count of test observations
            n_A = len(A)
            n_B = len(B)

            #Z score
            Z = (m_B - m_A)/np.sqrt((std_B**2)/n_B + (std_A**2)/n_A)
            pvalue = norm.sf(Z)
    #         print (Z)

            #test days
            n_d = len(A)
            ndt = ((n_d*1.645)/Z)-n_d
            if len(A) != len(At) != len(Ao) != len(temp):
                sys.exit('The number of rows in variables do not match')
            #pval
            pval = []
            pval.append(pvalue)
            pval = pd.DataFrame(pval)*100
            p_val = pval.iloc[0,0]
            p_val1 = p_val/100
            print("The P- value for "+ str(j) + "% uplift is " + str(round(p_val1,2)))
            print("The Confidence for "+ str(j) + "% uplift is " +str(100-round(p_val,2))+ "%" + "\033[0m")

            if 100-round(p_val,2) < 90 and ndt >= 1:
                print('The number of days the test will take to reach 90% confidence is ' +str(round(ndt)))
            pval.to_excel("pval.xlsx")
            #print(round(ndt)) 

            #Plotting results: choose range by rounding off z score to upper number
            z = np.arange(-3, 3, 0.1)
            plt.plot(z, norm.pdf(z), color = 'grey')
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['right'].set_visible(False)
            plt.fill_between(z[z<=Z], norm.pdf(z[z<=Z]), color = 'blue', label = 'Confidence', alpha = 0.05)
            plt.fill_between(z[z>Z], norm.pdf(z[z>Z]), color = 'blue', label = 'p_val', alpha = 0.4)
            plt.legend(loc='upper right')
            if 100-round(p_val,2) < 90 and ndt >= 1:                 
                plt.title('The P-value is '+ str(round(p_val/100,2))+'  and the number of days the test will take to reach 90% confidence is ' +str(round(ndt)))
            else:
                plt.title('The P-value is '+ str(round(p_val/100,2))+'  and the test has already reached significance')             
            plt.suptitle('The Confidence is ' +str(100-round(p_val,2))+ "%") 

            plt.savefig('plot.png')
            # Read Images 
            img = mpimg.imread('plot.png')  
            os.system('plot.png')

            workbook = xlsxwriter.Workbook('pval.xlsx')
            worksheet = workbook.add_worksheet()
            worksheet.insert_image('B2', 'plot.png')


NR_SBSC
YAGE
GENDER
MSINCEREGISTRNETWORK
AALLGROSSREVENUEM0
AALLGROSSREVENUEM1
AALLGROSSREVENUEM2
AALLGROSSREVENUEL2M
AALLGROSSREVENUEL3M
NALLDOUM0
NALLDOUM1
NALLDOUM2
NALLDOUL2M
NALLDOUL3M
ABONGAM0
ABONGAM1
ABONGAM2
NETUBLACKLISTM0
NETUBLACKLISTM1
NETUBLACKLISTM2
ADATACOSTM0
ADATACOSTM1
ADATACOSTM2
ADATACOSTL2M
ADATACOSTL3M
NDATAMBSM0
NDATAMBSM1
NDATAMBSM2
NDATADOUM0
NDATADOUM1
NDATADOUM2
NETURECHARGEM0
NETURECHARGEM1
NETURECHARGEM2
AETURECHARGEM0
AETURECHARGEM1
AETURECHARGEM2
GSMA_CLASS_FEATUREPHONE
GSMA_CLASS_HANDHELD
GSMA_CLASS_MOBILE_FEATURE
GSMA_CLASS_SMARTPHONE
NOKOAINTERNETM0
NOKOAINTERNETM1
NOKOAINTERNETM2
AOKOAINTERNETM0
AOKOAINTERNETM1
AOKOAINTERNETM2
MARKET_SEGMENT_DP
MARKET_SEGMENT_HUSTLER
MARKET_SEGMENT_MASS
MARKET_SEGMENT_UNCLASS
MARKET_SEGMENT_YOUTH
NMPESARECHARGEM0
NMPESARECHARGEM1
NMPESARECHARGEM2
AMPESARECHARGEM0
AMPESARECHARGEM1
AMPESARECHARGEM2
NMPESADOUM0
NMPESADOUM1
NMPESADOUM2
NMPESADOUL2M
NMPESADOUL3M
AMPESAGROSSM0
AMPESAGROSSM1
AMPESAGROSSM2
NOTHERRECHARGEM0
NOTHERRECHARGEM1
NOTHERRECHARGEM2
AOTHERRECHARGEM0
AOTHERRECHARGEM1
AOTHERRECHARGEM2
AOTHERGROSSREVENUEM0
AOTHERGROSSREVENUEM1
AOTHERGROSSREVENUEM2
AOTHERGROSSREVENUEL2M
AOTHERGROSSREVENUEL3M
NOTHERDOUM0
NOTHERDOUM1
NOTHERDOUM2
NOTHERDOUL2M
NOTHERDOUL3M
AGSMGROSSREVENUEM0
AGSMGROSSREVENUEM1
AGSMGROSSREVENUEM2
AGSMGROSSREVENUEL2M
AGSMGROSSREVENUEL3M
NGSMDOUM0
NGSMDOUM1
NGSMDOUM2
NGSMDOUL2M
NGSMDOUL3M
ACALLSALLREVENUEM0
ACALLSALLREVENUEM1
ACALLSALLREVENUEM2
ACALLSALLREVENUEL2M
ACALLSALLREVENUEL3M
NCALLSALLMINUTESM0
NCALLSALLMINUTESM1
NCALLSALLMINUTESM2
NCALLSALLMINUTESL2M
NCALLSALLMINUTESL3M
NCALLSDOUM0
NCALLSDOUM1
NCALLSDOUM2
NCALLSDOUL2M
NCALLSDOUL3M
ASMSREVENUEM0
ASMSREVENUEM1
ASMSREVENUEM2
ASMSREVENUEL2M
ASMSREVENUEL3M
NSMSQTYM0
NSMSQTYM1
NSMSQTYM2
NSMSQTYL2M
NSMSQTYL3M
NSMSDOUM0
NSMSDOUM1
NSMSDOUM2
NSMSDOUL2M
NSMSDOUL3M
NVOUCHERRECHARGEM0
NVOUCHERRECHARGEM1
NVOUCHERRECHARGEM2
AVOUCHERRECHARGEM0
AVOUCHERRECHARGEM1
AVOUCHERRECHARGEM2
AGAMBLINGMPESAM0
AGAMBLINGMPESAM1
AGAMBLINGMPESAM2
NGAMBLINGMPESAM0
NGAMBLINGMPESAM1
NGAMBLINGMPESAM2
NGAMBLINGMPESAL2M
NGAMBLINGMPESAL3M
AGAMBLINGMPESAL2M
AGAMBLINGMPESAL3M
AAVGGAMBLINGMPESAL2M
AAVGGAMBLINGMPESAL3M
AINP2PMPESAM0
AINP2PMPESAM1
AINP2PMPESAM2
AINP2PMPESAL2M
AINP2PMPESAL3M
AMAXINP2PMPESAL3M
AINMPESAM0
AINMPESAM1
AINMPESAM2
AINMPESAL2M
AINMPESAL3M
AMAXINMPESAL3M
AOUTMPESAM0
AOUTMPESAM1
AOUTMPESAM2
AOUTMPESAL2M
AOUTMPESAL3M
NOUTTRANSACMPESAM0
NOUTTRANSACMPESAM1
NOUTTRANSACMPESAM2
NOUTTRANSACMPESAL2M
NOUTTRANSACMPESAL3M
APAYBILLMPESAM0
APAYBILLMPESAM1
APAYBILLMPESAM2
AAVGPAYBILLMPESAL2M
AAVGPAYBILLMPESAL3M
APAYBILLMPESAL2M
APAYBILLMPESAL3M
LABEL

