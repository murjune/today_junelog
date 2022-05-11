# Chapter 2 - 반복

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
- 예시) **for(int i = 1; if i <= 10 ; i++){}**  
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
## 2. While

** while (조건) {} **
``` c
# include <stdio.h>
int main(void)
{   
    // while
    int i = 1;
    while(i <= 10)
    {
        printf("%d\n", i++); 
    }
    return 0;
    
}
```
## 3. Do while

** do {} while(조건); **
``` c
# include <stdio.h>
int main(void)
{   
    // while
    int i = 1;
    do {
        printf("%d\n", i++);
    }
    while(i <= 10);
    return 0;
    
}
```
# 3. 이중 반복문

## 구구단
```c
# include <stdio.h>
int main(void)
{   
    // 이중 for 문 - 구구단
    for(int i = 1; i <= 9; i++)
    {   
        printf("%d단\n", i);
        for (int j = 1; j<=9; j++)
        {
            printf("%d x %d = %d\n", i, j, i*j);
        }
    }
    return 0;
}
```
## 별찍기 1
```c
# include <stdio.h>
int main(void)
{   
    // 이중 for 문 - 별찍기 5단

    for(int i = 0 ; i < 5; i++)
    {   
        for(int j = 0; j <= i ; j ++)
        {
            printf("*");
        } 
        printf("\n");
    }
    return 0;
}
```
## 별 찍기 2 - 거꾸로 별찍기
``` c
# include <stdio.h>
int main(void)
{   
    // 이중 for 문 - 별찍기 5단

    for(int i = 0 ; i < 5; i++)

    {   for (int k = 1; k < 5-i; k++)
        {
            printf(" ");
        }

        for(int j = 0; j <= i ; j ++)
        {
            printf("*");
        } 
        printf("\n");
    }
    return 0;
}
```
