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
## 3. 배열과 포인터의 관계

### 예제 1
```c

# include <stdio.h>

int main(void)
{
    // 배열과 포인터의 관계
    int arr[3] = {5,10,15};
    int* ptr = arr; // 포인터가 arr배열을 가르침

    for(int i = 1 ; i<3; i++ )
    {
        printf("배열 arr[%d]의 값 : %d\n", i , arr[i]);
    }

    for(int i = 1 ; i<3; i++ )
    {
        printf("포인터 ptr[%d]의 값 : %d\n", i , ptr[i]);
    }
    return 0;

    /* 출력값 동일!!

    배열 arr[1]의 값 : 10
    배열 arr[2]의 값 : 15
    포인터 ptr[1]의 값 : 10
    포인터 ptr[2]의 값 : 15
    */
}   
```

### 예제 2
위에 예제 ptr, arr과 같음 가정
```c
ptr[0] = 10;
ptr[1] = 20;
ptr[2] = 30;

for(int i = 0 ; i<3; i++ )
{
    printf("배열 arr[%d]의 값 : %d\n", i , arr[i]);
}

for(int i = 0 ; i<3; i++ )
{
    printf("포인터 ptr[%d]의 값 : %d\n", i , ptr[i]);
}

/*
배열 arr[0]의 값 : 10
배열 arr[1]의 값 : 20
배열 arr[2]의 값 : 30
포인터 ptr[0]의 값 : 10
포인터 ptr[1]의 값 : 20
포인터 ptr[2]의 값 : 30
*/

```
즉, 위의 예제를 통해 ptr 과 arr는 같다는 결과를 도출해낼 수 있다.  

추가로 위의 예제를 아래와 같이 나타낼수도 있다.
``` c

ptr[0] = 10;
ptr[1] = 20;
ptr[2] = 30;

for(int i = 0 ; i<3; i++ )
{
    // printf("배열 arr[%d]의 값 : %d\n", i , arr[i]);
    printf("배열 arr[%d]의 값 : %d\n", i , *(arr + i));
}

for(int i = 0 ; i<3; i++ )
{
    printf("포인터 ptr[%d]의 값 : %d\n", i , *(ptr + i));
}
return 0;
/*
배열 arr[0]의 값 : 10
배열 arr[1]의 값 : 20
배열 arr[2]의 값 : 30
포인터 ptr[0]의 값 : 10
포인터 ptr[1]의 값 : 20
포인터 ptr[2]의 값 : 30
*/
```
이를 통해 알아낸 점
- *(arr +i)는 arr[i]와 동일한 표현  
- 즉, arr = arr 배열의 첫번째 값의 주소와 동일 = &arr[0]  

다음 예제를 보며, 이를 증명하자.
```c
printf("arr 자체의 값: %p\n", arr);
printf("arr[0]의 주소: %p\n", &arr[0]);

printf("arr 자체의 값이 가지는 주소의 실제 값: %d\n", *arr);
printf("arr 자체의 값: %d\n", *&arr[0]);

/*
arr 자체의 값: 0x16baab4c8
arr[0]의 주소: 0x16baab4c8
arr 자체의 값이 가지는 주소의 실제 값: 10
arr 자체의 값: 10
*/
```  
즉, 우리는 다음을 알 수 있다.  
- *&는 아무것도 없는 것과 같다.  
- &는 주소이면, *은 그 주소의 값이기 때문에   
- *&는 상쇄된다.  

이 또한, 예제로 확인!
```c
printf("arr[0]의 실제 값 : %d\n", *&*&*&*&*&arr[0]);
printf("arr[0]의 실제 값 : %d\n", arr[0]);

//arr[0]의 실제 값 : 10
//arr[0]의 실제 값 : 10
```
### 4. swap

``` c

# include <stdio.h>

int main(void)
{   
    // swap 전
    int a = 10;
    int b = 20;
    printf("a, b : %d, %d\n", a, b);
    // a, b : 10, 20

    // swap
    int tmp;
    tmp = b;
    b = a;
    a = tmp;

    // swap 후
    printf("a, b : %d, %d\n", a, b);
    a, b : 20, 10
    
    return 0;
}   
```

## 5. 포인터로 배열 값 변경하기

``` c

# include <stdio.h>
void changeArray(int* ptr);
int main(void)
{   
    // swap 전
    int arr[3] = {1,2,3};
    changeArray(arr);
    for (int i = 0; i < 3; i++)
    {
        printf("%d\n", arr[i]);
    }
    return 0;
}   

void changeArray(int* ptr)
{
    *(ptr + 2) = 50; // ptr[2] = 50과 같은 표현

}
```
이떄, 
```c
changeArray(arr); 
```
이거 대신 아래와 같이 표현해도 동일하다.
```c
changeArray(&arr[0]);
```
