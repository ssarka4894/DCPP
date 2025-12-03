// problem7.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

//#include <iostream>
//#include <string>
//using namespace std;
//
//// define a function to count the number of steps
//// given the number of total steps n
//// and the set of possible number of steps X = {1, 2}
//int count_step(int n, int X[2], int Xsize) {
//    int* storage = new int[n + 1];
//    for (int i = 0; i <= n; i++) {
//        storage[i] = 0;
//    }
//    storage[0] = 1;
//
//    for (int i = 0; i < n + 1; i++) {
//        for (int j = 0; j < Xsize; j++) {
//            if (i - X[j] >= 0) {
//                storage[i] += storage[i - X[j]];
//            }
//        }
//    }
//
//    int result = storage[n];
//    delete[] storage;
//    return result;
//}
//int main()
//{
//    int n = 4;
//    int X[2] = {1, 2};
//    int value = count_step(n, X, 2);
//    cout << "Total Number of step combinations: " << value << endl;
//}


#include <iostream>
#include <vector>
using namespace std;

// Count number of ways to climb n steps using steps from X
int count_step(int n, const vector<int>& X) {
    vector<int> dp(n + 1, 0);
    dp[0] = 1;  // Base case: 1 way to stand at step 0

    for (int i = 1; i <= n; i++) {
        for (int step : X) {
            if (i - step >= 0) {
                dp[i] += dp[i - step];
            }
        }
    }

    return dp[n];
}

int main() {
    int n = 4;
    vector<int> X = { 1, 2 };

    int value = count_step(n, X);
    cout << "Total number of step combinations: " << value << endl;

    return 0;
}

