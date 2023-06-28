[problem](https://cses.fi/problemset/task/2217)

NOTE: We have to pick number in their natural order 1->2->3...

In short the question is to count number of increasing sub-sequesnce with an advantage that all numbers occur from 1 to n only once. (we have to take full advantage of this property).

One observation is that we start a new round only when the next number is present before current number. That is index of next number comes before the index of current number. We have to just count these cases. 

    Ex:
    1 4 5 2 3
    1st round 1->2->3 (now we start new round since 4 is present before)
    2nd round 4->5 

    hence here we require 2 round. 

so we first create an invered array(index becomes value and value becomes index) since array elements will be only from 1 to n. 

in this inverted array index represent actual numbers and value represent their origional index position. now count all pair (i-1,1) whose origional index i-1 comes before i.(count number of adjascent inversions) These many times we have to restart a round. 

time - O(n)