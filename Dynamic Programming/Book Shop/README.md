[problem](https://cses.fi/problemset/task/1158)

This is standard 0-1 knapsack problem. 

The idea for basic recursion is we have two ways to go for each item. Either we can include that item in our knapsack and check profit or we do not inlucde and then check the profit. Out of two cases we choose the optimal one. Very basic working.

Subproblem 

    F[i][j] represents the max profit we can make if we have items from 0 to i and j is capacity of knapsack 

Recurrence Relation

    F[i][j] = max( F[i-1][j] , F[i-1][j-wt[i]] + val[i]) where wt[i] is weight of ith item and val[i] is profit we make with ith item.
    F[i][j] = 0 when i = -1. here -1 means who items are given to us therefore we can't make any profit
    F[i][j] = -inf when j<0. here since knapsack capacity is negative these are illegal cases so to ingore these we return -inf which is ingnored in max function.

Memoization

    The O(2^n) complexity can be reduced to O(n*w) if we use a matrix of size nXwt to memoize it. However there are some problems here. THE CONSTRAINTS n<=10^3 and wt<=10^5 therefore O(10^8) space is not good plus 10^8 time is no good for python :(.   

Hence we require to optimize the memory. But before that let's see bottum up solution

    As memoization here we can maintain matrix of size (n+1)X(x+1) here we will use 1st based indexing for items since we have to store base case also then no items are given. But this is a bad idea space wise. 

    How to optimize space. The hint is in recurrence relation itself. Observe to fill the value of ith row we just value from (i-1)th row so we don't need to maintain such big matrix, we can just solve it using two rows.

time - O(n*x) space - O(x)

NOTE:- python solution is TLE since 10^8 input is very huge for python(it took 150 seconds to execute the bigger test cases). 
