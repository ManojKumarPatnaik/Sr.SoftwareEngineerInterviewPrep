#TLE on 3 test cases
from collections import deque
n, m = map(int, input().split())

g = []
monsters = [[1e6]*m for _ in range(n)]
parent = [[None]*m for _ in range(n)]

for _ in range(n):
    g.append(input())

dir = [[-1, 0, "D"], [1, 0, "U"], [0, -1, "R"], [0, 1, "L"]]
track = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}
opposite = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L"
}


def valid_block(i, j):
    if not(i >= 0 and i < n and j >= 0 and j < m):
        return False
    return True


def monsters_valid(i, j):
    if not(i >= 0 and i < n and j >= 0 and j < m):
        return False
    if monsters[i][j] != 1e6:
        return False
    if g[i][j] == "#":
        return False
    return True


def bfs_monsters():
    q = deque()
    for i in range(n):
        for j in range(m):
            if g[i][j] == "M":
                q.appendleft([i, j])
    level = 0
    while len(q) > 0:
        for _ in range(len(q)):
            i, j = q.pop()
            if not(monsters_valid(i, j)):
                continue
            monsters[i][j] = level
            for X, Y, D in dir:
                if monsters_valid(i+X, j+Y):
                    q.appendleft([i+X, j+Y])
        level += 1


def player_valid(i, j, level):
    if not(i >= 0 and i < n and j >= 0 and j < m):
        return False
    if g[i][j] == "#":
        return False
    if monsters[i][j] <= level:
        return False
    return True


def player_win(i, j, level):
    if monsters[i][j] <= level:
        return False
    if i == 0 or i == n-1 or j == 0 or j == m-1:
        return True
    return False


def bfs_player(i, j):
    q = deque()
    q.appendleft([i, j])
    level = 0
    while len(q) > 0:
        for _ in range(len(q)):
            i, j = q.pop()
            if not(player_valid(i, j, level)):
                continue
            if player_win(i, j, level):
                return True, i, j
            for X, Y, D in dir:
                if valid_block(i+X, j+Y):
                    q.appendleft([i+X, j+Y])
                    if parent[i+X][j+Y] == None:
                        parent[i+X][j+Y] = D
        level += 1

    return False, -1, -1


bfs_monsters()
for i in range(n):
    for j in range(m):
        if g[i][j] == "A":
            res, a, b = bfs_player(i, j)
            if res:
                ans = []
                while a != i or b != j:
                    ans.append(opposite[parent[a][b]])
                    a, b = a+track[parent[a][b]][0], b+track[parent[a][b]][1]
                print("YES")
                print(len(ans))
                print("".join(ans[::-1]))
                exit(0)

print("NO")
