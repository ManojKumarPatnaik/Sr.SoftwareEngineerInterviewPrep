[problmem](https://cses.fi/problemset/task/1668)

This a standard problem of checking if graph is bipartite or graph coloring problem.  

This can be done with both dfs and bfs. The idea being give a color to current node and visit children(mark children with opposite color). If at any node we find that node and it's children has same color, we declare the graph is not bipartite. 

time - O(n) space - O(n)