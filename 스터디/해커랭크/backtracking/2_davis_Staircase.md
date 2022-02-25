
# 문제 : [Davis' Staircase](https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking)

```python
def stepPerms(n):
    if d[n] >= 0: return d[n]
    
    d[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    return d[n]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())
    d = [-1]*(37)
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for s_itr in range(s):
        n = int(input().strip())
        
        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

```
