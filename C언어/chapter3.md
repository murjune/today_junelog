# chapter 3 - 조건 분기

## if else

예제 1 - if , else 기본 예제
``` c
# include <stdio.h>

int main(void)
{
    // 버스 탄다고 가정, 학생/ 일반인으로 구분(일반인 : 20세)
    int age ;
    scanf("%d", &age);

    // 조건  {} else {}
    if (age >= 20)
        {
        printf("일반인 입니다.\n");
        }
    else
        {
        printf("학생입니다.\n");
        }
    return 0;
}
```
예제 2 - if , else if, else 기본 예제 + &&연산자
```c
# include <stdio.h>

int main(void)
{
    // 버스 탄다고 가정, 고등 학생/ 중학생/ 초등 학생/ 
    int age ;
    scanf("%d", &age);

    // 조건  {} else {}
    if (age < 20 && age >= 17)
        {
            printf("고등학생 입니다.\n");
        }
    else if ( 14<= age && age < 17)
        {
            printf("중학생 입니다.\n");
        }
    else if (age >= 8 && age < 14)
        {
            printf("초딩 입니다.\n");
        }
    return 0;
}
```
---
## break
```c
# include <stdio.h>

int main(void)
{
    // break
    // 1번부터 30번까지 있는 반에서 1번~ 5번까지 조별발표를 합니다.
    for (int i = 1; i <= 30 ; i++)
    {
        if (i > 6)
        {
            printf("나머지 학생들은 집에 가세요\n");
            break;
        }
        printf("%d번 학생 발표입니다.\n", i);
    }

    return 0;
}
```
출력 결과
```
1번 학생 발표입니다.
2번 학생 발표입니다.
3번 학생 발표입니다.
4번 학생 발표입니다.
5번 학생 발표입니다.
6번 학생 발표입니다.
나머지 학생들은 집에 가세요
```
---
## continue
```c
# include <stdio.h>

int main(void)
{
    // continue
    // 1번부터 30번까지 있는 반에서 7번은 아파서 결석
    // 7번을 제외하고 6번~10번까지만 발표
    for (int i = 1; i <= 30 ; i++)
    {   
        if (i == 7)
        {
            continue;
        }
        if (6<= i && i <= 10)
        {
            printf("%d번 학생 발표입니다.\n", i);
        }
         
    }

    return 0;
}
```
출력 결과
```
6번 학생 발표입니다.
8번 학생 발표입니다.
9번 학생 발표입니다.
10번 학생 발표입니다.
```
---
## && 와 || 연산자
```c
# include <stdio.h>

int main(void)
{
    int a = 10;
    int b = 10;
    int c = 12;
    int d = 13;

    if (a==b && c == d)
        {
            printf("a와 b의 값이 같고, c와 d의 값도 같습니다.\n");
        }
    else if (a == b || c == d)
        {
            printf("a와 b, 혹은 c와 d의 값이 같습니다.\n");
        }
    else 
        {
            printf("값이 다릅니다.\n");
        }
    return 0;
}
```
출력 결과
```
a와 b, 혹은 c와 d의 값이 같습니다.
```
---
## 랜덤
예제 1 
``` c
# include <time.h>
# include <stdlib.h>
# include <stdio.h>

int main(void)
{   
    srand(time(NULL)); // 난수 초기화
    int num = rand() % 3 ; // 0 ~ 2중 하나 뽑음
    // int num = rand() % 3 + 1; // 1~ 3 중 하나 뽑음
   
    return 0;
}
```
예제 2 - rand() 활용  

난수 초기화를 시켜주지 않으면, 똑같은 값만 출력한다.  
ex).7 9 3 8 0 2 4 8 3 9 // 이 값만 계속 출력
```c
# include <time.h>
# include <stdlib.h>
# include <stdio.h>

int main(void)
{   
    srand(time(NULL)); // 난수 초기화
    
    for (int i = 1 ; i  <= 10 ; i++)
        printf("%d ", rand() % 10 );

    return 0;
}
```
출력 결과
```
2 3 3 7 3 8 8 2 5 2
```
---
## switch case

switch : 값을 받아서 경우에 맞게 출력하는  조건문
``` c
# include <time.h>
# include <stdlib.h>
# include <stdio.h>

int main(void)
{   
    // 가위 0 바위 1 보 2
    strand(time(NULL));
    int i == rand() % 3; 
    switch(i) 
    {
        case 0: printf("가위\n");break; // break문을 안넣으면 아래 조건들까지 자동으로 수행됨
        case 1: printf("바위\n");break;
        case 2: printf("보\n");break;
        default: printf("몰라요\n");break;
    }
    return 0;
}
```
