
 #include <iostream>
 #include <windows.h> // Needed to display colors and call Sleep
 using namespace std;

 int main()
{
	 // Create a handle to the computer screen.
		HANDLE screen = GetStdHandle(STD_OUTPUT_HANDLE);
	
		 // Write 16 lines in 16 different colors.
		 for (int color = 0; color < 255; color++)
		 {
		 SetConsoleTextAttribute(screen, color);
		 cout << color << " Hello World!" << endl;
		 //Sleep(400); // Pause between lines to 		watch them appear
			 }
	 // Restore the normal text color)
		SetConsoleTextAttribute(screen, 7);
	 return 0;
	 }