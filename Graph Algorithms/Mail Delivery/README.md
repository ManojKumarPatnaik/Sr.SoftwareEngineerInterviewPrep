[problem](https://cses.fi/problemset/task/1691)

This is standard problem of finding euler circuit in graph (Hierholzer’s Algorithm). The same algorithm works for both directed and undirected graph.

For a graph to contain euler circuit. It should be first a euler graph. We need to confirm these two conditions for graph to contain an euler circuit.

    - graph is a single connected component (ignore nodes with zero degree since they don't have any edge for to be included in euler circuit)
    - all nodes should be of even degree (or indegree and outdegree should be same in case of directed graph)

After this we will apply the algorithm.

NOTE: this algorithm modifies graph

The idea of this algorithm is also simple and similar to dfs. The difference being in dfs we don't visit a node again if it's already visited. Here we don't visit a node again if until all of it's side edges are not processed. Hence every time we visit a new node, we remove the edge we came from to show this edge is processed. and if we find a node which has no outgoing edges that means it's processing is over and we include it in our answer. (And don't worry this algorithm will always print a circuit only always not a path no matter where we start. Think why)

