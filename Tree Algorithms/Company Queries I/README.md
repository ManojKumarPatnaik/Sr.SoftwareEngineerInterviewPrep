[problem](https://cses.fi/problemset/task/1687/)

This problem can be solved efficiently using binary jumping/lifting concept. This is very similar to concept of segment tree. For any kth ancestor it can be broken in logk steps to reach that.

The idea is to store the ancestor for any node i for powers of two. Like for any node i we will store it's 1st ancestor,2nd ancestor,4th ancestor,8th ancestor and so on.

We can construct a dp table of dimension nXlogn.

In my solution

    dp[j][i] represents 2^jth ancestor for node i

Recurrence relation being

    dp[j][i] = dp[j-1][ dp[j-1][i] ] 

After this kth ancestor can be found in logk operatins