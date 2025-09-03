#ifndef EMPLOYEE_H
#define EMPLOYEE_H
#include<iostream>
#include<cstdlib>
#include<string>

using namespace std;
class Employee
{
public:
	Employee();
	void SetNameNumber(string name, int number);
	void PrintNameNumber();

private:
	string employeeName;
	int employeeNumber;
};

#endif	
