#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	double p, r, t;
	cin >> p >> r >> t;
	double res = (p*r*t)/100;
    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(6);
	cout << res;
	return 0;
}