class DoublyLinkedListNode:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


def insertEnding(head, val):
    newNode = DoublyLinkedListNode(val)
    newNode.next = None
    if head is None:
        head = newNode
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = newNode
        newNode.prev = current
    return head


def printList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


head = DoublyLinkedListNode(2)
head.next = DoublyLinkedListNode(3)
head.next.next = DoublyLinkedListNode(4)

value = insertEnding(head, 5)
head = value
printList(head)
