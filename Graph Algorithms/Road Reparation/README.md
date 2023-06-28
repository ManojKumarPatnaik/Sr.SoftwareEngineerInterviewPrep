[problem](https://cses.fi/problemset/task/1675)

This is standard problem of finding cost of minimum spanning tree(kruskal's algorithm)(Greedy algorithm).  I have used DSU to detect loops while constructing tree. 

How to identify impossible case? For the graphs that are contain disconnected components it will be impossible to make a single minimum spanning tree. We know beforehand that there will be n-1 edges in minimum spanning tree if all components are connected. hence if after our calculation there are less that n-1 edges we will conclude an impossible case.