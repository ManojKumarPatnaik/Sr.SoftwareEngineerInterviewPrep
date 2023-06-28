# TLE recursive solution
from bisect import *
import sys
sys.setrecursionlimit(10**6)


class Project:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.p = z
        
    def __repr__(self):
        return "<"+str(self.a)+","+str(self.b)+","+str(self.p)+">"


n = int(input())

projects = [0]*n
for i in range(n):
    x, y, z = map(int, input().split())
    projects[i] = Project(x, y, z)

projects.sort(key=lambda k: k.b)

bsearch = [projects[i].b for i in range(n)]


def lower_bound(input_value):
    return bisect_left(bsearch, input_value)-1


memo = [-1]*(n)


def fun(i):
    if i < 0:
        return 0
    if memo[i] != -1:
        return memo[i]
    j = lower_bound(projects[i].a)
    memo[i] = max(fun(i-1), projects[i].p + fun(j))
    return memo[i]


print(fun(n-1))
