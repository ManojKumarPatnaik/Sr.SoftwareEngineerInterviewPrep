[problem](https://cses.fi/problemset/task/1620)

This is a binary search question. Note few points

    1. we know upper and lower limit. The minimum being no time 0, and maximum being the slowest machine and will take to make t products. The answer will remain within these limits only.

    2. If we know for any random time T. If it's possible to make t items within time T then we don't need to check for more time that T. The answer will always be less than or equal to T.

time - 

O(max(k)*t log(n))