[problem](https://cses.fi/problemset/task/1131)

## Thought 1

The solution can be broken down in two parts. 

    First for each subtree calculate the height of that subtree. This can be done with dfs in O(n)

    Once we have height of all subtree. Go to all nodes. For each node find the two child nodes with heighest heights. So the diameter will compose these two subtrees. Take the maximum of all possible diameters. 

Both parts can be done in one dfs call.

## Thought 2

The above method is fine but there is more elegant solution also. Let's observe diameter first

    The diameter always extend from one leaf node to another leaf node.

So all we need to do is know what these two nodes are. How do find the first leaf node. That's simple just make any one node as root and find the deepest node. this node will be the one of the above two leaf nodes. 

How do we get the second node? Well that's simple as well. Fix the leaf node that we found above as root node. Now find the deepest node. This is going to be our second node. The distance between them is our diameter. 

Here in question we just want diameter length and not the actual nodes which makes it so simply we can find the height of tree when we have fixed one leaf node as root. This will give us diameter directly. 