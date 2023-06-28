[problem](https://cses.fi/problemset/task/1686/)

This problem is an extension to finding strongly connected components (since graph is directed). 

In the previous problem we identified each connected components. So how we proceed next? First we will make a new graph in which each node will be a SCC from given graph. This new graph will be a Direced Acyclic graph (DAG). 

    This graph can be made various ways. What I have done is I already know how many nodes will be there in component. Now I iterate over each edge in origional graph and check if it's within the same SSC or differnt. If it connects two differnt SSC, I will add and edge in my DAG.

Why we need this DAG graph?

    Try to imagine how player will move. A player will start from one of the SCC and collect all the coins (since we can move to all nodes in an SCC without any restriction) then it will move to some other SCC if there is a edge available to another SCC. Then collect all the coins of that SCC and so on until he can't move to any new SCC.

    So basically we are moving from one SCC to another till we can't.

Each node of the DAG graph will store the sum of all coins that we can collect if we move only on that particular connected component. (This can be done in O(n) maintain a separate array (ssrCost) and use label data)

Now comes the part of DP. Now we have to find an optimal way of traversing over the nodes of DAG so that we get maximum coins.

What's the idea here? Iterate over each node and check it's child node. Solve chlid nodes first if not solved. now for our current node find the child which gives us maximum money(optimal). sum of this maximum coins plus the money of current node gives us the amount of money we start collecting coins from current node.

Finally print the maximum of all.

