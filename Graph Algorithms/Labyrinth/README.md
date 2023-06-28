[problem](https://cses.fi/problemset/task/1193)

This is standard bfs problem since we need to find **shortest distance between two fixed points**. What is interesting here is we also have to print the directional path to reach the destination.

So how do we maintain direction along with doing bfs. The idea being make another matrix which stores the direction we came from. (This is required since we have to trace back the path hence for each node we should where we came from). I called this matrix as parent.

You can either store coordinates of parent in this matrix or any other marker which helps you to trace back the path. I have stored charaters like U,D,L,R here since it's sufficient to trace back the path.

    Ex: if I moved from (3,4) to (4,4) then in parent[4][4] I will store "U" since I need to move up from (4,4) to go to it's parent.

So overall while doing bfs. If you are at any node i,j mark all the connected nodes parent to be i,j (only if child node is valid and not already been marked). The bfs return the position of B. 

From position we can track back to A using parent matrix. This path should be printed in reverse.