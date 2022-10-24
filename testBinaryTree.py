class Node:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data

def insert(node,data):
    #get node
    #compare node data if greater or less
        #move pointer to right if greater
        #move pointer to left if lesser
    pointer=node
    if pointer.data is None:
        pointer.data=data 
    elif pointer.data < data:
        if pointer.right is None:
            temp=Node(data)
            pointer.right=temp
        else:
            pointer=pointer.right
            insert(pointer,data)
    elif pointer.data >= data:
        if pointer.left is None:
            temp=Node(data)
            pointer.left=temp
        else:
            pointer=pointer.left
            insert(pointer,data)     

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

def run():
    root=Node(10)
    insert(root,5)
    insert(root,2)
    insert(root,8)
    insert(root,15)
    insert(root,12)
    insert(root,18)
    insert(root,13)
    insert(root,11)
    dfs(root)

run()
    
    