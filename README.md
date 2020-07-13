# Significance-Testing
This is a module for working on A/B testing.




Pre-requisites

1. A python terminal or a python IDE should be installed on the machine. eg. Anaconda 5.9
2. Python version 3.4 or greater should be used.
3. The files chi_sq.py, z_test.py, main.py and Samplez.xlsx should be kept in the same folder.
4. A basic understanding of A/B testing would be needed.



Steps and Instructions:
1. Run the jupyter notebook application Installed on your machine and navigate to the folder that houses all the files for the application. Once there run the application.ipynb file.
2. The first block is to import all the files.
3. The second block will give you a choice between a pre-test and a an ongoing test evaluation. Enter the choice when prompted.
4. Following this two tests have been included in this application, the chi square test and the Z-test. Choose as per need.
5. You can enter the data while using the application or on a separate excel sheet provided named Samplez.xlsx
6. The data that is to be entered for chi square test is as follow:

     	The visitors for the Test A
     	The visitors for the Test B
     	The conversions for the Test A		
     	The conversions for the Test B
     
Note: In case of a pre-test evaluation, we will have the first two only along with a variable Uplift.
	
7. The data for the Z-test will be as follow:

      The daily traffic on A
      The daily time spent on A
      The daily orders on A
      The daily traffic on B
      The daily time spent on B
      The daily orders on B
Note: In case of a pre-test evaluation we will have the data for A only and another variable uplift, that can be modified as per user preference. Also, the data can be entered for a total of 7 days only.

7. The final output generated will be displayed on the application screen as output and also in a .png file in the same folder.
