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
import random


#Set Variables
randomNumber= random.randint(0, 100)
correctNumber=False
changeToInt=0

def getInputData():
    print("Please input a number between 0 and 100:")
    return input()

def checkInputData(inputData):
    print("inputdata = " + str(inputData))
    print(type(inputData))
   
    
        #check if number
    try:
        
        print("xxxzzzzzz")
        changeToInt=int(inputData)
        print("input data: " +  inputData + " converted data type: " + type(changeToInt))
        #test=int(inputData+1)
        #calucateIfHighLowOrCorrect(int(inputData))
    except:
        print("Error- Please enter X or a number between 0 and 100")
    return

    

def calucateIfHighLowOrCorrect(inCalcData):
    print(inCalcData)
    if inCalcData < randomNumber:
        print ("Your number was lower than the random number\n")
    elif inCalcData > randomNumber:
        print ("Your number was Greater than the random number\n")
    else:
        print ("Your Number was right\n")
        correctNumber = True
    return 

    


print ("Welcome to the number gestting program!\n")
print("Type X to eXit")

while correctNumber != True:
    inputData=getInputData()
    if inputData == "x" or inputData == "X":
        print("Exiting by request")
        break
    checkInputData(inputData)




print("Thank you for playing")
quit()
'''
Example Output
Total Daytime charges: $16.14
'''