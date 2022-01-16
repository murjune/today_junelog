# Chapter 8: 구조체

## 1. 구조체의 기본

```c

# include <stdio.h>


struct Gameinfo
{	
	//[게임 출시]
	// 게임 이름: 나도 게임
	// 발매년도: 2017년
	// 가격 : 50원
	// 제작사 : 나도회사
	char * game ;
	int year ;
	int price ;
	char *company ; 	
};

int main(void)
{	
	// 구조체 사용
	struct Gameinfo gameinfo1;
	gameinfo1.game = "나도게임";
	gameinfo1.year = 2017;
	gameinfo1.price = 50;
	gameinfo1.company = "나도 회사";
	
	// 구조체 출력
	printf("== 게임 출시 정보 == \n");
	printf("게임 명: %s\n", gameinfo1.game) ;
	printf("출시 연도:%d\n",gameinfo1.year) ;
	printf("게임 가격:%d\n",gameinfo1.price) ;
	printf("게임 회사: %s\n",gameinfo1.company) ;
	
	// 출력 결과
	/*
	== 게임 출시 정보 ==
	게임 명: 나도게임
	출시 연도:2017
	게임 가격:50
	게임 회사: 나도 회사
	*/ 
```
## 2. 구조체 배열
```c
// 구조체를 배열처럼 초기화 
	struct Gameinfo gameinfo2 = {"나도게임",2018,70,"나도회사"};
	printf("== 게임 출시 정보 == \n");
	printf("게임 명: %s\n", gameinfo2.game) ;
	printf("출시 연도:%d\n",gameinfo2.year) ;
	printf("게임 가격:%d\n",gameinfo2.price) ;
	printf("게임 회사: %s\n",gameinfo2.company) ;
```
구조체를 배열처럼 사용할 수도 있다.
```c
// 구조체 배열 
	struct Gameinfo gameArray[2]= {
		{"나도게임1",2018,70,"나도회사"},
		{"나도게임2",2020,100,"나도회사"}
		
	}; 
```
## 3. 구조체 포인터
```c

# include <stdio.h>


struct Gameinfo
{	
	//[게임 출시]
	// 게임 이름: 나도 게임
	// 발매년도: 2017년
	// 가격 : 50원
	// 제작사 : 나도회사
	char * game ;
	int year ;
	int price ;
	char *company ; 	
};

int main(void)
{	
	// 구조체 사용
	struct Gameinfo gameinfo1;
	gameinfo1.game = "나도게임";
	gameinfo1.year = 2017;
	gameinfo1.price = 50;
	gameinfo1.company = "나도 회사";
	
	// 구조체 출력// 
	printf("\n\n== 게임 출시 정보 == \n");
	printf("게임 명: %s\n", gameinfo1.game) ;
	printf("출시 연도:%d\n",gameinfo1.year) ;
	printf("게임 가격:%d\n",gameinfo1.price) ;
	printf("게임 회사: %s\n",gameinfo1.company) ;

	// 구조체 포인터
	
	struct Gameinfo* gamePtr; // 포인터
	 
	gamePtr = &gameinfo1;//
	
	printf("\n\n== 포인터의 게임 출시 정보 == \n");
	printf("게임 명: %s\n", (*gamePtr).game) ;
	printf("출시 연도:%d\n",(*gamePtr).year) ;
	printf("게임 가격:%d\n",(*gamePtr).price) ;
	printf("게임 회사: %s\n",(*gamePtr).company) ;
	
	// 출력결과 
	/*
	== 게임 출시 정보 ==
	게임 명: 나도게임
		출시 연도:2017
	게임 가격:50
	게임 회사: 나도 회사
	
	
	== 포인터의 게임 출시 정보 ==
	게임 명: 나도게임
	출시 연도:2017
	게임 가격:50
	게임 회사: 나도 회사
	*/
	
	return 0;
 } 


```
이때, 구조체의 포인터는 간단하게 다음과 같이 나타낼 수 있다.(->)
```c
struct Gameinfo* gamePtr; // 포인터
	 
	gamePtr = &gameinfo1;//
	
	printf("\n\n== 포인터의 게임 출시 정보 == \n");
	printf("게임 명: %s\n", gamePtr->game) ; 
	printf("출시 연도:%d\n",gamePtr->year) ;
	printf("게임 가격:%d\n",gamePtr->price) ;
	printf("게임 회사: %s\n",gamePtr->company) ;
```
## 4. 구조체안의 구조체
```c

# include <stdio.h>


struct Gameinfo
{	
	//[게임 출시]
	// 게임 이름: 나도 게임
	// 발매년도: 2017년
	// 가격 : 50원
	// 제작사 : 나도회사
	char * game ;
	int year ;
	int price ;
	char *company ; 	
	
	
	struct Gameinfo *friendGame; // 연관 업체 게임 소개 
	
	   
};

int main(void)
{	
	// 구조체 사용
	struct Gameinfo gameinfo1;
	gameinfo1.game = "나도게임";
	gameinfo1.year = 2017;
	gameinfo1.price = 50;
	gameinfo1.company = "나도 회사";
	// 배열 구조체 
	struct Gameinfo gameinfo2 = {"나도게임",2018,70,"너도회사"};
	
	// 연관 업체 게임소개  
	gameinfo1.friendGame = &gameinfo2;
	
	printf("\n\n== 연관 업체의 게임출시 정보 == \n");
	printf("게임 명: %s\n", gameinfo1.friendGame->game) ;
	printf("출시 연도:%d\n",gameinfo1.friendGame->year) ;
	printf("게임 가격:%d\n",gameinfo1.friendGame->price) ;
	printf("게임 회사: %s\n",gameinfo1.friendGame->company) ;
	
	// 출력 결과
	/*
	== 연관 업체의 게임출시 정보 ==
	게임 명: 나도게임
	출시 연도:2018
	게임 가격:70
	게임 회사: 너도회사
	*/ 
	return 0;    
 }        

```

## 5. typedef

```c
// typedef
	// 자료형에 별명 지정
	int i = 1; 
	typedef int d; 
	typedef float f;
	d d1 = 3; // int i = 3; 
	f f1 = 3.34f; // float f = 3.34;
	printf("정수 변수 : %d 실수 변수 : %.2f\n", d1, f1);
	// 정수 변수 : 3 실수 변수 : 3.34
```
