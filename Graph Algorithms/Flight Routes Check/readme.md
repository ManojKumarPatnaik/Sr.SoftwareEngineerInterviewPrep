[problem](https://cses.fi/problemset/task/1682/)

This is standard algorithm Kosaraju for strongly connected components(SSR).

Here we don't need to perform the kosaraju algorithm fully. All we have to do is find only one connected component in graph. If the size of this SSR is equal to the given graph we can say "YES" we can reach all nodes from all other nodes. 
Otherwise we need to print a node which is outside our SSR and one which is inside our SSR. since we can't reach the inside node from outside one.