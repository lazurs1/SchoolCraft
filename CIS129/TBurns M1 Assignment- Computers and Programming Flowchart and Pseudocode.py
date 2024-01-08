######################################################################
#                   CIS 129                                          #  
# M1 Assignment: Computers and Programming Flowchart and Pseudocode  #
#              PROF: James Boron                                     #
#              Student: Thomas Burns                                 #
#                   8 Jan 2024                                       #
#                   V 1.0                                            #
#                   NOTES:                                           #
#   Should have __main__ entry point so code can be resued as module #
#     Input sanatation/try/catch is needed for input                 #
#        Should have proper functions for math ops                   #
#           More cool code check the blog for projects               #
#       https://elect144.com/index.php/category/blog/                #
#       Access to my GIT email- lazurs1@gmail.com                    #
######################################################################


cubeLength = float(input ("Please input one value for 1 edge: ")) #Specifications did not say data entry type (dec, int, etc) Went with float.
cube1SideArea = cubeLength * cubeLength
cubeSArea = 6*(cubeLength * cubeLength) #Could use 6*(cubeLength^2) if cast variable
cubeVolume= cubeLength * cubeLength * cubeLength #could use cubeLength^3 if cast variable


#Print Output
print (f"Cube Surface Area 1 Side {cube1SideArea}")
print (f"Total Cube Surface Area  {cubeSArea}")
print (f"Cube Volume {cubeVolume}")


'''
Example Output
Please input one value for 1 edge: 3
Cube Surface Area 1 Side 9.0 
Total Cube Surface Area  54.0
Cube Volume 27.0 
'''