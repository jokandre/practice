

class myLinkedList():
    """
    Interface:
    - addFirst(node)
    - addLast(node)
    - __iter__: for list traversal
    - removeFirst()
    - removeLast
    - addAt(index, node)
    - removeAt(index)
    """

    def __init__(self):
        self.head = None
        # self.size = 0

    def __repr__(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        counter = 0
        for _ in self:
            counter += 1
        return counter

    def addFirst(self, node):
        node.next = self.head
        self.head = node
        # self.size +=1

    def addLast(self, node):
        if not self.head:
            self.head = node
            return

        tempNode = self.head
        for tempNode in self:  # uses __iter__ to go to last node
            pass
        tempNode.next = node
        # self.size +=1

    def removeFirst(self):
        if not self.head:
            return
        self.head = self.head.next
        # self.size -=1

    def removeLast(self):
        if not self.head or not self.head.next:
            return
        tempNode = self.head
        while tempNode.next.next:
            tempNode = tempNode.next
        tempNode.next = None
        # self.size -=1

    def addAt(self, index, node):
        # print(self.size)
        if not self.head or 0 < index >= len(self): return 
        tempNode = self.head
        prevNode = None
        for _ in range(index):
            prevNode = tempNode
            tempNode = tempNode.next
        # print(prevNode, tempNode, tempNode.next)
        node.next = tempNode
        prevNode.next = node

    def removeAt(self, index):
        if not self.head or 0 < index >= len(self): return
        if index == 0: 
            self.removeFirst() 
            return 

        tempNode = self.head
        prevNode = None
        for _ in range(index):
            prevNode = tempNode
            tempNode = tempNode.next
        
        print(prevNode, tempNode, tempNode.next)
        prevNode.next = tempNode.next
        

class myNode:
    """
    Interface:
    - 
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


if __name__ == "__main__":
    linked = myLinkedList()
    print(linked)
    linked.head = myNode('a')
    linked.head.next = myNode('b')
    print(linked)

    for node in linked:
        print('yield:', node)

    linked.addFirst(myNode('first'))
    linked.addLast(myNode('last'))
    print(linked, len(linked))
    linked.removeFirst()
    linked.removeLast()
    print(linked)
    linked.addAt(1, myNode('mid1'))
    linked.addAt(2, myNode('mid2'))
    linked.addAt(2, myNode('mid'))
    print(linked)
    linked.removeAt(4)
    linked.removeAt(0)
    print(linked)
    