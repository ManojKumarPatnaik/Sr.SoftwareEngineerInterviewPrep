[problem](https://cses.fi/problemset/task/1144/)

The prerequisite to this problem include BIT/Segment tree, Coordinate/Index compression.

Let's build the solution step by step.

## First Idea

    Our intension is to count frequency in the given range. So the most basic way to deal with this can be is to create an array which will store the frequency of each salary (index will represent the salary).

    Ex: given array 3 7 2 2 5
    we can construct the following array(aa where aa[i] is frequency of salary i)
    
        aa : 0 0 2 1 0 1 0 1  
        i  : 0 1 2 3 4 5 6 7
    
Now that we have array aa how do we answer the query?

    we need prefix sums of array aa. With prefix sums we can give how many people has salary in range a to b. Plus we have to handle updates as well. So the best suited data structures for both of these operations is a BIT or Segment tree. 

## Main Problem

    The above solution is fine but aa array will be order of billion since salary are order of billion. Hence this is a problem. The solution is using coordinate compression.

    For compression coordinates we will store all possible salary value (both from input and queries). Then sort them and give each a new index value.

    Ex: for given test case the compressed coordinates are:

        coordinates: 2 3 5 6 7
                cmp: 0 1 2 3 4
    
    now instead of making array of size 8 we can make an array of size 5 only(this makes a big difference, in big test cases we will only need to make array of million size instead of billion).

After all these it's easy to answer the queries
