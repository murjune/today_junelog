# 1
입력값을 1 2 3 4 5 와 같이 여러개를 한 번에 넣고 저장 하고 싶을 때
아래와 같이 코딩을 하면 출력값으로 [1, 2 , 3, 4, 5]가 나온다.
  ``` python
  a = list(map(int, input().split())) 
  #[1, 2 , 3, 4, 5]
  ```
# 2
입력값을 1 2 3 4 5 와 3 4 5 6 7 와 같이 여러개를 한 번에 넣고 저장 하고 싶을 때
아래와 같이 코딩을 하면 출력값으로 [[1, 2 , 3, 4, 5], [3, 4, 5, 6, 7]]이 나온다.
  ``` python
    result = []
    for _ in range(2):
        l = list(map(int, input().split()))
        result.append(l)
# [[1, 2, 3, 4, 5], [3, 4, 5, 6, 7]]
```
# 3
위의 코드를 아래와 같이 축약할 수 있다.
``` python
    result = [list((map(int, input().split()))) for _ in range(2)]
```
