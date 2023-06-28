[problem](https://cses.fi/problemset/task/1135/)

The distance between any two nodes u and v can be found easily if we know the depth of u and v and we know the depth of lca of u and v. This is an extension to the previous problem.

    depth[u] + depth[v] - 2*depth[LCA(u, v)]

This gives distance between u and v