#include<iostream>
#include<string>
#include<cstdlib>

#include "Student.h"
#include "Employee.h"

using namespace std;

int main()
{
	Student Student1;
	Student1.SetNameAge("John Smith", 30);
	Student1.PrintNameAge();

	Employee Employee1;
	Employee1.SetNameNumber("Jane Smith", 40);
	Employee1.PrintNameNumber();

	return 0;
}