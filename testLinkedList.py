class Node:
    def __init__(self,data) -> None:
        self.next=None
        self.data=data
def traverse(node):
    print("self self: ", node)
    print("self data: ", node.data)
    print("self next: ", node.next)
    if (node.next!=None):
        traverse(node.next)
    else:
        print("End of the line")
def insert(node,answer1):#inserts at end
    pointer=node
    if pointer.data is None:
        head.data=answer1
    elif pointer.next is not None:
        insert(pointer.next,answer1)
    else:
        print("None")
        tempnode=Node(0)
        tempnode.data=answer1
        tempnode.next=None
        pointer.next=tempnode
head=Node(0)
head.data=None
head.next=None
while True:
    answer=int(input("What would you like to do?: \n[1] Add Node\n[2] See Nodes\n[3] Exit\n"))
    if answer==1:
        answer1=int(input("Type your number?:"))
        insert(head,answer1)
    elif answer==2:
        print("**********")
        traverse(head)
    elif answer==3:
        print("Goodbye")
        break
    else:
        print("Unidentified input")