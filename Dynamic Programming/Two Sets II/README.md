[problem](https://cses.fi/problemset/task/1093/)

As like other subset sum problems. This one also we can solve with same recursion technique. Either include each element in subset or discard it. Plus the constraint allow us to memoize the solution very well.

SUBPROBLEM

    F[i][j] represents the number of ways to generate the sum j if only i to n-1 elements are given to us.

RECURRENCE RELATION

    F[i][j] = F[i+1][j] + F[i][j-i] 
    F[n+1][0] = 1 (base case)since number to ways to generate a sum of zero when no elements are given to us is only 1 ie empty set.

MEMOIZATION

    Each solution can be uniquely identified with i (number of elements given to us) and j (the required sum of subset) hence a matrix of dimension (n+1)X(sum/2 + 1) will be sufficent to store all results. The question constraint allows us to do it.

BOTTOM UP
    
    Bottom up solution can be constructed using recurrence relation given above. Maintain a dp matrix of size same as meoization matrix. Initialize the base case. Now interate from smaller problem to bigger. That is iterate over matrix from n value to 1. Meanwhile calculate results for each subset sum j. 

    Finally results will be stores in dp[1][sum//2]

MEMORY OPTIMIZATION

    By looking at recurrence relation we can clearly judge that we don't need to declare the whole matrix for bottom up solution. Only two rows are sufficient enough to solve the problem.

time - O(n*sum/2) space - O(sum/2)