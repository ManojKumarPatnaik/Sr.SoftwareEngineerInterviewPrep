[problem](https://cses.fi/problemset/task/1688/)

This is standard problem of finding lowest common ancestor. This problem can be solved efficiently in same way we found kth ancestor. 

Here are steps in finding LCA

    Imagine a case in which u,v are nodes for which we want LCA and u is on higher depth compared to v.

    1. find the ancestor of u which is at the same level as v. This can be done easily if we have depth information stored. plus with help of kth ancestor function we can do it in logk time.

    2. now u and v are at same level. Here we do one conditional check. If v was already an ancestor of u then now u will be equal to v. Here we can directly return v.

    3. next we will move both u and v together. we will take bigger steps first. we move up only if ancestor of u and v are not same. Following this u and v will eventually reach just one step away from LCA node. Hence in end we take one extra step to reach LCA and return it.

    These steps can be done in logk + logn time

