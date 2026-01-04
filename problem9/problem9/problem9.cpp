#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int longestSubstringKDistinct(const string& s, int k) {
    if (k <= 0 || s.empty())
        return 0;

    unordered_map<char, int> freq;
    int left = 0, maxLen = 0;

    for (int right = 0; right < s.length(); ++right) {
        freq[s[right]]++;

        // Shrink window if more than k distinct characters
        while (freq.size() > k) {
            freq[s[left]]--;
            if (freq[s[left]] == 0)
                freq.erase(s[left]);
            left++;
        }

        maxLen = max(maxLen, right - left + 1);
    }

    return maxLen;
}

int main() {
    string s = "abcba";
    int k = 2;

    cout << longestSubstringKDistinct(s, k) << endl;  // Output: 3
    return 0;
}
