'''
x=12-4 * 3/ 2+ 9
print(x)
for x in range (1,10):
    print(x)



test="50"
print (type(test))
print(int(test))
convertNum=int(test)
print (type(convertNum))



try:
        
        print("xxxzzzzzz")
        changeInputDataToInt=int(test)
        print("input data: " +  inputData + " converted data type: " + type(test))
        #test=int(inputData+1)
        #calucateIfHighLowOrCorrect(int(inputData))
except:
        print("Error- Please enter X or a number between 0 and 100")

'''

def checkInputData(inputData):
    print("Hello\n")
    print("inputdata = " + str(inputData))
    print(type(inputData))
   
    
        #check if number
    try:
        
        print("xxxzzzzzz")
        changeToInt=int(inputData)
        print("input data: " +  inputData + " converted data type: " + type(changeToInt))
    except:
        print("Error- Please enter X or a number between 0 and 100")
    return


def inputCheck(incomingData):
    print("Incoming data: " + incomingData)
    try:
        convertedToInt=int(incomingData)
    except:
        print("Error")
    return convertedToInt

data1=input()
#checkInputData=(data1)
dataBack=inputCheck(data1)
print("Data back" + str(type(dataBack)))

