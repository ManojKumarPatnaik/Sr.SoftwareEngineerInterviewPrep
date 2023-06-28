[problem](https://cses.fi/problemset/task/1671)

This is standard problem of one point shortest path(Dijkstra's algorithm). (we can guess easily by constraints and edges are positive)

The main idea of dijkstra is to start from base node and calculate the distance of all adjascent nodes. Then process the next node which is having shortest distance (this can be done with a data structure with fast read write operation and gives us smallest element quickly like priority queue). repeat this until all nodes are processed one by one.

time - O(n+ElogV)