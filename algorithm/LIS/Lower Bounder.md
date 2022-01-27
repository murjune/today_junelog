[출처](https://seungkwan.tistory.com/8)
# Lower bound


어떠한 정렬된 배열 arr에서 어떠한 값 val의 lower bound란 arr을 정렬된 상태로 유지하면서 val이 삽입될 수 있는 위치들 중 가장 인덱스가 작은 것입니다.  

가령 [1, 3, 3, 6, 7] 이라는 배열에서 1의 lower bound는 1이고, 3의 lower bound는 2 이며, 5의 lower bound는 4입니다. (이 글에서 배열의 인덱스는 1부터 시작한다는 것에 유의해주세요).  
또한 upper bound라는 개념도 있는데, 이것은 반대로 삽입될 수 있는 위치들 중 가장 인덱스가 큰 것입니다.

lower bound는 이진 탐색을 통해 log N 시간에 구할 수 있으며, Python은 bisect_left를 통해 구할 수 있다.
