[problem](https://cses.fi/problemset/task/1681)

This is a simple question combining dfs and priciple of counting in dp. 

The ides is that number of ways to reach end from a node is equal to sum of the number of ways to reach end from it's childrens

Subproblem

    F[i] represents the number of ways to reach n from node i

Recurrence Relation

    F[i] = sum(F[j]) where j in all childrens from i.
    F[1] = 1 (base case) 

The above recurrence can be memoized.