# Chapter1
기본 구조
```c
# include <stdio.h>
int main() {

  return 0;
}

```
1. 모든 줄 마지막에 ;을 꼭 기입하기  
2. 맥은 visual studio를 지원 안함. 
3. dev C++ 도 지원 안한다.
# 정수형 변수

파이썬과 다르게 정수형 int로 선언을 해주어야한다.
```c
// 정수형 변수에 대한 예제
int age = 26;
printf("%d\n", age);
age = 12; // 변수값 바꾸기
printf("%d\n", age);
```
# 주석 사용법
1. /* , */
1. // (드래그 + command + /)
```c
// 주석 사용법 = /* */ , //
```
# 실수형 변수 
1. float 
1. double. 

소수점 2번째 자리까지만 나타내려면 % 뒤에 (.2)을 붙인다.
```c
// 실수형 변수 예제
float f = 2.34;
printf("%.2f\n", f);
double d = 2.05;
printf("%.2lf\n", d);
```
# 상수
const int: 정수형 상수(값이 변하는 변수와 달리 고정)
```c
// 상수 예제
const int Year = 2001;
printf("%d\n", Year);
// Year = 2001; // 상수는 바꿀 수 없다.
```
# 출력
파이썬의 print와 다르게 줄바꿈이 자동으로 되지 않는다.  
따라서, 마지막에 **\n**을 기입
아래 예제는 format을 활용한 것으로 보인다.
```c
// prinf 
int add = 7 +3 ;
printf("3 + 7 = %d\n", add);
printf("%d x %d = %d\n", 24, 45, 24*45 );
```
# 입력
vscode는 scanf_s가 없는듯...? 이거 때문에 2~3시간 낭비 ㅡㅡ

예제 1 - 정수 입력
```c
// scanf
#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
 
int main()
{
    int input;
    printf("값을 입력하시오:");
    scanf("%d", &input);
    printf("입력값 :%d\n",input);
    return 0;


}
```
예제 2 - 여러개 정수 입력
``` C
int main()
{
    int a,b,c;
 
    printf("숫자를 입력해주세요 : ");
    scanf("%d %d %d", &a, &b, &c);
 
    printf("1: %d\n", a);
    printf("2: %d\n", b);
    printf("3: %d\n", c);
 
    return 0;
```
예제 3 - 문자
문자 (한글자), 문자열(한 글자 이상의 여러 글자  
주의 사항  
> 문자열 "A" - X  
> 문자열 'A' - O
```c
#include <stdio.h>
 
int main()
{
    char c = 'A';
    printf("%c\n", c);
    return 0;
}
```
예제 4- 문자열
``` c
#include <stdio.h>
 
int main()
{
    char str[256]; // 256의 사이즈의 배열
    scanf("%s", str, sizeof(str)); // 크기를 지정
    printf("%s\n", str);
    return 0;
}
```
