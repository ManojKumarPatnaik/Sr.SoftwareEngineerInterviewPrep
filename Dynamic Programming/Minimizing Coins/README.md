[problem](https://cses.fi/problemset/task/1634/)

Just like last problem this is coin change problem. Instead of counting number of combinations we require optimum solution ie minimum coins. 

The idea is similar to last problem, for any subproblem which require sum as s we try to use all coins once. and recursively calculate result for (s-c) where c in coin value. Out of all coins chosen we consider the one which yields us a optimum ie minimum solution.

    F(x) represents the minimum number of coins required to make sum of x.

Recurrence relation

    F(x) = min(F(x-c)) for each coin c. where x>0
    F(x) = 0 where x == 0 (Base case) when sum required is 0 there is no need for any coins hence zero coins required to make sum of 0.

the bottom up dp solution can be build just like last time.

Complexity

    time O(xn) which is evident from bottom up solution. space O(x) for storing dp.