######################################################################
#                   CIS 129                                          #  
#            M2: Day time phone bill                                 #
#              PROF: James Boron                                     #
#              Student: Thomas Burns                                 #
#                   8 Jan 2024                                       #
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
In this module you learned about high quality programs. You also began learning about the individual components required to develop a high quality program.
Draw a flowchart and pseudocode for a program that produces a monthly bill for a cell phone customer. 
List at least 10 separate modules that might be included. For example, one module might calculate the charge for daytime phone minutes used.
Make a working version of this program using Python.
Complete the flowchart and pseudocode using draw.io. Include your pseudocode by adding a “square shape” next to your flowchart and populating it with your pseudocode for the program. 
Export your work in PDF format and attach it in the assignment submission area by the listed due date.
Complete the Python code using IDLE. Save your .py file and attach it in the assignment submission area by the listed due date. 
This assignment is worth 20 points and will be evaluated using the CIS 129 Assignment Rubric.
'''
#dict time:minutes- Data set was not specified or input was was not specified. Military time being used.
#This data set could be pulled from a mySQL DB (import mysql.connector-pip install mysql or API (using import results- pip install results) Or other data source

#k=Time, V=length of call
phoneCallsDict = {
  1000: 20.3,
  1100: 5,
  1230: 45,
  1400: 3,
  1700: 7,
  2100: 12,
  2300: 17
}

#Set a variable for combinging day time charges
totalCharge=float(0.0)

#Set a value of per minute charges
dateTimeRate=.20

#iteriate through the calls that were made (KEY)
for key in phoneCallsDict:
    #figure out day time- 6AM-8PM
    if key > 600 and key < 2000:
        #add to the total charges anything in daytime and pull the VALUE based on key
        totalCharge=totalCharge+ (phoneCallsDict[key]*dateTimeRate)
    print(key,phoneCallsDict[key])


print (f"Total Daytime charges: {totalCharge}")
'''
Example Output

'''