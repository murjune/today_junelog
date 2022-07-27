[참고](https://codingdog.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%ED%9A%8C%EC%A0%84%EC%9D%84-1%EC%A4%84%EC%97%90-%EA%B5%AC%ED%98%84%ED%95%B4-%EB%B4%85%EC%8B%9C%EB%8B%A4)
# Zip에 대해

# 인자 해체하기(Argument unpacking) - zip함수와 *을 이용해 
"*" : 별표(*)는 리스트의 원소를 개별적인 입력인자로 zip() 함수에 넘겨주는 역할을 합니다.  

``` python
p = [(1,4), (2,5), (3,6)]

t1, t2 = zip(*p)
print(t1, t2) # (1, 2, 3) (4, 5, 6)
```


# 2개 이상의 리스트 및 튜플 자료형 묶기(packing) : zip() 함수
```python
t1, t2 = (1, 2, 3) (4, 5, 6)
packing = list(zip(t1,t2))
print(packing) # [(1,4), (2,5), (3,6)]
```
# zip을 이용한 2중 배열 회전

```python

arr = [[1,2,3,4],[5,6,7,8]]

# 시계방향 90도 회전

rotated_arr = [list(k[::-1]) for k in zip(*arr)]
print(rotated_arr) # [[5, 1], [6, 2], [7, 3], [8, 4]]

```
