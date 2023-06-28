[problem](https://cses.fi/problemset/task/1194/)

Very good question. Brilliant explaination by [dardev](https://www.youtube.com/watch?v=hB59dxdDLII). 

Better visualization for this problem will be- Imagine each monsters as bombs which are exploding and growing by 1 unit in each step. Player need to escape these bombs and reach boundry without getting in contact with any of these bombs.

The main concept here is **Multiple point BFS**.

So the idea is each monster can reach a certain position after some steps. So first we will do multiple point bfs and for each position we will mark the minimum time in which a monster will reach there.

Next our player will walk only on those position in which we reach first and not any of the monsters. 

By following above rules if we are able to reach boundry then we win otherwise we lose. 

The path can be traced in the same way for previous problems. We can maintain a parent matrix which helps us to track back.

NOTE:- this time neither of my solution got accepted :( But I feel like there must be a better way to implement it in java. 