class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def printNodes(node: Node):
    currentNode = node
    while currentNode != Node:
        print(currentNode.value, end=" ")
        currentNode = currentNode.next

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def addBack(self, value):
        node = Node(value)
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = node
    
    def findNode(self, value):
        currentNode = self.head
        while currentNode:
            if currentNode.value == value:
                return currentNode
            currentNode = currentNode.next

        return RuntimeError('Node not found')
    
    def addAfter(self, node, value):
        newNode = Node(value)
        newNode.next = node.next
        node.next = newNode
    
    def deleteAfter(self, prevNode):
        if prevNode.next:
            prevNode.next = prevNode.next.next
        