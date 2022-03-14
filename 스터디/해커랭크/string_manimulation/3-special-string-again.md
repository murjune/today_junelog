
# 풀이
조건을 만족하는 special string은 3가지 케이스로 나눌 수 있다.  
- aca, aacaa, aaaaa 와 같이 길이가 짝수이고, 중간에 위치한 알파뱃을 제외하고 모두 같은 알파벳을 갖는 문자열
- a, aaa, aaaaa, aaaaa 와 같이 길이가 홀수이고, 모든 알파뱃으로 구성된 문자열
- aa, aaaa 와 같은 길이가 짝수이고, 모든 알파뱃이 구성된 문자열

이때, 첫번째 case와 두번째 case는 같은 경우로 봐도 무방하다. 따라서, 2 가지 case로 나누어 문제를 풀었다.  
- case 1 : 문자열 길이가 홀수인 special string
문자열의 길이 만큼의 for문을 돌았는데 , 이때 i는 special string의 중간에 위치하는 알파벳의 index이다.  

1. s[i]는 special string이므로 cnt += 1
2. i의 양 옆에 있는 문자가 같은 문자이면 +1. 
3. 2번 과정을 만족하면, 2번과정을 반복하는데, 중간에 위치한 알파벳을 제외하고 모두 같은 알파벳을 갖는지 check해 준다.  

- case 2 : 문자열 길이가 짝수인 special string

case1과 같이 for문을 돌며, i,i+1 이 special string의 중간에 위치하는 알파벳의 index이다. 
1. s[i]==s[i+1]을 만족하면 cnt += 1 
2. 1번 과정을 만족하면, i, i+1의 양 옆에 있는 문자가 같은 문자이면 +1. 
3. 2번과정을 반복하는데, 중간에 위치한 알파벳을 제외하고 모두 같은 알파벳을 갖는지 check해 준다.  


```python
def substrCount(n, s):

    cnt = 0
    
    # Case 1: 'aaa', 'aacaa', 'aaaaaa'
    for i in range(n): # i is mid
        
        # s[i]는 special string이므로 cnt += 1
        cnt += 1
        l = i - 1
        r = i + 1
        
        # i의 양 옆에 있는 문자가 같은 문자이면 +1. 
        if 0<= l and r < n and s[l] ==s[r] :
            cnt += 1
            
            #  중간에 위치한 알파벳을 제외하고 모두 같은 알파벳을 갖는지 check
            while 0<= l-1 and r +1 < n and  s[l-1]==s[l]  == s[r+1]:
                cnt += 1
                l -= 1
                r += 1
                
    # Case 2 : 'aaaa'
    for i in range(n):
        
        # 1. s[i]==s[i+1]을 만족하면 cnt += 1 
        if i+1 < n and s[i] == s[i+1]: # i & i+1 is mid
            cnt += 1
            l = i - 1
            r = i + 2
            # 2. 1번 과정을 만족하면, i, i+1의 양 옆에 있는 문자가 같은 문자이면 +1.
            # 3. 2번과정을 반복하는데, 중간에 위치한 알파벳을 제외하고 모두 같은 알파벳을 갖는지 check해 준다.  
            while 0 <= l and r < n and s[l] ==s[l+1]== s[r]:
                cnt += 1
                l -= 1
                r += 1
    return cnt
```
