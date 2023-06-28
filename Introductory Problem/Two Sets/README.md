[problem](https://cses.fi/problemset/task/1092/)

This problem is basic variation of subset sub problem in dp.

Here I have used greedy approach of counting

few observation 

    sum = n*(n+1)/2  i.e sum of first n natural numbers
    if sum is odd then no answer exist
    if sum is even then answer is possible

the question can be rephrased as given N natural numbers make a subset that adds to sum/2. The complement subset will automatically add up to sum/2.

Imagine the approach as a bag whose capacity is sum/2. Now start from biggest number and place them inside the bag. if it's not possible to include that number that simpley skip it. 

while doing this process keep track of which numbers were added in a list. 

time - O(1)