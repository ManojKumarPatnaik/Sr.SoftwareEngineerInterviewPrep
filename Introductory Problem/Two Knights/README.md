[problem](https://cses.fi/problemset/task/1072/)

We will solve this counting problem in negation way

we will calculate total number of ways in which two knights can be placed in attacking position on board and subtract it from total number of ways.

Let's say board is of size k X k

    number of positions on board pos = k*k
    total number of ways to keep two knights on board = (pos)*(pos-1)/2

now let's calculate number of ways of in attacking position. 

what is the minimum size of board when two night attack each other?

<p align="center">
    <img src="./img1.png"/>
</p>

it's board of size 3X2 which gives us two postions of attack.

All other bigger boards are combination of this small board. 

hence

    how many 3X2 board will be there in a board of size k X k ? 

    it will be (k-1)*(k-2) boards
    which will give us 2*(k-1)*(k-2) attacking positions pairs

but wait yet we only considered here 3X2 boards. Even 2X3 board will give other possible paris of solution

    hence totally there are 4*(k-1)*(k-2) positions pairs possible when knights will attack each other.

therefore for a chess board of size (k X k) required answer = (pos)*(pos-1)/2 - 4*(k-1)*(k-2)

[video for reference](https://www.youtube.com/watch?v=ZwsAz57b3A4&t=712s)

