# 프로젝트: 동물 뒤집기
``` c

# include <stdio.h>
# include <time.h>
# include <stdlib.h>
// 10마리의 서로 다른 동물 (각 카드당 2마리씩)
// 사용자로부터 2개의 입력을 받아서 -> 같은 동물 찾으면 뒤집기 
// 모든 동물의 쌍을 찾으면 종료
// 총 실패 횟수 알려주기 

// 전역 변수
int animal_graph[4][5];// 카드 지도 20장
char* animalName[10];
int visited[4][5];// 방문 처리 지도
// 함수
void initanimalArray();
void naming_animal();
void shuffleAnimal();
int getEmptyPos();
void printAnimal_all();
void printQuestion();
int findAll_animal();


int main(void)
{   
    srand(time(NULL));

    initanimalArray(); // 동물 맵 초기화
    naming_animal(); // 동물 이름 초기화

    // 게임 시작 전 동물 맵에 랜덤으로 동물들 배치
    shuffleAnimal();
    // 실패 횟수 초기화
    int failCount = 0;

    while(1)
    {
        int sel1 ; // 사용자가 선택한 첫번째 카드
        int sel2 ; // 사용자가 선택한 두번째 카드

        printAnimal_all();
        printQuestion(); // 문제 출력(카드 지도)
        printf("뒤집을 카드를 선택하시오: ");
        scanf("%d %d",&sel1, &sel2);

        if (sel1 == sel2) // 만약 선택한 두 카드 같으면 다시 뽑기!
        {
            continue;
        } 
        // 1. 좌표에 해당하는 카드를 뒤집어보고 같은지 안 같은지
        // 2. 이미 뒤집은 경우
        int sel1_x = sel1 / 5;
        int sel1_y = sel1 % 5;

        int sel2_x = sel2 / 5;
        int sel2_y = sel2 % 5;
        if (
            visited[sel1_x][sel1_y] == 0 &&
            visited[sel2_x][sel2_y] == 0 &&
            animal_graph[sel1_x][sel1_y] == animal_graph[sel2_x][sel2_y]
            
            )
        {
            printf("\n\n 빙고! : %s 발견\n\n", animalName[animal_graph[sel1_x][sel1_y]]);
            // 방문 처리
            visited[sel1_x][sel1_y] = 1;
            visited[sel2_x][sel2_y] = 1; 
        }
        else
        {
            printf("\n\n땡! 이미 뒤집힌 카드 or 틀렸습니다. \n\n");
            printf("%d : %s\n", sel1, animalName[animal_graph[sel1_x][sel1_y]]);
            printf("%d : %s\n", sel2, animalName[animal_graph[sel2_x][sel2_y]]);
            printf("\n\n");

            failCount++;
        }
        // 모든 동물을 찾았는지 여부
        if(findAll_animal() == 1)
        {
            printf("\n\n축하합니다. 모든 동물을 찾았습니다!\n");
            printf("지금까지 총 %d번 실수하셨습니다.",failCount);
            exit(0);
        }


    }
    
    

    return 0 ;
}

void initanimalArray()
{
    for(int i = 0 ; i <4 ; i++)
    {
        for(int j = 0; j < 5 ; j++)
        {
            animal_graph[i][j] = -1 ; // -1로 초기화시키기
        }
    }
}

void naming_animal()
{
    animalName[0] = "댕댕";
    animalName[1] = "양양";
    animalName[2] = "머일";
    animalName[3] = "참새";
    animalName[4] = "민멘";
    
    animalName[5] = "미노";
    animalName[6] = "머훈";
    animalName[7] = "토깽";
    animalName[8] = "둘기";
    animalName[9] = "숭숭";

}

void shuffleAnimal()
{
    for(int i = 0 ; i<10; i++)// 10마리 동물 중 1마리 뽑기
    {
        for(int j = 0 ; j < 2; j ++)// 2 빈공간 뽑기
        {
            int pos = getEmptyPos(); // 랜덤한 x,y좌표 뽑기
            int x = pos / 5;
            int y = pos % 5;
            animal_graph[x][y] = i; // 동물 번호 넣기
        }
    }
}

int getEmptyPos()
{   
    while(1)
    {
        int num = rand() % 20 ;

        int x = num / 5;
        int y = num % 5;
        if (animal_graph[x][y] ==-1) // 비어 있는 공간이라면 
        {
            return num;
        }
        // 이미 동물 번호가 차있다면 반복
    }
    
}

void printAnimal_all()
{   
    printf("\n===========답안지 ㅋㅋ==============\n\n");
     for(int i = 0 ; i <4 ; i++)
    {
        for(int j = 0; j < 5 ; j++)
        {
            printf("%8s", animalName[animal_graph[i][j]]);
        }
        printf("\n");
    }
    printf("\n============================================\n\n");
}

void printQuestion()
{   
    int seq = 0 ;
    for(int i = 0 ; i <4 ; i++)
    {
        for(int j = 0; j < 5 ; j++)
        {   
            // 방문 처리 안된 동물
            if (visited[i][j] != 0) 
            {
                printf("%8s",animalName[animal_graph[i][j]]);
                visited[i][j] = 1;
            }
            // 이미 뽑은 동물
            else
            {
                printf("%3d",seq);
            }
            
            seq++ ;
        }
        printf("\n");
    }
}

int findAll_animal()
{
    for(int i = 0 ; i <4 ; i++)
    {
        for(int j = 0; j < 5 ; j++)
        {
            if (visited[i][j] == 0)
            {
                return 0;
            }
        }
    }
    return 1;
}
```
