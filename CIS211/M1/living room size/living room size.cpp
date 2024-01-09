//////////////////////////////////////////////////////////////////////
//                       CIS 211                                    //
//             M1 Assignment: Living Room Size                      //
//            PROF: James Boron                                     //
//            Student: Thomas Burns                                 //
//                 8 Jan 2024                                       //
//                 V 1.0                                            //
//                 NOTES:                                           //
//         More cool code check the blog for projects               //
//     https://elect144.com/index.php/category//blog                //
//     Access to my GIT email- lazurs1@gmail.com                    //
//////////////////////////////////////////////////////////////////////
/* Task:
For this assignment, write a program that calculates the size of a living room in a home.
The program should prompt the user to enter the length and width of the room in feet.
It should then calculate and display the number of square feet of the room.
*/


#include <iostream>

using namespace std;
int main ()
{
	// Set values to 0.0 and 
	double roomLength, roomWidth;
	//Get data- I could have used cin >> roomLength, roomWidth; but the user would have had to put in a <space> between them- this is cleaner to me.
	cout << "Please put in room length:\n";
	cin >> roomLength; //no input valadation or error catching- incorrect input (non number) will cause GIGO
	cout << "Please put in room width:\n";
	cin >> roomWidth; //no input valadation or error catching- incorrect input (non number) will cause GIGO
	cout << "Room Size: " << roomLength * roomWidth << " total square footage\n";


/*
example data
Please put in room length:
2.5
Please put in room width:
3.7
Room Size: 9.25 total square footage
*/







}