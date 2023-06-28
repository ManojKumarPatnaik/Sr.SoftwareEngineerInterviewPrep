s = list(input())
ans = []

def permute(s,n):
    if n == 0:
        ans.append("".join(s))
        return
    for i in range(n):
        s[i],s[n-1] = s[n-1],s[i]
        permute(s,n-1)
        s[i],s[n-1] = s[n-1],s[i] #revert the change

permute(s,len(s))  
ans.sort()
print(len(set(ans)))
print(ans[0])
for i in range(1,len(ans)):
    if ans[i]!=ans[i-1]:
        print(ans[i])
