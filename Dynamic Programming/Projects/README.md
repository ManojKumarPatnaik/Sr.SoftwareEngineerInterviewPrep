[problem](https://cses.fi/problemset/task/1140)

The idea of recusion being very simple. You have two option for each project. Either you don't do it and simply go to next project or you do the currect project and look for another project whose start time is after the ending of current time. For this you can sort all the projects and do binary search for finding next suitable project. (sort project from their ending time if you start evaluation from last index otherwise sort the projects from their start time.)

SUBPROBLEM 

    F[i] represents the max profit you can make for projects from 0 to i.

RECURRENCE RELATION 

    F[i] = max( F[i-1] , profit of ith project + F[j]   ) , where j is a project which ends before ith project start.
    F[-1] = 0  when no projects are given you make zero profit

MEMOIZATION

    Each subproblem can be identified by i (number of projects 0 to ith position in sorted order of their ending time) an array of size n will be enough to memoize it.

BOTTOM UP

    Like memoization bottom up solution can be constructed in same way as memoization and following recurrent relation. Move from 0th project to end.

    finally solution will be in dp[n-1]

time - O(nlogn) space - O(n)