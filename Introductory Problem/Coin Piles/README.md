[problem](https://cses.fi/file/9ea35747c2646b291cece7549462479ede5430f9604451981811ef4b99a13613/1/1/)

first pile has a coins and second has b

let's say first kind of moves were done x times and second kind of moves y times.

hence 

    a = x + 2y
    b = y + 2x

add these two equations

    a+b = 3(x+y)
    x+y = (a+b)/3

now since x and y are integers so x+y will also give integer as result. hence (a+b) should be divisible by 3. This gives us our fist condition.

however this is not suffecient condition for the question. We have to also consider the cases in which the two piles differ too much in their height in those cases we can't finish both piles.

condition for that is

    a <= 2*b and b <= 2*a

time - O(1)