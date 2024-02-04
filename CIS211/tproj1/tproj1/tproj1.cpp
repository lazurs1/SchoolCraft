#include <iostream>
using namespace std;
int main()
{
	int seconds;
	cout << "Please enter a number of seconds:";
	cin >> seconds;

	if (seconds >= 86400)
	{
		cout << "Number of days: " << seconds / 86400;
	}
	if (seconds >= 3600 && seconds < 86400)
	{
		cout << "Number of Hours: " << seconds / 3600;
	}
	if (seconds < 3600 && seconds >=60)  cout << "Number of minutes: " << seconds / 60;
}