# 프로젝트 
경찰관이 범죄자의 정보를 입수 (조서 작성)  
이름? 나이? 몸무게? 키? 범죄명?
``` c
#include <stdio.h>
 
int main()
{   
    // 1. 이름
    char name[256]; 
    printf("이름이 뭐에요?");
    scanf("%s", name, sizeof(name));
    

    // 2. 나이
    int age;
    printf("몇살이에요?");
    scanf("%d",&age);

    // 3. 몸무게

    float weight;
    printf("몸무게는 몇 kg 이예요?");
    scanf("%f", &weight);
    
    // 4.키
    double height ;
    printf("키는 몇 cm 이에요?");
    scanf("%lf", &height);
    
    // 5. 죄목

    char what[256];
    printf("죄목이 뭐에요?");
    scanf("%s", what, sizeof(what));

    // 조서 내용 출럭
    printf("\n\n-- 범죄자 정보 --\n\n");
    printf("이름    : %s\n", name);
    printf("나이    : %d\n", age);
    printf("몸무게    : %.2f\n", weight);
    printf("키    : %.2lf\n", height);
    printf("죄목    : %s\n", what);


    return 0;
}
```

실행 결과  
```
이름이 뭐에요?이준원
몇살이에요?26
몸무게는 몇 kg 이예요?79.1
키는 몇 cm 이에요?181.3
죄목이 뭐에요?나는대단하다


-- 범죄자 정보 --

이름    : 이준원
나이    : 26
몸무게    : 79.10
키    : 181.30
죄목    : 나는대단하다
```
