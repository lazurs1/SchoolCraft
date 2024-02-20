// M5 TBurns Banking.cpp : This file contains the 'main' function. Program execution begins and ends there.
//Write a program that calculates the balance of a savings account at the end of a six - month period.It should ask the user for 
// the starting balance and the annual interest rate.A loop should then iterate once for every month in the period, performing the following steps :
//Ask the user for the total amount deposited into the account during that month and add it to the balance.Do not accept negative numbers.
//Ask the user for the total amount withdrawn from the account during that month and subtract it from the balance.
// Do not accept negative numbers or numbers greater than the balance after the deposits for the month have been added in.
//Calculate the interest for that month.
//The monthly interest rate is the annual interest rate(1 %) divided by 12. Multiply the monthly 
//interest rate by the average of that month’s starting and ending balance to get the interest amount for the month.
//This amount should be added to the balance.

#include <iostream>
#include<iomanip>
using namespace std;



int main()
{	
	//set variables
	double	balanceStart,
		monthlyIntrestRate,
		intrestRateYear;

		cout << "Hello, Welcome to the banking program\n";
		cout << "Please enter your starting balance: $";
		cin >> balanceStart;
		cout << "Please enter yearly intrest rate: ";
		cin >> intrestRateYear;
		monthlyIntrestRate = intrestRateYear / 100/12;
		cout << "Monthly intrest" << monthlyIntrestRate;


		cout << "We will be asking for some information.\n"
			"We will be asking for 6 months deposits then next we will be asking for any monthly withdrawls\n"
			"Please only input positive numbers and do not try to overdraw your account\n"
			"------------------------------------------------------------\n";

		for (int months = 1; months <= 6; months++ ) {
			double deposit, withdraw, monthlyAvgBalance;

			cout << "Please enter month" << months<< " deposit $";
			cin >> deposit;
			while (deposit < 0)
			{
				cout << "Invalad input- please enter a non negative amount: $";
				cin >> deposit;
			}

			double workingBalance = balanceStart + deposit;
			//cout << workingBalance << "\n";
			//cout << "Balance before Withdrawles: $" << setprecision(2) << workingBalance << "\n";

			cout << "Amount withdrawn this " << months <<" month " << ": $";
			cin >> withdraw;

			while (withdraw < 0 || withdraw > workingBalance) {
				if (withdraw < 0)
					cout << "The number needs to not be NEGATIVE: ";
				else cout << "You can't take out more than you have- you have $" << workingBalance;
			}
			
			workingBalance -= withdraw;
			monthlyAvgBalance =(balanceStart + workingBalance) / 2;
			cout << "\nMonth Starting Balance: $" << setprecision(5) << balanceStart << "\nBalance at end of month: $" << setprecision(5)<< workingBalance << "\nAverage monthly Balance $" << setprecision(4) <<monthlyAvgBalance << "\n";
			balanceStart = workingBalance + (monthlyAvgBalance * monthlyIntrestRate);
			cout << "Current Month #" << months << " Balance is: $" << balanceStart << "\n";
			


		}





}

