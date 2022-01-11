# Up and Down
``` c
# include <time.h>
# include <stdlib.h>
# include <stdio.h>

int main(void)
{   
    // Up and Down
    srand(time(NULL));
    int num = rand() % 100 + 1;// 1~100 사이의 숫자
    printf("숫자:%d\n", num);
    int ans ;
    int Chance = 5;
    
    while (Chance > 0)
        {
            printf("남은 기회 %d번 \n", Chance--);
            printf("숫자를 맞춰 보세요 (1~100) :");
            scanf("%d", &ans);

            if (ans > num)
                {
                    printf("Down\n");
                }
            else if (ans < num)
                {
                    printf("Up\n");
                }
            else if (ans == num)
                {
                    printf("정답입니다! 축하드려요\n"); 
                    break;
                }
            if (Chance == 0)
                {
                printf("모든 기회를 다 사용하셨습니다. 실패!\n");
                }
            
        }
    
    

    return 0;
}
```
# 출력 예시
```
숫자:69
남은 기회 5번 
숫자를 맞춰 보세요 (1~100) :40
Up

남은 기회 4번 
숫자를 맞춰 보세요 (1~100) :70
Down

남은 기회 3번 
숫자를 맞춰 보세요 (1~100) :60
Up

남은 기회 2번 
숫자를 맞춰 보세요 (1~100) :65
Up

남은 기회 1번 
숫자를 맞춰 보세요 (1~100) :68
Up

모든 기회를 다 사용하셨습니다. 실패!
```
