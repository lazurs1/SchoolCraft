//For this assignment you will create a program converting Fahrenheit temperatures to Celsius temperatures.
//The formula for converting a temperature from Celsius to Fahrenheit is :
//F = C x 1.8 + 32, where F is the Fahrenheit temperature and C is the Celsius temperature.
//Write a function named Fahrenheit that accepts a Celsius temperature as an argument and 
//returns the temperature converted to Fahrenheit.Demonstrate the function by accepting a Celsius temperature from a user and 
//displaying the temperature converted to Fahrenheit.Be sure to include comments throughout your code where appropriate.

#include <iostream>
using namespace std;


double fahrenheit(double celsius){return (celsius * 1.8 + 32);}
int main()
{   double temp;
    cout << "What is the temperature you wish to convert?  ";
    cin >> temp;
    cout << "The temperature in fahrenheit is: " << fahrenheit(temp) << " Degrees";
}

