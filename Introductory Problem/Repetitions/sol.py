s = input()

i,j=0,0
ans = 1
while i<len(s):
    j=i+1
    while j<len(s) and s[i] == s[j]:
        j+=1
    ans = max(ans,j-i)
    i = j
print(ans)