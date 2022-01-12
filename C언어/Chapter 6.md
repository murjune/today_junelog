[참고 ](https://dojang.io/pluginfile.php/339/mod_page/content/30/unit34-9.png)
# Chapter 6 - 포인터!!

▼ 그림 34-9 변수, 주소 연산자, 역참조 연산자, 포인터의 차이 

<img width = "600" src = "https://dojang.io/pluginfile.php/339/mod_page/content/30/unit34-9.png" >
[출처]: https://dojang.io/pluginfile.php/339/mod_page/content/30/unit34-9.png. 

## 포인터 예제
``` c
# include <stdio.h>

int main(void)
{
    int * ptr ; // pointer int*로 초기화
    int * ptr2 ; // pointer int*로 초기화
    int num = 10;
    ptr = &num; // num의 주소값
    ptr2 = num; // 오류!! int형이 아니라 int*값을 받아야함

    printf("%p\n", ptr); // 0x16d8cb4c4
    printf("%d\n", ptr2); // 10
    return 0;
}   
```
## 1. 주소값, value
&a: a의 주소값. 
a : value
``` c
# include <stdio.h>

int main(void)
{
    // 포인터

    // [철수] 101호 -> 메모리 공간의 주소
    // [영희] 102호
    // [민수]
    int 철수 = 1; // 암호(val)
    int 영희 = 2;
    int 민수 = 3;
    printf("철수네 주소 : %p, 암호: %d\n", &철수, 철수); // 철수네 주소 : 0x16da534d8, 암호: 1
    printf("영희네 주소 : %p, 암호: %d\n", &영희, 영희);// 영희네 주소 : 0x16b26b4d4, 암호: 2
    printf("민수네 주소 : %p, 암호: %d\n", &민수, 민수); // 민수네 주소 : 0x16b26b4d0, 암호: 3
    return 0;
}   
```
## 2. 포인터의 등장! 

포인터 변수에는 메모리 주소가 저장되어 있습니다.  
이때 메모리 주소가 있는 곳으로 이동해서 값을 가져오고 싶다면 역참조(dereference) 연산자 *를 사용합니다.
``` c

# include <stdio.h>

int main(void)
{
    int 철수 = 1; // 암호(val)
    
    // 미션맨 (pointer)
    // 미션 : 아파트의 철수네 집에 방문하여 문에 적힌 암호 바꾸기
    int * 미션맨 ;
    미션맨 = &철수; // 미션맨 :
    * 미션맨 *= 3 ;
    printf("철수집 암호: %d\n", 철수); // 3으로 바뀜!
    
    
    // 스파이의 등장(또 다른 포인터)
    int * 스파이;
    스파이 = 미션맨; // 미션맨이 가르키는 주소를 스파이도 가르킴, 즉 두개의 포인터가 동일한 메모리 주소를 가르킴
    스파이 = &철수;
    * 스파이 -= 2; // 철수네 암호(1) -2 


    // 두개의 값은 동일
    printf("스파이가 바꾼 집 암호: %d\n", *스파이); // 1

    printf("철수집 암호: %d\n", 철수); // 1
 
    
    // Q. 철수 , 미션맨 , 스파이가 사는 곳은?
    
    printf("철수가 사는 곳의 주소: %p\n", &철수); // 철수가 사는 곳의 주소: 0x16f52b4d8
    
    printf("미션맨이 사는 곳의 주소: %p\n", &미션맨); // 미션맨이 사는 곳의 주소: 0x16f52b4c8
    
    printf("스파이가 사는 곳의 주소: %p\n", &스파이); // 스파이가 사는 곳의 주소: 0x16f52b4c0
    
    return 0;
}   
```
