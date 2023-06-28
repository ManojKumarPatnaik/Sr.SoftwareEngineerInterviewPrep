from bisect import *


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


dp = [0]*(n)
for i in range(n):
    j = lower_bound(projects[i].a)
    if j >= 0:
        dp[i] = max(dp[i-1], projects[i].p + dp[j])
    elif i>0:
        dp[i] = max(dp[i-1], projects[i].p)
    else:
        dp[i] = projects[i].p

print(dp[n-1])
