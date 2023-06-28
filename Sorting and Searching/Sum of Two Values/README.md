[problem](https://cses.fi/problemset/task/1640/)

This problem is same as finding two numbers in an array which adds to a fixed number. The only change is we have to maintain the index data somehow. 

In my approach I have used a 2d matrix of size nX2 which stores numbers mapped to their index.

Now sort these all numbers and find the two numbers which adds to x with two pointer techinque moving from opposite end.

Finally print the index. 