[problem](https://cses.fi/problemset/task/1192)

This is a standard problem of counting number of connected components in an **undirected unweighted graph** (connected components also referred as islands). 

The idea of dfs being start from any node which is dot and visit all neighbours in 4 directions and mark them visited as well. The number of times you will have to do dfs is the number of connected components in the given graph.

time - O(nm) space - O(nm)