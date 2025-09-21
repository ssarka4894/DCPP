// problem3.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <algorithm>
using namespace std;

void find_lowest_positive_integer(int* num, int usersize) {
    int* val = new int[usersize];
    int output = 1;
    int counter = 1;
    for (int i = 0; i < usersize; i++) {
        if (num[i] > 0) {
            if (exists) {
                counter = counter + 1;
            }
            output = counter;
        }
    }
    cout << output;
    /*val = output;
    return val;*/
}


int main()
{
    const int SIZE = 100;
    int usersize;
    cout << "Enter the array size" << endl;
    cin >> usersize;

    if (usersize > SIZE) {
        cerr << "Array Requested too Large";
    }


    int* num = new int[usersize];
    cout << "Enter the numbers in your array: " << endl;
    for (int i = 0;i < usersize;i++) {
        cin >> num[i];
    }

    //cout << "Here is the resultant array: " << endl;

    //int* result = find_lowest_positive_integer(num, usersize);


    //cout << "Lowest Positive number is: " << result;


    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
