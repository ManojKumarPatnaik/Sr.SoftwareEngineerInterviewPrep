[problem](https://cses.fi/problemset/task/2183/)

This is a trivial problem. 

Let's say we already know result of **0 to i-1** sorted numbers , let it be **res**.

Means no subset in 0 to i-1 elements add to res.
In other words.
**Elements from 0 to i-1 can represent all sum from from 1 to res-1.**

The above statement will help in developing the solution.

    since 0 to i-1 elements can represent all sum from 1 to res-1.
    
    Then 0 to i elements can represent all sum from 1 to res-1+arr[i] if and only if arr[i] <= res.



    

