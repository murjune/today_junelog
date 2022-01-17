# Chapter 9 - 파일 입출력

# fputs , fgets -> 문자열 저장
## 1. file 생성 및 쓰기 - fputs
```c
# include <stdio.h>
# define Max 10000
int main(void)
{
    // 파일 입출력
    // 파일에 어떤 데이터를 저장
    // 파일에 저장된 데이터 불러오기

    // fputs, fgets 한 쌍
    char line[Max]; // char line[10000]와 동치
    FILE * file = fopen("c:\\test3.txt","wb");
    if (file == NULL)
    {
        printf("파일 열기 실패\n");
        return 1;
    }
    fputs("fputs를 이용해서 글을 적어볼게요.\n", file);
    fputs("잘 적히는지 확인해주세요\n", file);
    

    // 파일을 열고 나서 닫지 않은 상태에서 어떤 프로그램에 문제가 생기면?
    // 데이터 손실 발생 가능 ! 그래서 항상 파일을 닫아주는 습관을 들여주세요!
    
    fclose(file);
    // scanf ,printf 한 쌍

    return 0;
}
```
## 2. 파일 읽기 - fgets
```c
# include <stdio.h>
# define Max 10000
int main(void)
{
    // 파일 입출력
    // 파일에 어떤 데이터를 저장
    // 파일에 저장된 데이터 불러오기

    // 파일 읽기
    char line[Max]; // char line[10000]와 동치
    FILE * file = fopen("c:\\test3.txt","rb");
    if (file == NULL)
    {
        printf("파일 열기 실패\n");
        return 1;
    }
    
    while(fgets(line, Max, file ) != NULL)
    {
        printf("%s",line);
    }
    // fputs를 이용해서 글을 적어볼게요.
    // 잘 적히는지 확인해주세요
    fclose(file);





    return 0;
}
```
# fscanf, fprintf -> 

## 1. file 생성 및 쓰기 - fprintf
```c
# include <stdio.h>
# define Max 10000
int main(void)
{
    // fprintf, fscanf

    int num[6] = {0,0,0,0,0,0}; // 추첨번호
    int bonus = 0; // 보너스 번호
    
    char str1[Max];
    char str2[Max];
    FILE * file  = fopen("c:\\test2.txt","wb");
    if (file == NULL) 
    {
        printf("파일 열기 실패\n");
        return 1;
    }

    // 로또 추첨 번호 저장
    fprintf(file, "%s %d %d %d %d %d %d\n", "추첨번호 ", 1,2,3,4,5,6);
    fprintf(file, "%s %d\n", "보너스 번호 ", 0);


    fclose(file);
    return 0;
}
```
## 2. 파일 읽기 - fscanf
```c
# include <stdio.h>
# define Max 10000
int main(void)
{
    // fscanf
    int num[6] ; // 추첨번호
    int bonus ; // 보너스 번호
    
    char str1[Max];
    char str2[Max];
   
    FILE * file  = fopen("c:\\test2.txt","rb");
    if (file == NULL) 
    {
        printf("파일 열기 실패\n");
        return 1;
    }

    fscanf(file, "%s %d %d %d %d %d %d ",
    str1,&num[0],&num[1],&num[2],&num[3],&num[4],&num[5]);
    printf("%s %d %d %d %d %d %d \n",
    str1,num[0],num[1],num[2],num[3],num[4],num[5]);

    fscanf(file, "%s %d",str2,&bonus);
    printf("%s %d\n",str2,bonus);
    
    fclose(file);
    return 0;
}
```

