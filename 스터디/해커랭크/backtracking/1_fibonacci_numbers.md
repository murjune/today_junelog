# 문제: [fibonacci_numbers](https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking) 

# 풀이 
```python
def fibonacci(n):
    if n == 1 or n == 2: return 1

    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
```
