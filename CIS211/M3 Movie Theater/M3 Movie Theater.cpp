// M3 Movie Theater.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
/*
Prior to submitting this assignment, make sure you have completed the associated Learning Activities and Practices Exercises in the In this module you learned more detail about expressions and interactivity in
C++ and how to tie these together with the material from previous modules to solve problems.
Movie theaters often make more money on food and drink sales than they do on ticket sales. 
One particular theater charges $12 for tickets to evening shows and just $5 for kiddie matinees.
They have discovered that the average evening patron spends $8.50 on concessions and the average matinee patron spends $10.50 on concessions.
Write a program that computes and displays what percent of evening show income and what percent of matinee show income comes from ticket sales 
and what percent comes from concession stand purchases.

Complete the C++ code using Visual Studio or Xcode, compress (zip) and upload the entire project folder to the submission area by the listed due date.
This assignment is worth 20 points and will be evaluated using the CIS 211 Assignment Rubric.
*/
#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
    double  eveningTicket = 12.00, 
            eveningConcession = 8.50,
            eveningTicketPrecent = 0.0, 
            eveningIncomeTotal = 0.0,
            eveningConcessionPrecent = 0.0, 
            matineesTicket = 5.00,
            matineeConcession = 10.50, 
            matineeIncomeTotal=0.0, 
            matineeTicketPrecent=0.0, 
            matineeConcessionPrecent = 0.0;


    eveningIncomeTotal = eveningConcession + eveningTicket;
    matineeIncomeTotal = matineeConcession + matineesTicket;

    eveningTicketPrecent = eveningTicket * (100 / eveningIncomeTotal);
    eveningConcessionPrecent = eveningConcession * (100 / eveningIncomeTotal);

    matineeTicketPrecent = matineesTicket * (100 / matineeIncomeTotal);
    matineeConcessionPrecent = matineeConcession * (100 / matineeIncomeTotal);
    


    cout << "Evening Ticket Precent=  " << setprecision(2) << eveningTicketPrecent << "%\n";
    cout << "Evening Concession = " << setprecision(2) << eveningConcessionPrecent << "%\n";
    cout << "Matinee Ticket Precent= " << setprecision(2) << matineeTicketPrecent << "%\n";
    cout << "Matinee Concession Precent= " << setprecision(2) << matineeConcessionPrecent << "%\n";
    
}

