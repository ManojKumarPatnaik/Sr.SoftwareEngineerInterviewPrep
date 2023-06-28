[problem](https://cses.fi/problemset/task/1073)

## Thought 1

This problem can be easily solved with concept of sets/HashSets along with two pointer approach.

The idea is maintain the set of all number between two pointers in set. If the size of set equals gap between pointers that means all numbers are unique in between. 

If so move the right pointer to add new number. If not then move the left pointer to discard the number. 

Take the maximum out of all valid lengths.

time - O(n)

## Thought 2

What if we don't want to use sets here?

The other solution is based upon the idea of nearest neighbour.

    Any valid sub array with all unique numbers in between will always occur between two nearest neighbour. 

Ex:

1 **3 5 2 7** 1 

here the subarray 3 5 2 7 contains all unique numbers which occur between to nearest neighbours 1. So the subarray with unique elements becomes 1 3 5 2 7.

This will become the base of our solution. 

    Step 1:
    Create an array which stores the index of left nearest neighbour of the number present at ith index.

    Step 2:
    With the help of nearest neighbour array calculate the max subarray with all unique elements. 

### Step 1

How do we create nearest left neighbour array?

    The idea is to first create an array which stores all only index values(let's call this array id). 

    Sort this array based upon the songs number. 
    (this way same songs indexes will come together in id)

    Now create new array for storing left neighbour index (let's call it leftNeighbour) initialized to all -1. 

    now iterate over id array. since all similar songs are adjascent to each other in this array. Simply compare each song with it's left one. If they are same means they are nearest neighbour. 

    Since id array actually stores index of songs.
    In our leftNeighbour array store these index. such that element present at ith index has it's neighbour at leftNeighbour[i] position. 


### Step 2

    Now that we have leftNeighbour data. We can proceed to calculate final answer. 

    Iterate over the leftNeighbour array. If at any point i it has a left neighbour at index j. update the right most neighbour with j.

    Now ans is simply distance between right most neighbour and i.

(This algo is good. I recommend trace this on paper for better understanding.)



