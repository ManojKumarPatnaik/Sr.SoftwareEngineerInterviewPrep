[problem](https://cses.fi/problemset/task/1070/)

for n = 2 and n = 3 there are no solution which can be manually checked

since we want numbers which are adjascent to just differ by 1. we can create one list of all even numbers and other list of all numbers under n.

and then just concatenate them. that's all 

example
```
    n = 7
    odd list -> 1 3 5 7
    even list -> 2 4 6 

    contenated list 2 4 6 1 3 5 7 <-required answer 
```
always place even list before odd list for solving edge cases. 

time - O(n)