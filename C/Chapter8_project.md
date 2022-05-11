# Chapter 8 : 너, 내 집사가 되어라

```c

# include <stdio.h>
# include <time.h>
# include <stdlib.h>
// 다섯 마리의 고양이가 있다.
// 아무 키나 눌러서 랜덤으로 고양이를 뽑되,
// 5마리를 모두 뽑아서 열심히 키우면 된다!
// 중복 가능~

// 고양이
// 이름, 나이, 성격, 키우기 난이도(레벨)

typedef struct{
    char* name;
    int age;
    char* character;
    int level;// 1~5

}Cat;

// 지금까지 소유한 고양이
int collection[5] = {0,0,0,0,0};
// 전체 고양이 리스트
Cat cats[5];

// 함수
void init_Catinfo();
void printCat(int idx);
int checkcollection();
int main(void)
{
    srand(time(NULL));
    
    // 고양이 정보 초기화
    init_Catinfo();

    while(1)
    {
        printf("두근두근~! 어느 고양이의 집사가 될까요??\n 아무 키나 눌러서 확인해보세요!");
        getchar();

        // 고양이 뽑기
        int selected = rand() % 5;
        // 뽑은 고양이 정보 출력
        printCat(selected);
        // 뽑은 고양이 수집 처리
        collection[selected] = 1;

        // 지금까지 몇마리의 고양이를 수집하였는가?
        if (checkcollection() == 5)
        {
            printf("\n\n축하합니다!! 모든 고양이를 모두 모았어요!!\n\n");
            exit(0);
        }



        


    }



    return 0 ;
}
void init_Catinfo()
{
    cats[0].name = "냥냥이";
    cats[0].age = 2;
    cats[0].character = "귀여움";
    cats[0].level = 2;

    cats[1].name = "귀요미";
    cats[1].age = 2;
    cats[1].character = "애교가 많음";
    cats[1].level = 3;

    cats[2].name = "까칠이";
    cats[2].age = 5;
    cats[2].character = "까칠함";
    cats[2].level = 5;

    cats[3].name = "돼냥이";
    cats[3].age = 3;
    cats[3].character = "먹는걸좋아함";
    cats[3].level = 1;

    cats[4].name = "머일이";
    cats[4].age = 26;
    cats[4].character = "박종원을 좋아함";
    cats[4].level = 4;
    
}

void printCat(int idx)
{
    printf("\n\n====당신이 이 고양이의 주인이 되었어요!====\n\n");
    printf("이름     : %s\n",cats[idx].name);
    printf("나이     : %d\n", cats[idx].age);
    printf("성격     : %s\n", cats[idx].character);
    printf("레벨     : %d\n\n",cats[idx].level);
    
}

int checkcollection()
{
    printf("\n\n==== 지금까지 보유한 고양이 목록이에요 ===\n\n");
    int cnt = 0;

    for(int i = 0; i < 5 ; i++)
    {
        if (collection[i] == 1)
        {
            cnt += 1;
            printf("%10s",cats[i].name);
        }
        else
        {
            printf("%10s","(빈 박스)");

        }
    }
    printf("\n==================================\n\n");

    return cnt;
}
```
