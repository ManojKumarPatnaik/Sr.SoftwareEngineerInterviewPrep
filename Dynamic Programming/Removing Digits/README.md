[problem](https://cses.fi/problemset/task/1637/)

The idea being for any subproblem x. go through each digit of x. then recursively calculate solution for (x-d) where d is digit. the answer for subproblem will be minimum of all those results+1.

Each subproblem can be uniquely identified by x where x is given number to be reduced to zero.

    F(x) represents number of minimum steps required to reduce x to 0.

Recurrence relation

    F(x) = min(F(x-d)) for each digit d in x, where x>=10
    F(x) = 1 where x<10 (base condition) because every single digit number can be reduced to zero in one step.

Bottom up 

    bottom up approach we be created using recurrence relation above. 
    dp is array to store each subproblem. initialized with base conditions.
    dp[n] will be required answer. 

time complexity around O(n) ans space O(n)