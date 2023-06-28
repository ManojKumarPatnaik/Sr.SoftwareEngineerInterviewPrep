from collections import deque
import sys


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<"+str(self.x)+","+str(self.y)+">"


n, m = map(int, sys.stdin.readline().split())
g = []
for _ in range(n):
    g.append(sys.stdin.readline())

visited = [[-1]*m for _ in range(n)]


def validNode(node):
    if not(node.x >= 0 and node.x < n and node.y >= 0 and node.y < m):
        return False
    if visited[node.x][node.y] == 1 or g[node.x][node.y] == '#':
        return False
    return True


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

parent = [[None for j in range(m)] for i in range(n)]


def bfs(i, j):
    q = deque()
    q.appendleft(Node(i, j))
    while len(q) > 0:
        for _ in range(len(q)):  # remove all nodes at same level
            node = q.pop()
            if not(validNode(node)):  # discard invalid node
                continue
            visited[node.x][node.y] = 1
            for X, Y, D in dir:  # mark this node as parent of all adjascent nodes
                if not(validNode(Node(node.x+X, node.y+Y))):
                    continue
                # append next level nodes
                q.appendleft(Node(node.x+X, node.y+Y))
                if parent[node.x+X][node.y+Y] == None:
                    # mark the direction this node came from
                    parent[node.x+X][node.y+Y] = D
            if g[node.x][node.y] == "B":  # finish the search
                return Node(node.x, node.y)


for i in range(n):
    for j in range(m):
        if g[i][j] == "A":
            B = bfs(i, j)
            break
ans = []
while B != None:
    if parent[B.x][B.y] == None:
        break
    ans.append(opposite[parent[B.x][B.y]])
    P = track[parent[B.x][B.y]]
    B = Node(B.x+P[0], B.y+P[1])

if len(ans) > 0:
    print("YES")
    print(len(ans))
    print("".join(ans[::-1]))
else:
    print("NO")
