/*
* 
   _____ _____  _____   ___  __ __ 
  / ____|_   _|/ ____| |__ \/_ /_ |
 | |      | | | (___      ) || || |
 | |      | |  \___ \    / / | || |
 | |____ _| |_ ____) |  / /_ | || |
  \_____|_____|_____/  |____||_||_|
                                   
TBurns
Module 7

In this module you learned about Object-Oriented programming in C++ and how to combine this 
approach with the concepts covered in previous modules
-------------------------------------------------------------------------
A student has established the following monthly budget:
Housing                         1000.00
Utilities, Internet & Phone     200.00
Household expenses              63.00
Transportation                  52.00
Food                            250.00
Medical                         40.00
Insurance                       125.00
Entertainment                   130.00
Clothing                        80.00
Miscellaneous                   50.00
-------------------------------------------------------------------------
Write a modular program that declares a MonthlyBudget structure with member variables 
to hold each of these expense categories. The program should create two MonthlyBudget 
structure variables. The first will hold the budget figures given above. 
The second will hold the user-enter amounts actually spent during the past month. 
Using Program 7-19 as a model, the program should create a screen form that displays 
each category name and its budgeted amount, then positions the cursor next to it for 
the user to enter the amount actually spent in that category. 
Once the user data has all been entered, the program should compute and display the 
amount over or under budget the student’s expenditures were in each category, 
as well as the amount over or under budget for the entire month.

*/



#include <iostream>
#include <windows.h> 
#include <string>
using namespace std;
struct MonthlyBudget {
	float Housing,
		UtilitiesInternetPhone,
		Householdexpenses,
		Transportation,
		Food,
		Medical,
		Insurance,
		Entertainment,
		Clothing,
		Miscellaneous,
		Total;


};

void placeCursor(HANDLE, int, int);   // Function prototypes
void displayPrompts(HANDLE);
void displayPrevInfo(HANDLE screen, MonthlyBudget test);
void userInput(HANDLE screen, MonthlyBudget& mBudUserNums, MonthlyBudget lastMonthData);
void displayLogo(HANDLE screen);
//void userInput(HANDLE, MonthlyBudget&);



int main()
{
	
    MonthlyBudget mBudwithNums;
    mBudwithNums.Housing = 1000.00;
    mBudwithNums.UtilitiesInternetPhone = 200.00;
    mBudwithNums.Householdexpenses = 63.00;
    mBudwithNums.Transportation = 52.00;
    mBudwithNums.Food = 250.00;
    mBudwithNums.Medical = 40.00;
    mBudwithNums.Insurance = 125.00;
    mBudwithNums.Entertainment = 130.00;
    mBudwithNums.Clothing = 80.00;
    mBudwithNums.Miscellaneous = 50.00;
    MonthlyBudget mBudUserNums;

	// Get the handle to standard output device (the console)
	HANDLE screen = GetStdHandle(STD_OUTPUT_HANDLE);

	displayLogo(screen);


	mBudwithNums.Total = mBudwithNums.Miscellaneous + mBudwithNums.Clothing + mBudwithNums.Entertainment + mBudwithNums.Insurance + mBudwithNums.Medical + mBudwithNums.Food + mBudwithNums.Transportation + mBudwithNums.Householdexpenses + mBudwithNums.UtilitiesInternetPhone + mBudwithNums.Housing;
	placeCursor(screen, 0, 0);
	cout << mBudwithNums.Total;

	displayPrompts(screen);
	displayPrevInfo(screen, mBudwithNums);
	userInput(screen, mBudUserNums, mBudwithNums);


	mBudwithNums.Total = mBudwithNums.Miscellaneous + mBudwithNums.Clothing + mBudwithNums.Entertainment + mBudwithNums.Insurance + mBudwithNums.Medical + mBudwithNums.Food + mBudwithNums.Transportation + mBudwithNums.Householdexpenses + mBudwithNums.UtilitiesInternetPhone + mBudwithNums.Housing;
	placeCursor(screen, 0, 0);
	cout << mBudwithNums.Total;
	placeCursor(screen, 0, 20);
	cout << mBudUserNums.Total;

	if (mBudwithNums.Total > mBudUserNums.Total)
	{
		SetConsoleTextAttribute(screen, 32);
		placeCursor(screen, 16, 82);
		cout << "$" << mBudwithNums.Total - mBudUserNums.Total << " Is the amount saved";

	}
	else {
		SetConsoleTextAttribute(screen, 4);
		placeCursor(screen, 16, 82);
		cout << "$" << (mBudwithNums.Total - mBudUserNums.Total) * -1 << " Is the amount you are over!";
	}


	placeCursor(screen, 24, 7);
}


