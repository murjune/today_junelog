# 문제: 물고기 키우기 게임
``` c

# include <stdio.h>
# include <time.h>
# include <stdlib.h>
// 물고기가 6마리가 있어요
// 이들은 어항에 살고 있는데, 사막이에요
// 물이 다 증발하기 전에 부지런히 어항에 물을 줘서 물고기를 살려주세요
// 물고기는 시간이 지날수록 점점 커져서 나중에는 맛있다~

int level ;// 전역 변수 처리
int arrayFish[6] ; //전역 변수 처리
int* cursor; // 어항의 물고기를 가르키는 포인터 변수

void initData();
void printf_Fishes();
void decreadeWater(long elapsedTime);
int checkFishAlive();
int main(void)
{   
    long startTime = 0; //게임 시작 시간
    long totalElapsedTime = 0;// 총 경과 시간
    long preElapsedTime = 0; // 직전 시간의 경과시간(최근에 물을 준 시간 간격)
    
    int num; // 몇 번 어항에 물을 줄 것인가

    initData(); // 게임 데이터 초기화
    
    cursor = arrayFish; 

    // 현재 시간을 millisecond(1000분의 1초)단위로 반환
    startTime = clock() ;
    
    while (1)
    {   
        // 물고기들의 상태를 보고해 주는 함수
        printf_Fishes();
        printf("\n몇 번 어항에 물을 주시겠어요? ");
        scanf("%d", &num);

        // 입력값 체크
        if(num < 1 || num > 6)
        {
            printf("\n입력값이 잘못되었습니다.\n");
            continue;
        }
        // 지금까지 총 경과 시간
        totalElapsedTime = (clock() - startTime)/ 100 ; // 1000으로 나누면 경과시간이 표기가 안됨;;
        printf("총 경과 시간: %ld초\n", totalElapsedTime);


        // 직전 물 준 시간(마지막으로 물을 준 시간)이후로 흐른 시간
        
        preElapsedTime = totalElapsedTime - preElapsedTime;
        printf("최근 경과 시간: %ld 초 \n\n", preElapsedTime);

        // 어항의 물을 감소 (증발)
        decreadeWater(preElapsedTime);

        // 사용자가 입력한 어항에 물을 준다
        // Case 1: 어항의 물이 0이라 이미 물고기가 죽음-> 물을 줄 필요가없음
        if(arrayFish[num-1] <= 0)
        {
            printf("%d번 물고기는 이미 죽었습니다.\n", num);
        }
        // Case 2: 어항의 물이 0이 아닌 걍우

        else if(arrayFish[num-1] +1 <= 100)
        {
            // 물을 준다
            printf("%d 번 어항에 물을 1만큼 줍니다.\n\n", num);
            cursor[num-1] += 1;
        }

        // 레벨업의 유무를 확인 (5초마다 한번씩 레벨업)
        if ((totalElapsedTime / 5) == level)
        {   
            //  레벨업
            level += 1;
            printf("*** 축 레벨업 ! 레벨%d -> 레벨%d로 승급! ***\n\n",level-1,level);

            if (level == 5)
            {
                printf("\n\n >>> 축하합니다! 게임을 클리어하셨습니다!!\n");
                exit(0);
            }
        }
        // 모든 물고기가 죽었는지 확인
        if (checkFishAlive()==0)
        {
            printf(">> 모든 물고기가 죽었습니다.. 실패!!\n");
            exit(0);
        }
        
        // 지금까지 지난 시간 기록
        preElapsedTime = totalElapsedTime;
    }

    return 0;
}  

void initData()
{
    level = 1; // 게임 레벨(1~5)
    for(int i = 0; i < 6; i ++)
    {
        arrayFish[i]= 100;// 어항의 물 최대 높이 (0~100)

    }
}

void printf_Fishes()
{   
    
    printf("%3d번 %3d번 %3d번 %3d번 %3d번 %3d번\n",1,2,3,4,5,6);
    for(int i = 0; i < 6 ; i++)
    {
        printf(" %4d ",arrayFish[i]);
    }
}

void decreadeWater(long elapsedTime)
{
    for(int i = 0; i < 6 ; i++)
    {   
        // 어항의 물이 빠지는 속도는 Level에 비례, 2는 상수
        arrayFish[i] -= (3* (level)  * (int)elapsedTime);

        // 만약 어항에 물이 마이너스 값을 갖게 된다면 0으로 초기화
        if (arrayFish[i] < 0)
        {
            arrayFish[i] = 0;

        }
    }

}
int checkFishAlive()
{
    for(int i = 0; i<6; i++)
    {
        if (arrayFish[i] != 0)
        {
            return 1;
        }
    }
    return 0;
    
}
```
출력 예시 값
```
  1번   2번   3번   4번   5번   6번
  100   100   100   100   100   100 
몇 번 어항에 물을 주시겠어요? 1
총 경과 시간: 0초
최근 경과 시간: 0 초 

  1번   2번   3번   4번   5번   6번
  100   100   100   100   100   100 
몇 번 어항에 물을 주시겠어요? 1
총 경과 시간: 1초
최근 경과 시간: 1 초 

1 번 어항에 물을 1만큼 줍니다.


  1번   2번   3번   4번   5번   6번
   90    90    89    88    88    88 
몇 번 어항에 물을 주시겠어요? 4
총 경과 시간: 4초
최근 경과 시간: 0 초 

4 번 어항에 물을 1만큼 줍니다.

  1번   2번   3번   4번   5번   6번
   90    90    89    89    88    88 
몇 번 어항에 물을 주시겠어요? 1
총 경과 시간: 5초
최근 경과 시간: 1 초 

1 번 어항에 물을 1만큼 줍니다.

*** 축 레벨업 ! 레벨1 -> 레벨2로 승급! ***

  1번   2번   3번   4번   5번   6번
   79    75    74    74    73    73 
몇 번 어항에 물을 주시겠어요? 1
총 경과 시간: 8초
최근 경과 시간: 1 초 

1 번 어항에 물을 1만큼 줍니다.

  1번   2번   3번   4번   5번   6번
   74    69    68    68    67    67 
몇 번 어항에 물을 주시겠어요? 1
총 경과 시간: 8초
최근 경과 시간: 0 초 

1 번 어항에 물을 1만큼 줍니다.

  1번   2번   3번   4번   5번   6번
   75    69    68    68    67    67 
몇 번 어항에 물을 주시겠어요? 
1
총 경과 시간: 9초
최근 경과 시간: 1 초 

1 번 어항에 물을 1만큼 줍니다.

  1번   2번   3번   4번   5번   6번
   70    63    62    62    61    61 
몇 번 어항에 물을 주시겠어요? 11

입력값이 잘못되었습니다.
  1번   2번   3번   4번   5번   6번
   70    63    62    62    61    61 
몇 번 어항에 물을 주시겠어요? 1
총 경과 시간: 11초
최근 경과 시간: 2 초 

1 번 어항에 물을 1만큼 줍니다.

*** 축 레벨업 ! 레벨2 -> 레벨3로 승급! ***

  1번   2번   3번   4번   5번   6번
   59    51    50    50    49    49 
몇 번 어항에 물을 주시겠어요? 
1
총 경과 시간: 11초
최근 경과 시간: 0 초 

1 번 어항에 물을 1만큼 줍니다.

  1번   2번   3번   4번   5번   6번
   60    51    50    50    49    49 
몇 번 어항에 물을 주시겠어요? 11

입력값이 잘못되었습니다.
  1번   2번   3번   4번   5번   6번
   60    51    50    50    49    49 
몇 번 어항에 물을 주시겠어요? 1


1번 물고기는 이미 죽었습니다.
>> 모든 물고기가 죽었습니다.. 실패!!
```
