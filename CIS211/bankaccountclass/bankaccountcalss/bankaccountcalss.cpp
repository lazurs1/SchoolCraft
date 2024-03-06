// bankaccountcalss.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
using namespace std;
//
class BankAccount
    {
    private:
        double balance;
    public:
        BankAccount()
            { balance = 0;}

        BankAccount(double startingBal)
            { balance = startingBal;}

        void depost (double amt)
            { balance += amt; }

        void withDraw(double amt)
        { balance -= amt;}

        double getBalance()
        { return balance; }
    };




int main()
{
    BankAccount acct1;
    BankAccount acct2 (500.0);
    BankAccount acct3 (300.0);

    cout << "Starting balance of account 1: $" << acct1.getBalance() << endl;
    cout << "Starting balance of account 2: $" << acct2.getBalance() << endl;
    cout << "Starting balance of account 3: $" << acct3.getBalance() << endl;

    cout << "\nDeposting 100 in account 2";
    cout << "\nWithdrawing 50.00 from account 3\n\n";
    cout << "------------------------------------------------\n";
    acct2.depost(100.0);
    acct3.withDraw(50.0);
    
    cout << "New balance of account 2: $" << acct2.getBalance() << "\n";
    cout << "New balance of account 3: $" << acct3.getBalance() << "\n";

    for (int zz = 0; zz < 500; zz++) {
        acct2.depost(.25);
        cout << "New balance of account 2: $" << acct2.getBalance() << "\n";        
    }
    cout << "aaaaaaaaaaaaaNew balance of account 2: $" << acct2.getBalance() << "\n";
}

