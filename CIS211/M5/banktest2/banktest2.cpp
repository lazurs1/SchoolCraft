#include <iostream>

int main() {
    double startingBalance, annualInterestRate;
    std::cout << "Enter the starting balance: ";
    std::cin >> startingBalance;
    std::cout << "Enter the annual interest rate (in percentage): ";
    std::cin >> annualInterestRate;

    // Convert annual interest rate to monthly interest rate
    double monthlyInterestRate = annualInterestRate / 100 / 12;

    // Loop for six months
    for (int month = 1; month <= 6; ++month) {
        double totalDeposits, totalWithdrawals;
        std::cout << "Enter the total amount deposited into the account during month " << month << ": ";
        std::cin >> totalDeposits;

        // Validate totalDeposits input
        while (totalDeposits < 0) {
            std::cout << "Invalid input! Please enter a non-negative amount: ";
            std::cin >> totalDeposits;
        }

        double balance = startingBalance + totalDeposits;

        std::cout << "Enter the total amount withdrawn from the account during month " << month << ": ";
        std::cin >> totalWithdrawals;

        // Validate totalWithdrawals input
        while (totalWithdrawals < 0 || totalWithdrawals > balance) {
            if (totalWithdrawals < 0)
                std::cout << "Invalid input! Please enter a non-negative amount: ";
            else
                std::cout << "Invalid input! Withdrawal amount cannot exceed the current balance (" << balance << "): ";
            std::cin >> totalWithdrawals;
        }

        balance -= totalWithdrawals;

        // Calculate interest for the month
        double interest = ((startingBalance +  balance)/2) * monthlyInterestRate;

        // Update balance with interest
        balance += interest;

        // Update starting balance for the next iteration
        startingBalance = balance;

        std::cout << "Balance at the end of month " << month << ": " << balance << std::endl;
    }

    return 0;
}