/******************************************************
 *                    placeCursor                     *
 ******************************************************/
void placeCursor(HANDLE screen, int row, int col)
{                       // COORD is a defined C++ structure that  
	COORD position;     // holds a pair of X and Y coordinates
	position.Y = row;
	position.X = col;
	SetConsoleCursorPosition(screen, position);
}

/******************************************************
 *                   displayPrompts                   *
 ******************************************************/
void displayPrompts(HANDLE screen)
{
	SetConsoleTextAttribute(screen, 10);
	placeCursor(screen, 1, 50);
	cout << "Monthly Budget";
	placeCursor(screen, 2, 0);
	cout << "------------------------------------------------------------------------------------------------------------------------";
	placeCursor(screen, 3, 0);
	cout << "    Item                            Last Cost            This month Cost          Difference";
	placeCursor(screen, 4, 0);
	cout << "------------------------------------------------------------------------------------------------------------------------";
	placeCursor(screen, 5, 3);
	cout << "Housing:";	
	placeCursor(screen, 6, 3);
	cout << "Utilities, Internet & Phone:";
	placeCursor(screen, 7, 3);
	cout << "Household expenses:";
	placeCursor(screen, 8, 3);
	cout << "Transportation:";
	placeCursor(screen, 9, 3);
	cout << "Food:";
	placeCursor(screen, 10, 3);
	cout << "Medical:";
	placeCursor(screen, 11, 3);
	cout << "Insurance:";
	placeCursor(screen, 12, 3);
	cout << "Entertainment:";
	placeCursor(screen, 13, 3);
	cout << "Clothing:";	
	placeCursor(screen, 14, 3);
	cout << "Miscellaneous:";
	placeCursor(screen, 15, 0);
	cout << "------------------------------------------------------------------------------------------------------------------------";
	placeCursor(screen, 16, 3);
	cout << "Total:";



	placeCursor(screen, 5, 57);
	cout << "$";
	placeCursor(screen, 6, 57);
	cout << "$" ;
	placeCursor(screen, 7, 57);
	cout << "$" ;
	placeCursor(screen, 8, 57);
	cout << "$" ;
	placeCursor(screen, 9, 57);
	cout << "$" ;
	placeCursor(screen, 10, 57);
	cout << "$" ;
	placeCursor(screen, 11, 57);
	cout << "$" ;
	placeCursor(screen, 12, 57);
	cout << "$" ;
	placeCursor(screen, 13, 57);
	cout << "$" ;
	placeCursor(screen, 14, 57);
	cout << "$" ;
	placeCursor(screen, 16, 57);
	cout << "$" ;

}

void displayPrevInfo(HANDLE screen, MonthlyBudget lastMonthData)
{
	SetConsoleTextAttribute(screen, 10);
	placeCursor(screen, 5, 37);
	cout << "$" << lastMonthData.Housing ;
	placeCursor(screen, 6, 37);
	cout << "$" << lastMonthData.UtilitiesInternetPhone ;
	placeCursor(screen, 7, 37);
	cout << "$" << lastMonthData.Householdexpenses ;
	placeCursor(screen, 8, 37);
	cout << "$" << lastMonthData.Transportation ;
	placeCursor(screen, 9, 37);
	cout << "$" << lastMonthData.Food ;
	placeCursor(screen, 10, 37);
	cout << "$" << lastMonthData.Medical ;
	placeCursor(screen, 11, 37);
	cout << "$" << lastMonthData.Insurance ;
	placeCursor(screen, 12, 37);
	cout << "$" << lastMonthData.Entertainment ;
	placeCursor(screen, 13, 37);
	cout << "$" << lastMonthData.Clothing ;
	placeCursor(screen, 14, 37);
	cout << "$" << lastMonthData.Miscellaneous ;
	placeCursor(screen, 16, 37);
	cout << "$" << lastMonthData.Total;
}



