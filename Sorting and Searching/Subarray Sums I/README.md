[problem](https://cses.fi/problemset/task/1630)

This is a sliding window techinque with dynamic size (or a two pointers approach).

The idea is if the sum inside window exceeds the required value then remove the value from left of window else add a new value from right. This method works because all numbers are positive here. so if the window exceeds required value then there is no point to add more elements from right hence we remove elements from left.


