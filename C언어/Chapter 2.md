# Chapter 2

# 1. 쁠쁠(++)

## 예제 1 - ++
``` C
# include <stdio.h>
int main(void)
{   
    // ++
    int a = 10;

    printf("a : %d\n", a); // a : 10
    a++;
    printf("a : %d\n", a); // a : 11
    a++;
    printf("a : %d\n", a); // a : 12
    return 0;
    
}
```
## 예제 2 - ++의 활용
```C
# include <stdio.h>
int main(void)
{   
    // ++a 
    // a = a + 1;
    int a = 10;

    printf("a : %d\n", ++a); // a: 11 , a += 1 수행 후 , a 출력
    printf("a : %d\n", a++); // a: 11 , a 출력 후, a+= 1 
    printf("a : %d\n", a); / a: 12, a 출력
    return 0;
    
}
```
---
# 2. 반복문

for , while ,do while 문이 있다.

## 1. for

for(선언 ; 조건 ; 증감)
- 예시) for(int i = 1; if i <= 10 ; i++). 
  > + 정수형 변수 i는 1이다.  
  > + i가 10 이하면  
  > + i를 처리해준 후, 1을 더한다.
``` c
# include <stdio.h>
int main(void)
{   
    // for
    for(int a = 1; a <= 10; a++)
    {
        printf("%d\n", a); 
    }
    return 0;
    
}
```
출력
```
1
2
3
4
5
6
7
8
9
10
```
