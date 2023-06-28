[problem](https://cses.fi/problemset/task/1746/)

This is another 2 dimensional dp problem.

The recursion idea is move over the given array from left to right and keep track of previous number(we can go from right to left also, it depends on solver. This will change how we process bottum up solution).

If at any position i the number is zero then we try try to explore all the possible numbers we can keep at this position.
Ideally there is only three max possible numbers we can keep at ith position ie (prev-1),prev,(prev+1) where prev is previous number.Here we will sum the answer for all these three possiblities.

If the ith number is not zero then we can simply skip to next number (although we will need to check still if prev number and current number differ max by 1 if not then these are branches that won't yield a valid solution hence we will store zero for such solutions).

subproblem

    F[i][j] represents the number of possible solutions when we have processed all numbers from i to n-1 and the previous number to ith element was j. 

Recurrence relation

    F[i][j] = F[i+1][j-1] + F[i+1][j] + F[i+1][j+1], when x[i] == 0 , make sure j lies inside bound
    F[i][j] = F[i+1][x[i]], when x[i] != 0, in this case we don't have any option hence we simply copy result from subproblem
    F[i][j] = 1(base case) if i=n because there is no number left hence a valid solution
    F[i][j] = 0(invalid cases) when the prev number and ith number do not differ at max by 1

Memoization

    Since each subproblem can be identified based on i (subarray processed from i to n-1) and j (previous number to ith element was j) then we can simply maintain a 2d matrix of dimension (n+1)X(m+1) which will be O(10^7) which is ok.

Bottum up solution

    Just like memoization here we will maintion a dp matrix of dimensions (n+1)X(m+1) and initialize base case. That is nth row should contain 1. Since this is bottum up solution we will move in opposite direction as our recursive solution. We will start from last element and lowest value of j. We will process rowise based on the recurrence relation given above and build solution up. 

    Finally our dp[1][x[0]] will have required answer for the cases when first element is not zero. Otherwise we need sum of all values in dp[1]. (this action can be included in somehow but I kept it separate).

time - O(nm) space - O(nm)

yes we can optimize space here but was not necessary.
