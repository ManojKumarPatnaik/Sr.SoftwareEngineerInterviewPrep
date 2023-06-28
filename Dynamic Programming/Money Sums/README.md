[problem](https://cses.fi/problemset/task/1745/)

The recursion is idea is very similar to subset sum problems in dp. Just go to each number in the array and either include it in subset or do not include it. This way we can generate every possible sum that you can get with these numbers. 

The next question is how do you generate only unique sums that too in order. Here you can get creative but I used to contraints for my advantage. Here each number is below 1000 and totally there are only 100 numbers so this means any subset can't exceed the value of 100000. Hence I can simply make an boolean array of size 100000 which stores True at it's ith position if any subset can generate the sum of i. 

Finally I will just print the subset sums in order.

But there is a very good iterative solution also. It works on the idea that given all the sums that we can make using 0 to i-1 elements. For the ith element we have to just add ith element to all possible sums generated using 0 to i-1 elements. Continue this till last element and finally print unique results. 

The above approach can be used in similar way like our recursive solution to get the final result.

