[problem](https://cses.fi/problemset/task/1136/)

This problem is similar to static range update point query that is done on 1d arrays. Here we have to do that same for a tree.

The path from u to v goes through the LCA (this is done in previous problem). To prefix count from u to v we have to increment prefix at node u and v. we need to decrement one from lca otherwise it will count twice. To stop the effect on the parent nodes of lca we decremnt one more on parent of lca.

The above steps can be done O(logk) time since it takes logk time to find LCA of u and v.

Now after this we have to propagate on prefix once. For any parent node and we have to add sum of all it's children node.

Finally print the prefix array.