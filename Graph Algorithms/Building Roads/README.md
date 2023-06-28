[problem](https://cses.fi/problemset/task/1666)

This is an extension to connected components problem. Here we have to just identify all connected components and connected one edge from one connected components to another. 

One very effective approach for this problem is using concept of DSU. All the nodes under one connected components belong to one set. Each set has one head node. We just have to connect all head nodes. If there are x connected components then we require x-1 edges to connect them.

The implementation being any two nodes that are connected should be taken union since they will definetly belong to same set. In the end all the nodes which no not have any parent are head nodes. Print all these nodes in pairs.
