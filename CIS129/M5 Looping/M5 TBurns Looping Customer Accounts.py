######################################################################
#                   CIS 129                                          #  
#            M5 Customer Account                                     #
#              PROF: James Boron                                     #
#              Student: Thomas Burns                                 #
#                   19 Feb 2024                                      #
#                   V 1.0                                            #
#                   NOTES:                                           #
#       https://elect144.com/index.php/category/blog/                #
#       Access to my GIT email- lazurs1@gmail.com                    #
######################################################################
'''

Assignment Content
Draw a flowchart and pseudocode for the Homestead Furniture Store that gets each of the following:
Sales transaction data, including an account number
Customer name
Purchase price
Output the account number and name, then output the customer’s payment each month for the next 12 months. 
Assume that there is no finance charge, that the customer makes no new purchases, and that the customer pays off the balance with equal monthly payments.
This program should execute continuously for any number of customers until a sentinel value is supplied for the account number.

'''

print ("Welcome to the customer payment program")
sentinel="x"
inputVal=""
boolTruth= False
while  boolTruth == False:
    inputAcctNum = input("Please input your account or x to exit: ")
    if inputAcctNum != sentinel :
        if inputAcctNum.isnumeric():
            name=input("Please input your name: ")
            price=input("Please input Purchase price for your item: $")
            print("\n")
            if price.isnumeric():
                print("-----------------------------------------------------------")
                print ("Thank you "+ name + " with account #" + inputAcctNum)
                print("Your payments for the next 12 months without intrest will be:")
                print("-----------------------------------------------------------")
                priceFloat=float(price)
                monthlyPayment=round((float (price)/12),2)
                for i in range  (0,12):
                    print ("Payment #" + str(i +1) + " $"+ str(monthlyPayment))
            else: print ("Please enter a number for purchase price.")
        else:
            print("Your account number was not a number or x. Please re-enter")
    else:
        boolTruth=1
print("Thank you for your busniess")
    