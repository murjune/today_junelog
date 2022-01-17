# Chapter 9 - 비밀 일기

```c
# include <stdio.h>
# include <string.h>
#include <termios.h>

#include <unistd.h>
# define Max 10000



// 비밀번호를 입력 받아서
// 맞는 경우는 비밀 일기를 읽어와서 보여주고, 계속 작성하도록 합니다.
// 틀린 경우는 경고 메세지를 표시하고, 종료합니다.
int getch(void);
int main(void)
{
    //fgets, fputs 활용
    char line[Max];// 파일에서 불러온 내용을 저장할 변수
    char contents[Max]; // 일기장에 입력할 내용
    char password[20]; // 비밀번호 입력
    char c; // 비밀번호 입력 할 때 키값 확인용[마스킹]

    printf("'비밀 일기'에 오신것을 환영합니다\n");
    printf("비밀번호를 입력하세요 : ");

    // getchar() vs getch()의 차이?
    // getchar() : 엔터를 입력받아야 동작을 합니다.
    // getch() : 키 입력 시 바로바로 동작을 합니다.
    int i = 0 ;
    while(1)
    {
        c = getch();
        // Enter -> 비밀번호 입력 종료
        if (c == 13) // Enter의 ASCII코드: 13
        {
            password[i] = '\0';
            break;
        }
        else // 비밀번호 입력중
        {
            printf("*");
            password[i] = c;
        }
        i++;
    }   
    // 비밀 번호 : 준원wnsdnjs
    printf(" === 비밀번호 확인 중..===");
    if (strcmp(password, "wnsdnjs") == 0) // 비밀번호 일치
    {
        printf("=== 비밀번호 확인 완료 ===");
        char * fileName = "c:\\secretdiary/txt";
        // "a+b": 파일이 없으면 생성, 없으면 append
        FILE * file = fopen(fileName, "a+b");
        if (file == NULL)
        {
            printf("파일 열기 실패\n");
            return 1;

        } 
        while(fgets(line, Max,file) != NULL)
        {
            printf("%s",line);
        }
        printf("\n\n 내용을 계속 작성하세요 ! 종료하시려면 EXIT를 입력하요!\n");

        while(1)
        {   
            // 새 줄(\n)이 나오기 전까지 읽어드림(한 문장씩)
            scanf("%[^\n]",contents);
            getchar(); // Enter 입력(\n) Flush 처리

            if(strcmp(contents, "EXIT") == 0)
            {
                printf("비밀 일기를 종료합니다.\n");
                break;
            }

            fputs(contents,file);
            // Enter를 위에서 무시처리 했으므로, 임의로 추가
            fputs("\n",file);
            
        }
        fclose(file);
    }
    else // 비밀번호 틀린 경우
    {
        printf("=== 비밀번호가 틀렸어요 ===\n");
        printf("너 누구야!! 감히 내 일기장을 !!!\n\n\n");

    }

     
    return 0;
}
int getch(void)

{

    struct termios oldt, newt;

    int ch;

    tcgetattr( STDIN_FILENO, &oldt );

    newt = oldt;

    newt.c_lflag &= ~( ICANON | ECHO );

    tcsetattr( STDIN_FILENO, TCSANOW, &newt );

    ch = getchar();

    tcsetattr( STDIN_FILENO, TCSANOW, &oldt );

    return ch;

}
```
