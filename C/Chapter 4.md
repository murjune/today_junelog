# Chater 4 - 함수

## 1. 함수의 기본형태

반환형 함수명(전달값)  
  > ex.) Void p(int num) - void는 반환하지 않는 함수  
  
1. 선언  
```c
void p(int num);
```
2. 정의
```c
void p(int num) // 함수 정의
{
    printf("num의 값은 %d입니다.\n", num);
}
```
3. 예시
```c

# include <stdio.h>
void p(int num); // 함수 p 선언
int main(void)
{   
    int num = 1;
    p(num); //num의 값은 1입니다.
    // 더하기
    num += 4;
    p(num); //num의 값은 5입니다.
    // 빼기
    num -= 1;
    p(num); //num의 값은 4입니다.
    // 곱하기
    num *= 2;
    p(num);//num의 값은 8입니다.
    // 나누기
    num /= 3;
    p(num);//num의 값은 2입니다.

    return 0;
}

void p(int num) // 함수 정의
{
    printf("num의 값은 %d입니다.\n", num);
}
```
---
## 2. 함수의 종류

### 1. 전달값 x, 반환값 x인 함수
```c

# include <stdio.h>
void p(); // 전달 값 x, 반환 값 x

int main(void)
{  
    p(); // 전달값 x, 반환값 x인 함수 입니다.
    return 0;
}

void p() // 
{
    printf("전달값 x, 반환값 x인 함수 입니다.\n");
}
```
### 2 . 전달값 ㅇ, 반환값 x인 함수
``` c

# include <stdio.h>
void p(int num); // 전달 값 ㅇ, 반환 값 x

int main(void)
{  
    p(3); // 전달값 ㅇ, 반환값 x인 함수 입니다.
    return 0;
}

void p(int num) 
{
    printf("전달값 ㅇ, 반환값 x인 함수 입니다.\n");
}
```
### 3. 전달값 x, 반환값 ㅇ인 함수
``` c

# include <stdio.h>
int r(); // 전달값 x, 반환 값 ㅇ

int main(void)
{  
    printf("%d\n",r()); // 전달값 x, 반환값 ㅇ인 함수 입니다. // 4
    return 0;
}

int r()
{
    
    printf("전달값 x, 반환값 ㅇ인 함수 입니다.\n");
    return 4;
    
}
```
### 4. 전달값(파라미터) ㅇ, 반환값 ㅇ인 함수
``` c

# include <stdio.h>
int apple(int a, int b); // 전달값 ㅇ, 반환 값 ㅇ

int main(void)
{  
    printf("남은 사과의 개수는 %d개 입니다.\n",apple(5,3)); // 전달값 ㅇ, 반환값 ㅇ인 함수 입니다. 
    return 0;                                        // 남은 사과의 개수는 2개 입니다.
}

int apple(int a, int b)
{
    
    printf("전달값 ㅇ, 반환값 ㅇ인 함수 입니다.\n");
    return a - b;
    
}
```
 
