[problem](https://cses.fi/problemset/task/1071)

If we want number present at x row and y column

Take the max of x and y let's call it sq 

This will give biggest square on whose outer edge this number is present, then answer will be (sq^2-somevalue) or ((sq-1)^2+somevalue).

*note that*
    
    Odd rows are increasing and even rows are decreasing  
    Even cols are increasing and odd cols are decreasing 

now check if we will calculate row wise or column wise

if sq is even (means expected number is in even row or column )

    add extra ( x + (sq - y) ) value to (sq-1)^2

else sq+1 is odd

    subtract (x - 1) - (sq-y) value to sq^2
