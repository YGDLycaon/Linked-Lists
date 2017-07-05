class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None   
    
    def addNode(self,data):
        newNode=Node(data)

        if self.head==None:
            self.head=newNode
        
        if self.tail!=None:
            self.tail.next=newNode
        
        self.tail=newNode

    def removeNode(self,index):
        prev=None
        node=self.head
        i=0
        while (node!=None) and (i<index):
            prev=node
            node=node.next
            i+=1
        if prev==None:
            self.head=node.next
        else:
            prev.next=node.next

    def iterate(self):
        node=self.head
        while node!=None:
            print(node.data)
            node=node.next

    def checkCycle(node):
        marker1=node
        marker2=node
        while marker2 != None and marker2.next!=None:
            marker1=marker1.next
            marker2=marker2.next.next
            if marker1==marker2:
                return True
        return False


l=LinkedList()
l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(4)
l.iterate()
print("\n")
l.removeNode(1)
l.iterate()