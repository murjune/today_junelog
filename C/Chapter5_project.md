# 프로젝트 : 아빠의 대머리 
``` c
# include <stdio.h>
# include <time.h>
# include <stdlib.h>
int main(void)
{   
    srand(time(NULL));
    int ans ;
    int treatment = rand() % 4 ; // 발모제
    int now_showBottle = 0; // 현재 선택한 발모제 개수
    int pre_showBottle = 0; // 전에 선택한 발모제 개수

    printf("===========아빠의 대머리 게임을 시작===========\n\n");
    // 3번의 기회
    for(int i = 0; i <3; i ++){
        
        printf("%d번째 시도: ", i+1);
        int bottle[] = {0,0,0,0};
        now_showBottle = rand() % 2 + 2; // 2개 or 3개

        // 이전에 보여준 병의 개수와 다르게
        if (now_showBottle == pre_showBottle)
        { 
            if (now_showBottle == 3)
            {
                now_showBottle = 2;
            }
            else 
            {
                now_showBottle = 3;
            
            }
        }
        // pre에 now값 넣어주기
        pre_showBottle = now_showBottle;
        
        // 선택할 bottle 고르기
        for(int j = 0 ; j < now_showBottle; j ++)
        {

            int selectBottle = rand() % 4 ;

            // 아직 고르지 않은 병은 고르기
            if (bottle[selectBottle] == 0)
            {
                bottle[selectBottle] = 1 ; 
            }
            else
            {
                j -= 1;
            }
        }
        // 사용자에게 몇번 병을 썼는지 보여줌
        for(int k = 0 ; k < 4; k ++)
        {
            if (bottle[k] == 1)
            {
                printf("%d번 ", k+1);
            }
        }
        printf("물약을 머리에 바릅니다!\n");
        // 고른 병들 중 발모제가 있는지 확인
        if (bottle[treatment] == 1)
        {
            printf("\n>>>>>아빠의 머리가 자라납니다!\n");
        }
        else
        {
            printf("\n>>>>>아빠의 머리가 자라나지 않았습니다.\n");  
        }
        
        printf("\n....계속하시려면 아무 버튼이나 눌러주세요....\n\n");
        getchar();
    }

    printf("\n\n 발모제는 몇번 일까요? ");

    scanf("%d", &ans );
    if (ans == treatment+1)
    {
        printf(">>>>>>정답입니다!<<<<<<\n");
    }
    else
    {
        printf(">>>>>>>>>땡!<<<<<<<<<!\n");
    }
    
    return 0;
}   

```
# 출력 예시
```
===========아빠의 대머리 게임을 시작===========

1번째 시도: 1번 2번 물약을 머리에 바릅니다!

>>>>>아빠의 머리가 자라납니다!

....계속하시려면 아무 버튼이나 눌러주세요....


2번째 시도: 2번 3번 4번 물약을 머리에 바릅니다!

>>>>>아빠의 머리가 자라나지 않았습니다.

....계속하시려면 아무 버튼이나 눌러주세요....


3번째 시도: 2번 3번 물약을 머리에 바릅니다!

>>>>>아빠의 머리가 자라나지 않았습니다.

....계속하시려면 아무 버튼이나 눌러주세요....




 발모제는 몇번 일까요? 1
>>>>>>정답입니다!<<<<<<
```