void userInput(HANDLE screen, MonthlyBudget& mBudUserNums, MonthlyBudget lastMonthData)
{
	placeCursor(screen, 5, 58);
	cin >> mBudUserNums.Housing;
	placeCursor(screen, 5, 82);
	cout << "$" << lastMonthData.Housing - mBudUserNums.Housing;

	placeCursor(screen, 6, 58);
	cin >> mBudUserNums.UtilitiesInternetPhone;
	placeCursor(screen, 6, 82);
	cout << "$" << lastMonthData.UtilitiesInternetPhone - mBudUserNums.UtilitiesInternetPhone;

	placeCursor(screen, 7, 58);
	cin >> mBudUserNums.Householdexpenses;
	placeCursor(screen, 7, 82);
	cout << "$" << lastMonthData.Householdexpenses - mBudUserNums.Householdexpenses;

	placeCursor(screen, 8, 58);
	cin >> mBudUserNums.Transportation;
	placeCursor(screen, 8, 82);
	cout << "$" << lastMonthData.Transportation - mBudUserNums.Transportation;

	placeCursor(screen, 9, 58);
	cin >> mBudUserNums.Food;
	placeCursor(screen, 9, 82);
	cout << "$" << lastMonthData.Food - mBudUserNums.Food;

	placeCursor(screen, 10, 58);
	cin >> mBudUserNums.Medical;
	placeCursor(screen, 10, 82);
	cout << "$" << lastMonthData.Medical - mBudUserNums.Medical;

	placeCursor(screen, 11, 58);
	cin >> mBudUserNums.Insurance;
	placeCursor(screen, 11, 82);
	cout << "$" << lastMonthData.Insurance - mBudUserNums.Insurance;

	placeCursor(screen, 12, 58);
	cin >> mBudUserNums.Entertainment;
	placeCursor(screen, 12, 82);
	cout << "$" << lastMonthData.Entertainment - mBudUserNums.Entertainment;

	placeCursor(screen, 13, 58);
	cin >> mBudUserNums.Clothing;
	placeCursor(screen, 13, 82);
	cout << "$" << lastMonthData.Clothing - mBudUserNums.Clothing;

	placeCursor(screen, 14, 58);
	cin >> mBudUserNums.Miscellaneous;
	placeCursor(screen, 14, 82);
	cout << "$" << lastMonthData.Miscellaneous - mBudUserNums.Miscellaneous;

	float total2 = mBudUserNums.Miscellaneous + mBudUserNums.Clothing + mBudUserNums.Entertainment + mBudUserNums.Insurance + mBudUserNums.Medical + mBudUserNums.Food + mBudUserNums.Transportation + mBudUserNums.Householdexpenses + mBudUserNums.UtilitiesInternetPhone + mBudUserNums.Housing;
	placeCursor(screen, 16, 57);
	cout << "$" << total2;
	mBudUserNums.Total = total2;
}

void displayLogo(HANDLE screen)
{
	placeCursor(screen, 20, 0);


	cout << "    ______  _____   ______      _____    __      __\n";
	cout << "  .' ___  ||_   _|.' ____ \    / ___ `. /  |    /  |\n";
	cout << " / .'   \_|  | |  | (___ \_|  |_/___) | `| |   ` | |\n";
	cout << "| |          | |   _.____`.     .'____.'  | |     | |\n";
	cout << " \ `.___.'\ _| |_ | \____) |  / /_____ _ | |_   _| |_ \n";
	cout << "  `.____ .'|_____| \______.'  |_______||_____ ||_____| \n";

}
