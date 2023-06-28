board = []
for _ in range(8):
    board.append(list(input()))

ans = 0

def check(board,i,j):
    for x in range(8):
        if board[x][j] == "X":
            return False
    x = i
    y = j
    while x>=0 and y>=0:
        if board[x][y] == "X":
            return False
        x-=1
        y-=1
    
    x = i
    y = j
    while x>=0 and y<8:
        if board[x][y] == "X":
            return False
        x-=1
        y+=1
    return True

def rec(board,i,queen):
    if queen == 0:
        global ans
        ans+=1
        return
    if i == 8:
        return
    for j in range(8):
        if board[i][j] == "." and check(board,i,j):
            board[i][j] = 'X'
            rec(board,i+1,queen-1)
            board[i][j] = '.'

rec(board,0,8)
print(ans)