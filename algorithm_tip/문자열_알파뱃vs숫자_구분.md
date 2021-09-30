# 알파벳인지 숫자인지 확인하기
  
isalpha(): 문자열 구성이 알파벳인지 확인하는 방법
isdigit(): 문자열 구성이 숫자인지 확인하는 방법
isalnum(): 문자열 구성이 알파뱃 or 숫자인지 확인하는 방법

# 예제1
``` python

s1, s2, s3, s4 = 'ab', '12', 'ab12', 'ab12#'

# s1
print(s1.isalpha()) # True
print(s1.isdigit()) # False
print(s1.isalnum()) # True
# s2
print(s2.isalpha()) # False
print(s2.isdigit()) # True
print(s2.isalnum()) # True
# s3
print(s3.isalpha()) # False
print(s3.isdigit()) # False
print(s3.isalnum()) # True
# s4
print(s4.isalpha()) # False
print(s4.isdigit()) # False
print(s4.isalnum()) # False



```
# 예제2
``` python
arr = 'abcde123%^'
str_list = []
num_list = []
for i in arr:
    if i.isalpha():
        str_list.append(i)
    elif i.isalnum():
        num_list.append(int(i))

print(str_list) # ['a', 'b', 'c', 'd', 'e']
print(num_list) # [1, 2, 3]

```
