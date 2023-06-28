[problem](https://cses.fi/problemset/task/2079/)

This problem of finding centroid is helpful in doing centroid decomposition. However finding centroid is one simple process. 

Few points to note about centroid

    1. There is always a centroid for any tree
    2. If a node is centroid then none of it's children will have more than n/2 nodes as subtree size. (This rule we use to find the centroid)

First we need to preprocess the subtree size of all nodes.

The algo is start at any arbitary node and check all it's children. If any of the children has more than n/2 subtree size. Move in that direction and continue the same. This way you will automatically reach a position when all children will have less than n/2 nodes and we will reach our centroid. 

time - O(n)