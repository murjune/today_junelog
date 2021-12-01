``` python


# 다음 순열
def I():
    I = -1
    for i in range(n-1):
        #1 A[i] <A[i+1]인 i의 최댓값 찾기
        if A[i] < A[i+1]:
            I = max(I,i)
    return I

def J(i):
    J = i+1 # i가 0이상이면 j는 무조건 존재하기 떄문

    for j in range(i+1,n):
        if A[i] < A[j]: # A[i] < A[j]를 만족하는 j의 최댓값 찾기
            J = max(J,j)
    return J


def next_permutation(A):
    i = I()

    if i == -1:  # 다음 순열이 존재하지 않을 때

        return [-1]
    else:
        j = J(i)
        # swap : A[i]과 A[j]을 swap
        A[i], A[j] = A[j], A[i]
        # reverse
        B = A[i + 1:]
        A = A[:i + 1] + B[::-1]
        return A
n= int(input()) # N(1 ≤ N ≤ 10,000)
A = list(map(int, input().split()))# 1234 4321
print(' '.join(map(str,next_permutation(A))))

```
