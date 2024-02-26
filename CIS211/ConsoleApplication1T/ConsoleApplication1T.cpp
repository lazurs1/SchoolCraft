// ConsoleApplication1T.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <iomanip>
#include <ios>
#include <iostream>
//
//int main()
//{
//    std::cout << "Hello World!\n";
//}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file


using namespace std;
string functiontest(string aaa)
{
    cout << "function111" << aaa;
    return "test++_+" + aaa;
    }
    int main()
{       
        //2-3
        //cout << "Programin is fun";
        
        //2-4
        //cout << "Programing is fun " << "more fun";
        //cout << "Programing is fun ";
        //cout << "more fun";

        //2-5
        //cout << "The folliwing items were top sellers" << endl;
        //cout << "during the month of June:" << endl;
        //cout << "Computer games" << endl;
        //cout << "Coffee" << endl;
        //cout << "Asprin" << endl;

        //2-6
        //cout << "The following items were top sellers\n";
        //cout << "during the month opf June\n";
        //cout << "Computergames\nCoffee";
        //cout << "\nAsprin\n";
        
        //2-7
        //int number;
        //number = 5;
        //cout << "The value of the number is " << number << endl;

        //number = 7;
        //cout << "Now the value of the nmumber is " << number << endl;


        ////2-9
        //int checking;
        //unsigned int miles;
        //long diameter;

        //checking = -20;
        //miles = 4276;
        //diameter = 100000;

        //cout << "We have made a jorney of " << miles << " miles.\n";
        //cout << "Our checking accounting balance is " << checking << " dollars\n";
        //cout << "The mMilky way galaxy is about " << diameter;
        //cout << " light years in diameter.\n";
        
        //2-10
        //int floors = 56,
        //    rooms = 300,
        //    suites = 300;

        //cout << "The Grande Hotel has " << floors << " floors\n";
        //cout << "with " << rooms << " rooms and " << suites;
        //cout << " suites.\n";

        //2-11
        //float distance = 1.496E08;
        //double mass = 1.989E30;
        //cout << "The Sun is " << distance << " kilometers away.\n";
        //cout << "The Sun\'s mass is " << mass << " kilograms.\n";

        //2-15 String
        //string movieTitle;
        //movieTitle = "Wheels fo Fury";
        //cout << "My favorite movie is " << movieTitle << endl;

        //2-16
        //bool boolValue;
        //boolValue = true;
        //cout << boolValue << endl;
        //boolValue = false;
        //cout << boolValue << endl;

        //2-17
        //double apple;
        //cout << "The size of a short interger is " << sizeof(short) << " bytes. \n";
        //cout << "The size of a long interger is " << sizeof(long) << " bytes. \n";
        //cout << "An apple can be eaten in " << sizeof(apple) << " bytes. \n";


        //2-18
        //string month = "February";
        //int year, days = 29;
        //year = 1776;
        //cout << "In " << year << " " << month << " had " << days << " days.\n";

        ////2-20           
        //double  basePayRate = 18.25,
        //    overtimePayRate = 27.38,
        //    regularHours = 40.0,
        //    overtimeHours = 10,
        //    regularWages,
        //    overtimeWages,
        //    totalWages;
        //// calc regular wages
        //regularWages = basePayRate * regularHours;
        ////calc overtime wages
        //overtimeWages = overtimePayRate * overtimeHours;
        ////total wages = regular +overtime
        //totalWages = regularWages + overtimeWages;

        //cout << "Wages for this week are $" << totalWages << endl;

        //2-21
        //int totalSeconds = 125,
        //minutes,
        //seconds;

        //minutes = totalSeconds / 60;
        //seconds = totalSeconds % 60;

        //cout << totalSeconds << " seconds is the equivalent to ";
        //cout << minutes << " minutes and " << seconds << " seconds\n";
        
        //3-1
        //int length, width, area;

        //cout << "This program calculates the area of a rectangle.\n";

        //// user imput
        //cout << "What is the length of the rectangle? ";
        //cin >> length;
        //cout << "What is the width of the rectangle? ";
        //cin >> width;

        ////comuter area
        //area = length * width;
        //cout << "The area of the rectangle is " << area << endl;
 


        //auto x = 4 + 17 % 2 - 1;
        //cout << x << endl;
        //cout << 17 % 2 << endl;
        

        ////3-7
        //int     books,
        //        months;

        //double booksPerMonth;

        ////Get user inputs
        //cout << "How many books do you plan to read? ";
        //cin >> books;

        //cout << "How many months will it take you to read them? ";
        //cin >> months;

        //// Compute and siplay books read per months
        //booksPerMonth = static_cast<double>(books) / months;
        //cout << "That is " << booksPerMonth << " books per month.\n";







    


    ////return 0;

    //int i = 0;
    //int i2 = 0;
    //int i3 = 0;
    ////cout << "test\n";

    ////for (i = 0; i < 5;) {
    ////    cout << "Hello"<< i << "\n";
    ////    i++;
    ////}
    ////

    //bool condition1 = true;
    //cout << "-----------------------------------------------------------------";
    //for (; condition1;) {
    //    
    //    cout << "Hello" << i+1 << "\n";
    //    i++;
    //    if (!(i < 5))
    //        condition1 = false;
    //}

    //cout << "-----------------------------------------------------------------";

    //while (i2 < 5)
    //    {
    //        cout << "Hello2  " << i2 + 1 << "\n";
    //        i2++;

    //    }
    //cout << "-----------------------------------------------------------------";
    //do
    //{
    //    cout << "Hello3  " << i3 + 1 << "\n";
    //    i3++;

    //} while (i3 < 9);

    //cout << "-----------------------------------------------------------------";
    //cout << "testing1   " << functiontest("bbbbn");


    //cout << "-----------------------------------------------------------------";
    //int num, limit;
    //cout << "Table of squares\n";
    //cout << "How high to go? ";
    //cin >> limit;
    //cout << "\n\nnumber square\n";
    //num = 1;
    //while (num <= limit)
    //{
    //    cout << setw(5) << num << setw(6)
    //        << num * num << endl;
    //    num++;
    //}
    //int sum = 0; // sum is the

    //cout << "-----------------------------------------------------------------";
    //while (num <= 10)     // accumulator
    //{
    //    sum += num;
    //    num++;
    //}
    //cout << "Sum of numbers 1 – 10 is "
    //    << sum << endl;

    cout << "test" << fixed << setprecision(2) << 3.1415927;
    string test = "abc";
    cout <<  "\nString Length: " << test.length() << "\n";


    const int SIZE = 12;
    char name1[SIZE], name2[SIZE];

    strcpy_s(name1, "Sebastian");
    cout << "name1 now hold s the string " << name1 << endl;

    strcpy_s(name2, name1);
    cout << "name2 now also hold the string " << name2 << endl;


    cout << "Randmom Number\n" << rand() % 7 + 1;


    string test1 = "Thomas";
    string test2 = "thomas1";
    if (test1 > test2)
        cout << "true\n";
    else
        cout << "False\n";
}