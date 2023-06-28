[problem](https://cses.fi/problemset/task/1652/)

This is same as doing prefix sum array in 1 dimension. Here we have to maintain prefix sum for 2 dimensions. 

    Make a matrix dp of dimension nXn
    where dp[i][j] stores the number of trees in rectangle (1,1) to (i,j)

This matrix can be precalculated in O(n^2) with the following relation

    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + 1,0(if (i,j) contains a tree or not)

Now queries can be answered easily with this matrix

    A rectangle starting from (x1,y1) and ending at (x2,y2) will have these many trees-
    dp[y2][x2]  - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1]