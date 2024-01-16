// M2 Assignment Grocery Bill Thomas Burns CIS 211 Mr. Boron Jan 14 2024
/*
Assignment Content
Prior to submitting this assignment, make sure you have completed the associated Learning Activities and Practices Exercises in the module.
In this module you learned more detail about C++ syntax including, variables, literals, data types, programming style 
and how to tie all of these together to solve problems.
For this assignment, write a program that calculates a grocery bill. 
The program should output �<Your First Name�s> Market� as the title. 
The program should prompt the user to enter the price for six products of your choosing.
The program should calculate the total price of the groceries, add 6% sales tax to the groceries, and display the total price including sales tax.
Be sure to include comments throughout your code where appropriate.
Complete the C++ code using Visual Studio or Xcode, compress (zip) and upload the entire project folder to the submission area by the listed due date.
This assignment is worth 20 points and will be evaluated using the CIS 211 Assignment Rubric.
*/

#include <iostream>
using namespace std;

int main()
{

    //set input variables
    double priceProduct1;
    double priceProduct2;
    double priceProduct3;
    double priceProduct4;
    double priceProduct5;
    double priceProduct6;

    //set tax as const
    const double salesTax = 0.06;

    //set other variables to be used with math operations
    double totalAmountWithOutTax;
    double totalTax;
    double totalAmount;

    cout << "Welcome to Thomas's Market\n--------------------------\n\n"; // \n\n to add 1 blank line after title block

    //display text via cout and then take input via cin for each product- this could have also been done as totalAmountWithOutTax =+ new input....
    cout << "Enter Price for Product 1: $";
    cin >> priceProduct1;
    cout << "Enter Price for Product 2: $";
    cin >> priceProduct2;
    cout << "Enter Price for Product 3: $";
    cin >> priceProduct3;
    cout << "Enter Price for Product 4: $";
    cin >> priceProduct4;
    cout << "Enter Price for Product 5: $";
    cin >> priceProduct5;
    cout << "Enter Price for Product 6: $";
    cin >> priceProduct6;

    //Math this thing by adding all the product prices togehter to come up with a pre-tax amount
    totalAmountWithOutTax = priceProduct1 + priceProduct2 + priceProduct3 + priceProduct4 + priceProduct5 + priceProduct6;

    //Figure total tax amount and put in variable totalTax
    totalTax = totalAmountWithOutTax * salesTax;

    //Add tax + total amount without tax together to get grand total
    totalAmount = totalAmountWithOutTax + totalTax;

    //Output info
    cout << "\nBill subtotal:     $" << totalAmountWithOutTax << "\n";
    cout << "Total Tax:         $" << totalTax << "\n"; //add spaces to align
    cout << "-------------------------------\n";
    cout << "Grand Total Bill:  $" << totalAmount << "\n\n\n"; //add spaces to align
}
/* 
Example output
Welcome to Thomas's Market
--------------------------

Enter Price for Product 1: $1.25
Enter Price for Product 2: $0.5
Enter Price for Product 3: $2.34
Enter Price for Product 4: $1.47
Enter Price for Product 5: $10.9
Enter Price for Product 6: $12.02

Bill subtotal:     $28.48
Total Tax:         $1.7088
-------------------------------
Grand Total Bill:  $30.1888



*/
