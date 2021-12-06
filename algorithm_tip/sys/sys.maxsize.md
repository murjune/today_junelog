# 꿀팁

보통 최솟값이나 최댓값을 구하기 위해 초깃값을 Min = 10**8 , Max = -10**8 이런식으로 표기했지만  

다음과 같이 import모듈의 maxsize모듈을 이용하면 편하다.
``` python
import sys

Min = sys.maxsize
Min = -sys.maxsize
```
