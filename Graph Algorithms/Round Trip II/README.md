[problem](https://cses.fi/problemset/task/1678/)

This is standard problem of detecting cycle in a directed graph.

So the last part of the problem was to detect cycle in undirected graph here our graph is directed. 

The idea of detecting cycle in an undirected graph is while doing dfs if we visit any node that we already visited previously we declare there is a cycle. But here there is some twist. Here there exist a cycle only if while doing dfs we encounter a node which we already visited plus that node is our **ancestor** and not a **sibling**. Then only cycle will exist. Think why.

So how do we know if our encountered node is an ancestor? That is also easy to do and we will use the power of recursion and backtracking. Maintain a separate array of size n to store the status for each node. Each node will either be marked -1 (ie this node is not an ancestor) or 0 (ie this node is an ancestor of our current processing node). 

So the idea is while we are recursing down each node on the path will be set to 0. Once the processing of that particular node is finished we unmark it -1 while backtracking. 

So now while doing dfs if we reach any node which is both visited and its status marked as 0, we declare there is a cycle in graph.

Good now how about retriving/tracing the cycle? Just like all many other graph algoritms here also we will maintain a parent array. This array will point to the parent of each node as we recurse down in dfs. In the end when I find an actual cycle. We can trace back the full cycle just by tracing this parent array, and print result in reverse order.