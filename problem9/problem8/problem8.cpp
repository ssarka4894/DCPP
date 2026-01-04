// problem8.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <deque>
#include <vector>
using namespace std;

void printSlidingWindowMax(const vector<int>& a, int k) {
    int n = (int)a.size();
    if (k <= 0 || k > n) {
        cout << "Input Not Valid!\n";
        return;
    }

    deque<int> dq; // stores indices, a[dq] is decreasing

    for (int i = 0; i < n; i++) {
        // Remove out-of-window indices
        while (!dq.empty() && dq.front() <= i - k) dq.pop_front();

        // Maintain decreasing deque
        while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();

        dq.push_back(i);

        // Print max once first window is ready
        if (i >= k - 1) {
            cout << a[dq.front()] << (i == n - 1 ? '\n' : ' ');
        }
    }
}

int main() {
    vector<int> arr = { 10, 5, 2, 7, 8, 7 };
    int k = 3;
    printSlidingWindowMax(arr, k); // 10 7 8 8
}
