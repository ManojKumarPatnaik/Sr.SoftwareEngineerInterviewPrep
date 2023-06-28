[problem](https://cses.fi/problemset/task/1197/)

This is a very good extension to bellman-ford algorithm for single source shortest path.

Bellman-Ford helps us here to detect if there are any negative cycles in graph.

What additional challenages in question?

    How do you detect negative cycles in disconnected directed graph using bellman-ford algoritm?

    How do you trace back the negative cycle?

So for the first question. 
    The problem is this algorithm is **single sourced** so the problem is if we choose any node as source. It might have some disconnected graphs which we never reach. 

    The simple solution to this problem is that add one more dummy node to the graph which connects to every node in graph with zero edge weight and we make this dummy node as source node. Will this node change our answer? No since all the edges from this dummy node will be outward so there is no way this node can make another cycle. But adding this node will make sure we relax all the connected components and not just one connected component.  

Now coming to second challange.

    How do we trace back? This is also similar to all the previous graph questions with tracing. We will maintain a predecessar/parent array which will store the parent of each node. 
    In our case suppose u->v is a edge and if node v is **relaxed** by node u. So u is the parent of v.

    Good now we have parent of all nodes after performing bellman ford algorithm. Now what's next?

We can DETECT if the graph has any negative cycle in nth relaxation.(This is from Bellman Ford algorithm)

Okay Now we know there is a negative cycle. How do we trace it?

    This can be done with the help of the node which got relaxed at last.(The node which got relaxed in the end of nth relaxation). Now why is this node important to us?

    The thing is this last relaxed node got relaxed because there was a negative cycle in graph. Hence if we trace back from last relaxed node and get to the cycle (just like a murder mystery).

    Okay now we know where to start trace back. But the issue is this last relaxed node is not gurranteed to be the part of negative cycle (this node can also lie outside of negative cycle). So how far we should trace back to get to the actual cycle node????

Before answer the previous problem remember the fact that tracing from last relaxed will GURANTEED make us reach negative cycle.

The answer to previous problem lies in the fact that there are n nodes. and there is a cycle in graph (imagine this as self loop and rest of graph is linked list). hence in worst case we will have to trace back n-1 nodes back to reach to the actual cycle.

So now,
**Doing atleast n-1 trace back will definetly get us to one of the node in negative cycle**

Finally printing this cycle. The idea is keep of tracing back in this negative loop until you reach to the same node again. Finally print the data in reverse order.

## Overall 

The solution can be broken down in following steps

    Add dummy node to the graph
    Relax all the edges n-1 times atleast.
        - parallely maintain the parent of each node
    Detect negative cycle in nth relaxation
    If there is negative cycle
        - trace back the last relaxed node at least n-1 times to enter cycle
        - trace all the nodes of negative cycle
        - print the result
