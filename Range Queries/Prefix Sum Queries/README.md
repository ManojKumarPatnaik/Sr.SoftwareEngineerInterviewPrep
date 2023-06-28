[problem](https://cses.fi/problemset/task/2166/)

This can be solved using segment tree(ST). we will build the solution step by step.

So our first idea is for each range in ST we will store the maximum value of prefix sum in that range. On the basis of result of child nodes we will calculate the result of parent nodes. Let's see how

    Consider a range from a to b. which can be divided in mid. hence we have two ranges [a,mid] and [mid+1,b] for which we know the result of maximum prefix sum. Now we want to calculate the maximum prefix sum of range [a,b].

    (scribbled area denote prefix with maximum sum)

<p align="center">
    <img src="./img/img1.jpg" alt="img1">
</p>

    Now to combine both results there are two possbile solution. Either the maximum prefix of a,b range will be same as a,mid range, or it will be sum of range a,mid and max prefix sum of range mid+1,b

<p align="center">
    <img src="./img/img2.jpg" alt="img2">
</p>

So to calculate the result of parent node we need two kind of information for all ranges ie

    1. sum of all elements in that particular range (this we have already done) 
    2. max prefix sum in that particular range (this we will calculate based on above explaination)

Now that we know what information we require. we can either maintain two segment trees or make a single segment tree with nodes as class/struct (it's your choice)

