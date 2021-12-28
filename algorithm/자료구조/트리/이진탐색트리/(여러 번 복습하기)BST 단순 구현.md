# 해결해야 할 점

1. 만약 BST가 unbalanced한 점 
2. root를 모를 경우
3. root를 삭제할 경우
``` python

class Node():
    def __init__(self,value):
        self.node = value
        self.left = None
        self.right = None

class BST():
    def __init__(self, value):
        self.root = value

    def insert(self,value):
        self.now = self.root
        while True:

            if value < self.now.node:
                if self.now.left == None:
                    self.now.left = Node(value)

                    break
                else:
                    self.now = self.now.left
            else:
                if self.now.right == None:
                    self.now.right = Node(value)

                    break
                else:
                    self.now = self.now.right

    def search(self,value):
        self.now = self.root
        while self.now:
            if self.now.node == value:
                return True
            if value < self.now.node:
                self.now = self.now.left
            else:
                self.now = self.now.right
        return False

    def delete(self, value):
        self.now = self.root
        self.parent = None
        is_child_right = None
        flag = False
        while self.now:
            if self.now.node == value:
                flag = True
            elif self.now.node > value:
                self.parent = self.now
                self.now = self.now.left
                is_child_right = False
            else:
                self.parent = self.now
                self.now = self.now.right
                is_child_right = True
        if flag == False:
            print("트리 안에 해당 값이 없습니다.")
            return

        # 1. 자식이 없는 경우

        if not self.now.left and not self.now.right:
            if is_child_right:
                self.parent.right = None
            else:
                self.parent.left = None
        # 2. 자식이 하나 있는 경우

        # 1) 오른쪽 자식만 있는 경우
        if not self.now.left and self.now.right:
            if is_child_right:
                self.parent.right = self.now.right
            else:
                self.parent.left = self.now.right
        # 2) 왼쪽 자식만 있는 경우
        if self.now.left and not self.now.right:
            if is_child_right:
                self.parent.right = self.now.left
            else:
                self.parent.left = self.now.left
        # 3. 자식이 둘다 있는 경우
        if self.now.left and self.now.right:
            # now를 루트로 삼는 서브트리의 왼쪽트리의 가장 오른쪽에 위치한 노드를 now자리에 change
            self.change = self.now.left
            self.change_parent = self.now
            # 서브트리의 왼쪽트리의 가장 오른쪽에 위치한 노드 찾기
            while self.change:
                self.change_parent = self.change
                self.change = self.change.right
            # 1) 가장 오른쪽 노드가 왼쪽 자식을 갖을 경우
            # change의 왼쪽 자식이 change 자리에 들어간다.
            if self.change.left:
                self.change_parent.right = self.change.left

            # 2) 가장 오른쪽 노드가 왼쪽 자식을 갖지 않을 경우
            # change 삭제
            else:
                self.change_parent.right = None

            # 이제 change 노드를 now노드에 넣기

            if is_child_right:
                self.change_parent.right = self.change
                self.change.left = self.now.left
                self.change.right = self.now.right
            else:
                self.change_parent.left = self.change
                self.change.left = self.now.left
                self.change.right = self.now.right
        print("요청하신 값을 삭제하였습니다.")
        return
arr = [3,8,2,4,7,9,1,6,10]
root = Node(5)
bst = BST(root)
for i in arr:
    bst.insert(i)
print(bst.search(3)) # True
print(bst.search(4)) # True
print(bst.search(1)) # True
bst.delete(1) # 요청하신 값을 삭제하였습니다.
print(bst.search(6)) # None
bst.delete(3) # 요청하신 값을 삭제하였습니다.
bst.delete(8) # 요청하신 값을 삭제하였습니다.
bst.delete(11) # 삭제할 노드가 트리안에 존재하지 않습니다.
print(bst.search(3)) # None
print(bst.search(8)) # None

```
