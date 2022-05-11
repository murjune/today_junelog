# 피라미드를 쌓아라 - 프로젝트
```c
# include <stdio.h>
int main(void)
{   
    // 피라미드를 쌓아라 - 프로젝트
    /*
        *
       ***
      ******
     ********
    **********
    */

    int floor;
    printf("몇 층으로 쌓겠느냐?");
    scanf("%d", &floor);

    for(int i = 0 ; i < floor; i++)
    {   

        for(int blank = 1 ; blank < floor-i; blank++)
        {
            printf(" ");
        }
        
        for(int j = 0 ; j < 2*i + 1; j++)
        {
            printf("*");
        }
    printf("\n");
    }
    return 0;
}
```
