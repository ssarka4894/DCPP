#include<iostream>
#include<string>
#include<cstdlib>

#include "Student.h"

using namespace std;

Student::Student()
{
	studentName = "No Name";
	studentAge = 0;
}

void Student::SetNameAge(string name, int age)
{
	studentName = name;
	studentAge = age;
}

void Student::PrintNameAge()
{
	cout << "Student name is " << studentName << endl;
	cout << "Student age is " << studentAge << endl;
}

