[problem](https://cses.fi/problemset/task/1642/)

Just like last problem. The contraint here n<1000 hence a solution of O(n^2) will be enough to solve this. The brute force solution is going through all quartet which will be of O(n^4).

The idea is

    We will maintain a map in which we will store the sum of all pairs of numbers in O(n^2). now for every pair of numbers that add to s1 we will check in map if there is any other pair that adds up to x-s1 in O(1) time. If a matching pair exist then we have our answer.

NOTE:
the question asks us to give only distint numbers. How do we make sure that our solution only counts distinct pairs? The idea is do not pre build the map. generate is while going through all the pairs. for any pair i and j where j>i always. the map will store sum of all combination of pairs from 0 to i. this will make sure that if any quartet is found, it's going to be distint.  