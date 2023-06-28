[problem](https://cses.fi/problemset/task/1676/)

This is also based upon DSU concept. Here also for every edge input makes we will try to do union of them the only addition being we have to maintain another array in which we will have to store the size of each set(or connected component). 

If both the nodes which we try to join already belong to one connected component it won't change the size of connected component neither it will change number of connected components. But if both of the nodes belong to two different connected components. Then joining them will reduce the number of components by one. and we will make new component whose size will be equal to sum of size of previous two connected components. 