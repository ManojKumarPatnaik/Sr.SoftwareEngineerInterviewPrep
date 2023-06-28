[problem](https://cses.fi/problemset/task/2162/)

This question is easily solvable with a queue. The idea is keep all children a queue. Now start removing children from queue. if the removed child is in even position then insert it again at the back of queue else print it and discard. 

There is one condition we need to handle in case of odd sized. The problem is this is a circle and not an array. In case of odd sized arrays we jump back to first element and remove it as well. 

Hence in case of odd sizes we have to remove one extra first child in the end. 

## Analysis

    for n = 8
    1 2 3 4 5 6 7 8 - n operations 
    1 3 5 7 - n/2 operations
    1 5 - n/4 operations
    1 - n/8 operations

therefore complexity is

n + (n/2) + (n/4) + (n/8) + .... 
n X (1 + 1/2 + 1/4 + 1/8 + ...)
n X 2

time - O(2n)