#include<iostream>
#include<string>
#include<cstdlib>

#include "Employee.h"

using namespace std;

Employee::Employee()
{
	employeeName = "No name";
	employeeNumber = 0;
}

void Employee::SetNameNumber(string name, int number)
{
	employeeName = name;
	employeeNumber = number;
}

void Employee::PrintNameNumber()
{
	cout << "Employee name is" << employeeName << endl;
	cout << "Employee number is" << employeeNumber << endl;
}