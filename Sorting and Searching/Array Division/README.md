[problem](https://cses.fi/problemset/task/1085/)

A binary search problem. Notice following things

    For any given array the maximum sum a subarray can have is when we take full array as one. in that case subarray with maximum sum is sum all all elements of array.

    the minimum sum a subarray can have is when all elements are subarrays. in that case sum subarray with maximum is is the maximum element of array. 

    hence we know the answer will lie in range of max(arr) to sum(arr)

How do we make sure if a sum is achievable in an array.

    The algorithm is simple for that. On given array move from left to right and keep on adding each value until sum is under required sum value. Once the sum is exceeded then we start new subarray from that point and do the same process. in end we need to know how many subarray it took us to maintain the required sum inside the subarray. if it is under k then we got one answer hence we can check for smaller value otherwise we have to check for larger value.