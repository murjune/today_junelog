# Chapter 5 : 배열

# 1. 배열(Array)
array는 index 0 부터 시작, 순차적인 공간을 가지고 있다.  
배열을 선언할 때, 크기를 지정해 주어야 한다.  


## 1. 배열의 기초 예제. 
``` c

# include <stdio.h>

int main(void)
{
    // 배열
    int subway[3]; // 배열의 크기 3

    subway[0] = 10; 
    subway[1] = 20;
    subway[2] = 30;
    for(int i= 0; i < 3 ; i++ )
    {
    printf("지하철 %d호차에는 %d명이 타고 있습니다.\n", i+1, i );
    }
    return 0;
}
```
출력 결과
```
지하철 1호차에는 0명이 타고 있습니다.
지하철 2호차에는 1명이 타고 있습니다.
지하철 3호차에는 2명이 타고 있습니다.
```

## 2. 배열의 기초 예제 2 

1. 배열의 형태
``` c
# include <stdio.h>

int main(void)
{
    // 배열
    int arr[5] = {1,2,3,4,5}; // 배열의 크기 5
    for(int i= 0; i < 5 ; i++ )
    {
    printf("arr %d번 인덱스에는 element: %d이 있습니다.\n", i, arr[i] );
    }
    return 0;
}
```
출력 결과
```c
arr 0번 인덱스에는 element: 1이 있습니다.
arr 1번 인덱스에는 element: 2이 있습니다.
arr 2번 인덱스에는 element: 3이 있습니다.
arr 3번 인덱스에는 element: 4이 있습니다.
arr 4번 인덱스에는 element: 5이 있습니다.
```
---
2. 배열의 값 초기화  

만약 다음과 같이 arr의 크기만 지정해주고 값을 초기화해주지 않는다면?
```c
int arr[5] ;
printf("%d\n", arr[0]) ; // 0
```
dummy라 하는 값(ex. -9324302840)이 출력되는데, 이 값은 컴퓨터마다 다르다 한다.  

그런데, vs code에서는 0을 초기값으로 갖는 것 같다.  

다음 case의 예제를 보자.
```c
int arr[5] = {1,2,3};
printf("%d\n", arr[4]) ; // 0
```
위의 결과를 통해 index 3부터는 자동으로 0으로 초기화 된다는 것을 알 수 있다.  

또한, 다음과 같이 배열을 초기화할 수 있는데
```c
int arr[] = {1,2,3}; // arr[3] = {1,2,3}과 동일
```
arr[3] = {1,2,3} 과 동일하다.
---
3. 배열의 크기  

배열의 크기에는 항상 상수가 들어와야 한다.
```c
# include <stdio.h>

int main(void)
{
    // 배열 크기는 항상 상수로 선언
    const int size = 10;
 
    int arr[size] = {1,2}; // error: expected expression
    printf("%d\n", arr[0]) ;
}   
```
**변수는 안됨**
```c
int size = 10; // 변수는 안됨
int arr[size] = {1,2}; // error: expected expression
```
---
# 2 문자열

## 1. 문자 vs 문자열
문자는 ' ', 문자열은 " "사이에 넣는다.  
문자 format형태 : %c, 문자열 format 형태 : %s  

문자열의 끝에는 끝을 의미하는 문자 NUll '\0'이 포함되어 있기 때문에  
기존 문자열 size+1에 해당하는 값으로 배열 크기를 지정해주어여 한다. (그런데, vscode에서는 Size로 저장해도 되네?)
``` c
// 문자
    char c = 'A'; // " "아님 작은 따옴표 ' '
    printf("%c\n",c); // A
    // 문자열
    char str[7] = "coding"; // [c][o][d][i][n][g][\0]
    printf("%s\n", str); // coding
```
또 다른 형식으로 문자열을 나타낼 수 있다.
```c
char str[] = "coding"; // 자동으로 char str[7];로 크기 지정됨
printf("%s\n", str);  // coding
printf("%d\n", sizeof(str)); // 7 , format specifies type 'int' but the argument has type 'unsigned long'
printf("%lu\n", sizeof(str)); // 7
```  
이떄, sizeof 자체가 unsigned long형이기 때문에 format 값을 %ld (l: long int를 의미)을 써주야한다.    
[참고](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=alsdomm&logNo=221434173436)
---
### 2. 반복문 활용 예제

```c
char str[] = "coding";
    
    for(int i; i < sizeof(str); i++)
    {
        printf("%c ", str[i]);
        // c o d i n g  
    }
```
### 3. 한국어 vs 영어

한국어와 영어의 메모리 크기는 다르다.  
따라서, 출력했을 때 크기가 다르게 나오는데, 한국어 1자에 3bite, 영어 1자에 1bite 갖는다고 생각하자.  
(강의에서는 2bite였는데 뭐 환경에마다 다른가?)  

[답변](https://github.com/murjune/today_junelog/new/main/C%EC%96%B8%EC%96%B4) - 즉, vscode는 utf-8을 사용
```
CP949와 EUC-KR은 한글 1글자를 2바이트로 저장하는데, UTF-8은 한글 1글자를 3바이트로 저장합니다.
```
``` c
// 한국어
char str1[] = "ㅇㅇ";
printf("%ld\n", sizeof(str1)); // 7 

// 영어

char str2[] = "abc";
printf("%ld\n", sizeof(str2)); // 4
```
# 3. 문자열 심화
뭐 심화?ㅋㅋ는 아니고 vscode에선 자동으로 Null처리를 해주기 때문에 편하다~  
다음은 위의 예시를 {}형태로 나타낸 예제다.
```c
char s1[7] = {'c','o','d','i','n','g'};
printf("%s\n", s1); // coding

char s2[6] = {'c','o','d','i','n','g'};
printf("%s\n", s2); // coding

char s3[6] = "coding";
printf("%s\n", s3); // coding
printf("%ld\n",sizeof(s3)); // 6
```
# 4. 아스키코드(ASCII)
아스키 코드에 대해선 너무 잘 알고 있으므로 (파이썬 배울 때)  
C언어로 어떻게 표현하는지만 보자!!
```c
printf("%c\n", 'a');// a
printf("%d\n", 'a');// 97

printf("%c\n", 'b');// b
printf("%d\n", 'b');// 98

printf("%c\n", 'A');// A
printf("%d\n", 'A');// 65 
```
