######################################################################
#                   CIS 129                                          #  
#            M4: Add two numbers and see if they equal a thrid       #
#              PROF: James Boron                                     #
#              Student: Thomas Burns                                 #
#                   4 Feb 2024                                       #
#                   V 1.0                                            #
######################################################################
'''
Assignment Content
Prior to submitting this assignment, make sure you have completed the associated Learning Activities and Practices Exercises in the module.
In this module you learned about making decisions. You learned about the syntax and rules used to develop programs containing decisions and how the logic can make your programs more robust.
Draw a flowchart and pseudocode that accepts three numbers from a user and displays a message if the sum of any two numbers equals the third. Make a working version of this program in Python.
Complete the flowchart and pseudocode using draw.io. Include your pseudocode by adding a “square shape” next to your flowchart and populating it with your pseudocode for the program. 
Export your work in PDF format and attach it in the assignment submission area by the listed due date.
Complete the Python code using IDLE. Save your .py file and attach it in the assignment submission area by the listed due date. 
This assignment is worth 20 points and will be evaluated using the CIS 129 Assignment Rubric.

'''
def checkinput(i1,i2,i3):
    if (i1 + i2 == i3):
        print(f"your numbers {i1} + {i2} sum up to {i3}")
        return()
    else:
        print(f"your numbers {i1} + {i2} sum up to {i1+i2} does not sum up to {i3}")
        return()


try: #error handle if non number entered or other error
    #Get Input
    input1= input("Please enter 1st number:")
    input2= input("Please enter 2nd number:")
    input3= input("Please enter 3rd number:")

    #check input
    intInput1=int(input1)
    intInput2=int(input2)
    intInput3=int(input3)
    checkinput(intInput1,intInput2,intInput3)
except: #error- not a number entered
    print("Please enter a number next time")

