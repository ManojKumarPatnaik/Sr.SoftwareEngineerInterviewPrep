s = input()

cnt = [0]*26

def charToIndex(i):
    return ord(i)-65

def indexToChar(i):
    return chr(i+65)

for i in s:
    cnt[charToIndex(i)]+=1

flag = False
for i in cnt:
    if i%2 == 1:
        if not(flag):
            flag = True
            continue
        else:
            print("NO SOLUTION")
            exit()
    
ans = []
oddChar = ""
for i in range(26):
    if cnt[i]!=0:
        ans.append(indexToChar(i)*(cnt[i]//2))
    if cnt[i]%2 == 1:
        oddChar = indexToChar(i)
    
print("".join(ans) + oddChar  +"".join(ans[::-1]))