// CIS 211 Thomas Burns Module 4- Coffee Shop program
// Mr. Boron, If you read this- can you plese let me know if you recieved my other email? Thank you
// Also, I'm assuming from the basic nature of this that its not a culmative cost ("Quantity discounts are given according to the table below.")  based on 4 LB @ 12.99 + 5-10 @ .05/lb less + 11-19 @ .10/lb less- etc.
// 

#include <iostream>
#include<iomanip>
using namespace std;
int main()

{
    const double    costPerLB=12.99,
                    discount_5to9LB =       .05,
                    discount_10_19LB =      .10,
                    discount_20to29LB =     .15,
                    discount_30orMoreLB =   .20,
                    cost_5to9LB =           costPerLB - (costPerLB * .05),
                    cost_10_19LB =          costPerLB - (costPerLB * .10),
                    cost_20to29LB =         costPerLB - (costPerLB * .15),
                    cost_30orMoreLB =       costPerLB - (costPerLB * .20);

    int inputLbs;

    cout << fixed << setprecision(2);
    cout << "Please enter the number of pounds of coffee: ";
    cin >> inputLbs;

        if (inputLbs < 5)
        {
            cout << "Your bill does not earn a discount. Your total is: $" << inputLbs * costPerLB;
        }
        else if (inputLbs >=5 && inputLbs <10)
            {
            cout << "Your order has earned a " << discount_5to9LB << "/LB discount. Your total is : $" << inputLbs * cost_5to9LB;
            }
        else if (inputLbs >= 10 && inputLbs < 20)
        {
            cout << "Your order has earned a " << discount_10_19LB << "/LB discount. Your total is : $" << inputLbs * cost_10_19LB;
        }
        else if (inputLbs >= 20 && inputLbs < 29)
        {
            cout << "Your order has earned a " << discount_20to29LB << "/LB discount. Your total is : $" << inputLbs * cost_20to29LB;
        }
        else //Over 30 LB
        {
            cout << "Your order has earned a " << discount_30orMoreLB << "/LB discount. Your total is : $" << inputLbs * cost_30orMoreLB;
        }


}

/*
Assignment Content
Prior to submitting this assignment, make sure you have completed the associated Learning Activities and Practices Exercises in the module.
In this module you learned about making decisions in C++ and how to combine decision making with the material from the first few modules to solve problems.
For this assignment, write a program that calculates a discount for buying certain quantities of coffee. Consider the following scenario:
A coffee company sells a pound of coffee for $12.99. Quantity discounts are given according to the table below.
Quantity
Discount
5-9		    5%
10-19		10%
20-29		15%
30 or more	20%
Write a program that asks for the number of pounds purchased and computes the total cost of the purchase. 
Make sure the output formatting is appropriate for the values provided. Be sure to include comments throughout your code where appropriate.
*/