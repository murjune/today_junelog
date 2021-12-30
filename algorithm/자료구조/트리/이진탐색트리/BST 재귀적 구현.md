# BST 소스코드 Ver. 1

## BST_ Search, Insert
``` python
class Node(object):
    def __init__(self, data):
        self.node = data
        self.left = self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        # data 삽입 재귀함수 실행
        self.root = self.insert_value(self.root, data)
        return

    def insert_value(self, now, data):

        if now == None:
            now = Node(data)
            return now
        else:
            if data < now.node:
                now.left = self.insert_value(now.left, data)
            else:
                now.right = self.insert_value(now.right, data)
        return now

    def search(self,data):

        is_search = self.search_value(self.root,data)
        return is_search

    def search_value(self,now,data):

        if now == None:
            return False
        if now.node == data:
            return True
        elif now.node > data:
            return self.search_value(now.left,data)
        else:
            return self.search_value(now.right,data)

# 입력 예시
arr = [5, 3,8,2,4,7,9,1,6,10]

bst = BST()
print(bst.search(1)) # False
for i in arr:
    bst.insert(i)
print(bst.search(1)) # True
print(bst.search(2)) # True

```

## BST_ delete 
``` python

```
