from z_test import *
from chi_sq import *


print('Hi, Which of the following would you like to do?')

print('''
1. Pre - Test Evaluation
2. Test Evaluation
Other tests will be added soon.
''')



t = input("Enter your Choice : ")


if t=='1':
        print("We'll we working on the pre - test Evaluation today")
        print()
        print('Hi, Which of the following tests would you like to do?')
        print('''
        1. Chi Square Test
        2. Z- Test
        Other tests will be added soon.
        ''')
        
        g = input("Enter your Choice : ")
        print('You selected choice ' + g)
        
        if g=='1':
            print("Please enter the values")
            chi_sq2()
        
        elif g=='2':
            print("We'll we working on the z-test today")
            print()
            print("A Z-test is a type of hypothesis test. Hypothesis testing is a way for you to figure out if results from a test are valid or repeatable.")
            print()
            print('The result for the hypothesis testing is as given below')
            print()
            
            z_t2()
            
			
			
            
elif t=='2':
        print("We'll we working on an ongoing test evaluation today")
        print()
        print('Which of the following tests would you like to do?')
        print('''
        1. Chi Square Test
        2. Z- Test
        Other tests will be added soon.
        ''')
        
        h = input("Enter your Choice : ")
        print('You selected choice ' + g)

        if h=='1':
            chi_sq()
            
        elif h=='2':
            print("We'll we working on the z-test today")
            print()
            print("A Z-test is a type of hypothesis test. Hypothesis testing is a way for you to figure out if results from a test are valid or repeatable.")
            print()
            print('The result for the hypothesis testing is as given below')
        
            z_t()





