// dayshoursminutes.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    const int   secPerDay = 86400,
                secPerHr = 3600,
                secPerMin = 60;
    double seconds;

    cout << "This program will convert seconds to days, hours, minutes.\n\n";
    cout << "Enter the number of seconds (60 or more): ";
    cin >> seconds;
    cout << fixed << setprecision(2);

    if (seconds >= secPerDay)
        cout << "this equals " << seconds / secPerDay << " days. \n";
    else if (seconds >= secPerHr)
        cout << "This equals " << seconds / secPerHr << " hours. \n";
    else if (seconds >= secPerMin)
        cout << "This equals " << seconds / secPerMin << " minutes. \n";
    else
        cout << "This is less than one minute.\n";
}

