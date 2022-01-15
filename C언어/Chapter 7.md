# Chapter 7 - 다차원 배열

## 1. 다차원 배열의 형태
``` c
# include <stdio.h>
# include <time.h>
# include <stdlib.h>

int main(void)
{   
    // 다차원 배열 Multidimensional Array
    int arr[4] = {1,2,3,4}; 

    // 이중 배열 ex
    int arr[2][4] = 
    {
        {1,2,3,4},
        {5,6,7,8}
    };
    
    // 삼중 배열 ex
    int arr[2][4][2]= // 2 x 4 x 2
    {
        { 
            {1,2},
            {2,3},
            {3,4},
            {4,5}

        },
        {
            {1,2},
            {2,3},
            {3,4},
            {4,5}
        }
    }
    

    return 0;
}  

```
## 2. 다차원 배열의 사용
``` c

# include <stdio.h>
# include <time.h>
# include <stdlib.h>

int main(void)
{   
    // 이중 배열 
    int arr[2][4] = 
    {
        {1,2,3,4},
        {5,6,7,8}
    };

    printf("이차원 배열 arr의 2행 3열 원소는 %d다.\n", arr[2-1][3-1]);
    // 이차원 배열 arr의 2행 3열 원소는 7다.
    // index는 0부터 시작하기 때문

    // 삼중 배열 
    int arr2[2][4][2]= // 2 x 4 x 2
    {
        { 
            {1,2},
            {2,3},
            {3,4},
            {4,5}

        },
        {
            {1,2},
            {2,3},
            {3,4},
            {4,5}
        }
    };
    printf("이차원 배열 arr의 좌표평면상 (x,y,z) = <0,3,1> 원소는 %d다.\n", arr2[0][3][1]);
    // 이차원 배열 arr의 좌표평면상 (x,y,z) = <0,3,1> 원소는 5다.
    return 0;
}  

```
