[problem](https://cses.fi/problemset/task/1137)

We can solve this problem flattening the given tree. 

Flattening? This is basically the preorder traversal of the tree. The advantage of preorder traversal is any subtree in given tree is stored as a subarray in preorder (Big hint).

So sum of subtree in a tree becomes sum of subarray in preorder. Hence it can be done with BIT or ST. The range size will be equal to the size of subtree(this can be precalculated).

Few final things about this question. We have to build segment tree on the values of the nodes hence we have to make separate array which stores which node is stored at which index in given segment tree. Otherwise we can't update the tree.