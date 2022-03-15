def alternatingCharacters(s):
    # Write your code here
    tmp = s[0] # 시작 문자
    n = len(s) 
    cnt = 0 # 문자를 delete한 개수
    for i in range(1,n):
        if (s[i] == tmp): # 같은 문자면 삭제
            cnt += 1
        else:
            tmp = s[i] # 다른 문자면 tmp 바꾸기
    return cnt
