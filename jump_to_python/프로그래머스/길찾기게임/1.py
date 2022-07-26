import sys
sys.setrecursionlimit(10**5)

class Node():
    def __init__(self, x, nodeNum):
        self.x = x
        self.nodeNum = nodeNum
        self.left = None
        self.right = None


class BST():

    def __init__(self):
        self.root = None
        self.preOrderList = []
        self.postOrderList = []

    def addNode(self, x: int, nodeNum):
        if self.root is None:
            self.root = Node(x, nodeNum)
            return

        now: Node = self.root

        while True:
            if x < now.x:
                if now.left == None:
                    now.left = Node(x, nodeNum)
                    break
                else:
                    now = now.left
            else:
                if now.right == None:
                    now.right = Node(x, nodeNum)
                    break
                else:
                    now = now.right
    def preOrder(self, now: Node):
        self.preOrderList.append(now.nodeNum)
        if now == None:
            return
        if now.left:
            self.preOrder(now.left)
        if now.right:
            self.preOrder(now.right)

    def postOrder(self, now: Node):
        if now == None:
            return
        if now.left:
            self.postOrder(now.left)
        if now.right:
            self.postOrder(now.right)
        self.postOrderList.append(now.nodeNum)
        
def solution(nodeinfo):
    graph = nodeinfo
    for i in range(len(graph)):
        graph[i].append(i+1)

    graph.sort(key= lambda x: -x[1])
    ans = []
    bst = BST()
    for node in graph:
        bst.addNode(node[0], node[2])
    bst.postOrder(bst.root)
    bst.preOrder(bst.root)
    ans.append(bst.preOrderList)
    ans.append(bst.postOrderList)
    return ans