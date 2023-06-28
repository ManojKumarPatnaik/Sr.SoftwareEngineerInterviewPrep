[problem](https://cses.fi/problemset/task/1679/)

This is standard problem of topological sort.   

Remember only a directed acyclic graph can have a topological sorting order.

So the main idea of topo sort is choose all source nodes first (a source node is a node with only outward edge and no inward edge). Why we start from source nodes? Because source node have no inward edge hence it can be done first.

Once all source nodes are choosen then logically remove all those nodes from graph. This will expose fresh new source nodes. Repeat this process until nothing is left.

Remember any two parallet source nodes can be taken up in any order since they are not dependent over each other.

Now how do we know if graph is not an acyclic graph ie it has cycle? This can be also done when the above algorithm finishes. In the end if there are some nodes which have inward nodes left but still no sinks are there is graph. This is a condition of a cycle to be present. 