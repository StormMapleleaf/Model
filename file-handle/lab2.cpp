#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to add two large numbers represented as strings
string ADD(string a, string b) {
    int carry = 0;
    string result = "";

    // Ensure 'a' is the longer string
    if (a.length() < b.length()) {
        swap(a, b);
    }

    int lenA = a.length();
    int lenB = b.length();

    // Perform addition digit by digit from right to left
    for (int i = 0; i < lenA; i++) {
        int digitA = a[lenA - 1 - i] - '0';
        int digitB = (i < lenB) ? b[lenB - 1 - i] - '0' : 0;
        int sum = digitA + digitB + carry;
        result = char(sum % 10 + '0') + result;
        carry = sum / 10;
    }

    // If there's a remaining carry, append it to the result
    if (carry) {
        result = char(carry + '0') + result;
    }

    return result;
}

// Memoization table to store intermediate results
vector<vector<string>> memo(101, vector<string>(101, ""));

// Function to compute binomial coefficient C(m, n)
string C(int m, int n) {
    // Base cases
    if (m == 0 || m == n) return "1";
    
    // Check memoization table
    if (memo[m][n] != "") return memo[m][n];

    // Recursively compute and store in memo table
    string result = ADD(C(m - 1, n - 1), C(m, n - 1));
    memo[m][n] = result;
    
    return result;
}

int main() {
    int m, n;
    cin >> m >> n;

    // Output the result based on the input
    if (m <= n) {
        cout << C(m, n) << endl;
    } else {
        cout << "0" << endl;
    }

    return 0;
}
