// classtest.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

class BankAccount
{
    private:
        double balance;

public:
    BankAccount()
        { balance = 0;  }

    BankAccount (double startingBal)
        {     balance = startingBal;    }
    void deposit (double amt)
        { balance += amt;  }
    void withDraw(double amt)
        {  balance -= amt;}
    double getBalance()
        { return balance;  }
};

int main()
{
    BankAccount acct(500.25);
    cout << acct.getBalance()<<endl;
    acct.deposit(25.25);
    cout << acct.getBalance();
}
