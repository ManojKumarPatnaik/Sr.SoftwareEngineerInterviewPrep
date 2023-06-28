[problem](https://cses.fi/problemset/task/1623/)

In first look this looks like another subset sum problem in dp.

But the contraint for n is very small ie <20. From here only we can guess that it's not expecting an optimised solution rather a brute-force. 

My recursion solution is very similary to knapsack dp problem. for each element in array, either include in or not. For each level of recursion calculate the differnce between numbers present in sack and numbers not present in sack. Out of all those numbers get the minimum one. 

time - 2^n