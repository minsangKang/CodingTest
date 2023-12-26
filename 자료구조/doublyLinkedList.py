class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new
            new.prev = node
            self.tail = new

    def printNodes(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.next

    def searchFromHead(self, value):
        if self.head == None:
            return False
        
        node = self.head
        while node:
            if node.value == value:
                return node
            else:
                node = node.next

        return False
    
    def searchFromTail(self, value):
        if self.head == None:
            return False
        
        node = self.tail
        while node:
            if node.value == value:
                return node
            else:
                node = node.prev

        return False
    
    def insertBefore(self, value, beforeValue):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = new
            return True
        else:
            node = self.tail
            while node.value != beforeValue:
                node = node.prev
                if node == None:
                    return False
                
            if node.prev != None:
                beforeNew = node.prev
                beforeNew.next = new
                new.prev = beforeNew
                new.next = node
                node.prev = new
            else:
                new.next = node
                node.prev = new
                self.head = new
        
        return True
    
    def insertAfter(self, value, afterValue):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = new
            return True
        else:
            node = self.head
            while node.value != afterValue:
                node = node.next
                if node == None:
                    return False
                
            if node.next != None:
                nextNew = node.next
                nextNew.prev = new
                new.next = nextNew
                new.prev = node
                node.next = new
            else:
                new.prev = node
                node.next = new
                self.tail = new

            return True