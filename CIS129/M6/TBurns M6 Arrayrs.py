######################################################################
#                   CIS 129                                          #  
#            M7: Arrays                                              #
#              PROF: James Boron                                     #
#              Student: Thomas Burns                                 #
#                   2 Feb 2024                                       #
#                   V 1.0                                            #
######################################################################
'''
Assignment Content
Search the web to discover the ten most common user-selected passwords, and store them in an array. 
Draw a flowchart and pseudocode for a program that prompts a user for a password, 
and continue to prompt the user until the user has not chosen one of the common passwords.
123456
123456789
qwerty
password
12345
qwerty123
1q2w3e
12345678
111111
1234567890


Make a working version of this program in Python.
'''

PWList=("123456","123456789","qwerty","password","12345","qwerty123","1q2w3e","12345678","111111","1234567890")
print (PWList[1])
print("Welcome to the password checker")
passCheck=input("Please input your password for check: ")
while passCheck in PWList:
    passCheck=input("Your password is in the check list, please try a new one:")
print("Your password was not in the list")