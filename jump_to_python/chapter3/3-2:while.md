## While
``` python
while True:  # 무한 반복

while a != 4: # a가 4일때까지 반복

while a < 4: # a가 4보다 작으면 계속 반복
```
## break

break는 반복문을 탈출하고 싶을 때 쓴다.

``` python
# while (break)
students_absent =[3, 5]
num = 0
print("출석부른다~")
while  num < 8:
    num += 1
    print("{0}번!".format(num))
    if num in students_absent:
        print("그는 오지 않았다람쥐!")
        print("나 수업 안해~")
        break # 선생님 도망~
    print("네")
 ```
 
 ## continue
 
 continue는 while문의 맨 처음으로 돌아가고 싶을 때 쓴다.(무한 루프 조심!)
 
 ``` python
# while (continue)
students_absent =[3, 5]
num = 0
print("출석부른다~")
while  num < 8:
    num += 1
    print("{0}번!".format(num))
    if num in students_absent:
        print("그는 오지 않았다람쥐!")
        continue # 다시 while num < 8로 간다.
    print("네")
 ```
