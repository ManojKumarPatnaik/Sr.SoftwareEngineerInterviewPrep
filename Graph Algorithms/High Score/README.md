[problem](https://cses.fi/problemset/task/1673/)

This is standard problem of single source shortest path with negative edges for directed graph(Bellman–Ford algorithm).

Our question require the longest path from 1 to n. This can be done easily if all the edges weights signs are inverted, in that case the longest path will become the shortest path and we can apply the algorithm simply.

Bellman-Ford algorithm also easily identify the possibilities of negative loops which can make infinite score.

Note we are doing a dfs on reverse graph to mark only those nodes which can lead us to n. All nodes which do not lead a way to n should not be accounted.
