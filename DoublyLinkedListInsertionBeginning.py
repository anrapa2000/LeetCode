class DoublyLinkedListNode():
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data

def insertBeginninng(head, val):
        newNode = DoublyLinkedListNode(val)
        newNode.next = head
        newNode.prev = None
        head.prev = newNode
        return newNode

def printList(head):
    current = head
    while current is not None:
        print(current.data) 
        current = current.next

head = DoublyLinkedListNode(2)
head.next = DoublyLinkedListNode(3)
head.next.next = DoublyLinkedListNode(4)

value = insertBeginninng(head, 5)
print(value.data)
head = value
printList(head)
