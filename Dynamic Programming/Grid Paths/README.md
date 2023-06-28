[problem](https://cses.fi/problemset/task/1638/)

The recursion idea being for any position on matrix <i,j> we have only two options move one row down or move one column right. The number to ways to reach corner from <i,j> will be equal to number of ways to reach corner from <i+1,j> and number of ways to reach corner from <i,j+1>.here <i+1,j> and <i,j+1> are subproblem which we precalculate.

    F[i][j] represents the number of ways to reach corner from position <i,j>

Recurrence relation

    F[i][j] = F[i+1][j] + F[i][j+1] , where i,j are under bound
    F[n-1][n-1] = 1 ,(base condition) the reason being if we are already on corner then only one way we can reach corner by not moving. 

Memoization

    Each subproblem can be uniquely identified by <i,j>. hence we can store results of subproblem in a matrix of size nXn.

Bottom up 

    just like memoization matrix here we require here an dp matrix of same dimensation. First we initialize the base condition then move from smaller subproblem to bigger subproblem. We start from corner and move back in column and row. dp[0][0] will have our required answer.

Time - O(n^2) space - O(n^2)

Space optimization:

    From our recurrence relation we can note that we only require the values from very next row and column. Hence we don't need to maintain a whole matrix to store values. only two rows are enough.

space - O(n)

