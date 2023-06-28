[problem](https://cses.fi/problemset/task/1646/)

This is static range queries question. Maintain a prefix 1-based array which will store sum of number from 0 to (i-1)th position at the ith index. Queries can be answered as prefix[b] - prefix[a-1] for sum in range of a to b.