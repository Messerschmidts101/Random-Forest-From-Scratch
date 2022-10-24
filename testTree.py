from dataclasses import dataclass


class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data

def dfs(node):
    print(node.data)
    if node.left is not None:
        dfs(node.left)  
    if node.right is not None:
        dfs(node.right)

def bfs(node):
    queue=[]
    queuedata=[]
    queue.append(node)
    queuedata.append(node.data)
    while len(queue) > 0:
        node=queue.pop(0)
        print(node.data)
        if node.left is not None:
            queue.append(node.left)
            queuedata.append(node.left.data)
        if node.right is not None:
            queue.append(node.right)
            queuedata.append(node.right.data)

def autoinsert():
    root=Node("*")
    
    A=Node('A')
    root.left=A

    B=Node('B')
    root.right=B

    C=Node('C')
    A.left=C

    D=Node('D')
    A.right=D

    E=Node('E')
    B.left=E
    
    F=Node('F')
    B.right=F

    G=Node('G')
    C.left=G

    H=Node('H')
    C.right=H

    I=Node('I')
    D.left=I

    J=Node('J')
    D.right=J

    K=Node('K')
    E.left=K

    L=Node('L')
    E.right=L

    M=Node('M')
    F.left=M

    N=Node('N')
    F.right=N

    print("~~~DFS~~~")
    dfs(root)
    print("~~~BFS~~~")
    bfs(root)

autoinsert()