[problem](https://cses.fi/problemset/task/1744)

The idea is pretty simple. Given a rectangle of dimension iXj, cut it at all possible rows and all possible columns and recursively calculate the result. Out of all these take the minimum one. The base case is also pretty simple. If i == j then answer is zero.

SUBPROBLEM

    F[i][j] represents the minimum moves required to cut out square for a rectangle of dimension iXj

RECURRENCE RELATION

    F[i][j] = min( F[I][j] + F[i-I][j] + 1, F[i][J] +  F[i][j-J]+1) where I and J are all possible position to cut. 
    F[i][j] = 0 if i == j

MEMOIZATION

    Each subproblem can be memoized in a matrix of size (a+1)X(b+1)

BOTTOM UP

    Maintain a dp matrix of dimension (a+1)X(b+1) initialize the base case and follow the recurrence relation.

time - O(n^3) space - O(n^2)