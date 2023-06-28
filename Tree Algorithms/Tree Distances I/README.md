[problem](https://cses.fi/problemset/task/1132/)

The solution is based on one good obervation. For any node the longest distance path will end at either ends of the diameter. With this fact we can build the solution if we know the two nodes that are present on the ends of diameter first (let's call these nodes a and b). 

Once we know the diameter nodes we will do dfs from them and mark the distance for each node. Finally we will iterate over all the nodes and check from current node i if it is good for us to go to a or to b. Out of these two cases take the maximum one.

My solution is O(7n) hence did not pass some test cases.