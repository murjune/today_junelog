# 문제: [Strings: Making Anagrams](https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings)
# 풀이

```python
def makeAnagram(a, b):
    d1 = [0]*26;
    d2 = [0]*26;
    for c in a:
        d1[ord(c)-97] += 1;

    for c in b:
        d2[ord(c)-97] += 1;
    
    ans = 0;

    for i in range(26):
        ans += abs(d1[i]-d2[i]);
    
    return ans;
```
