


arr = input()
alphabetList = [0]*26

for s in arr:
    if ord(s) >= 97:
        alphabetList[ord(s)- 97] += 1
    else:
        alphabetList[ord(s)-65] += 1

ans =''
cnt = 0
pivot = max(alphabetList)
for i in range(26):
    if (alphabetList[i] == pivot):
        ans = chr(65+i)
        cnt += 1

if cnt == 1:
    print(ans)
else:
    print("?")


