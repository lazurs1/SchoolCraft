######################################################################
#                   CIS 129                                          #  
#            M3: Random Number Guess                                 #
#              PROF: James Boron                                     #
#              Student: Thomas Burns                                 #
#                   14 Jan 2024                                       #
#                   V 1.0                                            #
#                   NOTES:                                           #
#   Should have __main__ entry point so code can be resued as module #
#                no Dataset specified                                #
#                no input for data specified                         #
#           More cool code check the blog for projects               #
#       https://elect144.com/index.php/category/blog/                #
#       Access to my GIT email- lazurs1@gmail.com                    #
######################################################################
'''

Assignment Content

Prior to submitting this assignment, make sure you have completed the associated Learning Activities and Practices Exercises in the module.
In this module you learned about structured programs. You learned about the elements and techniques required to develop a structured program and how structure increases the organization of your code.
Draw a flowchart and pseudocode that describes the process of guessing a number between 1 and 100.
After each guess, the player is told that the guess is too high or too low.
The process continues until the player guesses the correct number.
Make a working version of this program in Python.
Complete the flowchart and pseudocode using draw.io. Include your pseudocode by adding a “square shape” next to your flowchart and populating it with your pseudocode for the program. 
Export your work in PDF format and attach it in the assignment submission area by the listed due date.
Complete the Python code using IDLE. Save your .py file and attach it in the assignment submission area by the listed due date. 
This assignment is worth 20 points and will be evaluated using the CIS 129 Assignment Rubric.
'''
#import random number module to create random number when called?
import random

#Set Variables
#Get a random INT betwenn 0-100 (inclusive)
randomNumber= random.randint(0, 100)
#Set variable to bool FALSE Initial state
correctNumber=False
dataInputGood=False

#Get user input
def getInputData():
    return input("Please input a number between 0 and 100 and press enter: ")

#Try Except on converting input string to INT
def inputCheck(incomingData):
    #Check if number by trying to convert to interger
    try:
        convertedToInt=int(incomingData)
        dataInputGood=True
        return convertedToInt
#If the convert blows up:
    except: 
        print("Error- Please enter a Number or X to eXit")
        dataInputGood=False
        return 


#Function to check on value/match
def calucateIfHighLowOrCorrect(inCalcData):
    #input less than random numer
    if inCalcData < randomNumber:
        print (f"Your number {inCalcData} was lower than the random number\n")
        return False
    #Input Greater than random number
    elif inCalcData > randomNumber:
        print (f"Your number {inCalcData} was Greater than the random number\n")
        return False
    #if entered number matches random number tell user they are right and set return value to TRUE
    else:
        print (f"Your Number {inCalcData} was right")
        return True 


#Initial Information for user
print ("Welcome to the number gestting program!\n")
print("Type X to eXit") #Check value to exit- no infinante loop

#keep checking if bool correctNumber is True then exit or if X is entered exit
while correctNumber != True:
    inputData=getInputData()
    #See if X or x is pressed- if so break out of while loop
    if inputData == "x" or inputData == "X":
        print("Exiting by request")
        break
    #if value returned as TRUE 
    correctNumber=calucateIfHighLowOrCorrect(inputCheck(inputData))
#Say Thank you for playing
print("Thank you for playing")
quit()
