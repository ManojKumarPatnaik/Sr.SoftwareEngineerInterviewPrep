[problem](https://cses.fi/problemset/task/1651/)

The idea here is to make a difference array. A difference array stores the difference of adjascent elements.

    If arr is our origional array. Make a array named diff of same dimension such that

        diff[i] = arr[i] - arr[i-1]

There are few advantages of this diff array.

HOW TO RETERIEVE VALUE AT POSITION i OF ORIGIONAL ARRAY?

    simply add all values values from 1 to i of diff array. (this can be done in logn time with BIT since BIT is good at maintaining prefix sums of an array.)

HOW TO UPDATE A RANGE FROM a to b by value u?

    In origional array it will take O(n) time to update a range of a to b. But in diff array this can be done much faster. 
    Simply add the value u to ath element in diff and subtract u to (b+1)th element if diff.(this can also 2logn time since we are maintaining BIT)

Why updating this way works?

    since to get a number in origional array are a doing prefix sum of diff. hence adding at position a and subtracting at position b+1 accounts same as if we will add a value u from a to b in origional array. 

    
