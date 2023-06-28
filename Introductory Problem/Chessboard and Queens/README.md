[problem](https://cses.fi/problemset/task/1624/)

This is famous N-Queens problem however again with contraints we can see that it's not expecting a very good optimized solution. 

The idea of recursion is simple. Go to each row and try to place queen on each column if possible. keep going until all 8 queens are placed and count that as answer.

The function to check if we can place queen at that position or not can be optimized. 

For each level of recursion we are recurring n more times. hence time complexity - **N^N**