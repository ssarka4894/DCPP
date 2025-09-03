#ifndef STUDENT_H
#define STUDENT_H
#include<iostream>
#include<cstdlib>
#include<string>

using namespace std;

class Student
{
public:
	Student();
	void SetNameAge(string name, int age);
	void PrintNameAge();

private:
	string studentName;
	int studentAge;
};

#endif