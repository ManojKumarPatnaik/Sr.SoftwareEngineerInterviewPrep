n = int(input())

a = [0]*n
b = [0]*n
for i in range(n):
    a[i],b[i] = map(int,input().split())

# each movie is identified by it's index
movie = [i for i in range(n)]

# sort all movies by their ending time
movie.sort(key=lambda x:b[x])

cnt = 0
time = 0
for i in range(n):
    if time<=a[movie[i]]: #next movie starts before current time
        cnt+=1
        time = b[movie[i]]

print(cnt)
    
