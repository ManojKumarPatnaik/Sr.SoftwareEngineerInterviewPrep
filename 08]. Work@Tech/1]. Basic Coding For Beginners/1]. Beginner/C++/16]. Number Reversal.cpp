#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n, reversed_number = 0, remainder;
    cin >> n;
    while(n != 0) {
        remainder = n % 10;
        reversed_number = reversed_number * 10 + remainder;
        n /= 10;
    }
    cout << reversed_number;
	return 0;
}