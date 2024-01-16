// RestaurantBill.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;
int main()
{
    double billAmount = 44.50;
    double tax = 0.0675;
    double tip = 0.15;
    double taxTotal = billAmount * tax;
    double subTotal = billAmount + taxTotal;
    double tipAmount = subTotal * tip;
    double totalBill = subTotal + tipAmount;
    cout << 5 / 2 << "\n";

    cout << "Meal Cost: $" << billAmount << "\n";
    cout << "Tax amount: $" << taxTotal << "\n";
    cout << "Meal + Tax amount: $" << subTotal << "\n";
    cout << "Tip Amount: $" << tipAmount << "\n";
    cout << "Total Bill: $" << totalBill << "\n";
}

