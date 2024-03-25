#include <iostream>
using namespace std;
void myFunc();
int main()
{   int var=100;
cout << var << endl;
myFunc();
cout << var << endl;
return 0;
}

void myFunc()
{ int var = 50;
cout << var << endl;
}
