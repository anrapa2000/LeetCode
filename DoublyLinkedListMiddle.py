class DoublyLinkedListNode:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


def insertMid(head, pos, val):
    newNode = DoublyLinkedListNode(val)
    if pos == 0:
        head = newNode
        return
    if pos == 1:
        newNode.next = head
        head.prev = newNode
        return
    current = head
    for _ in range(1, pos - 1):
        if current is None:
            return head
        current = current.next
    newNode.next = current.next
    current.next = newNode
    newNode.prev = current
    newNode.next.prev = current
    return head


def printList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next


head = DoublyLinkedListNode(1)
head.next = DoublyLinkedListNode(2)
head.next.prev = head
head.next.next = DoublyLinkedListNode(4)
head.next.next.prev = head.next
value = insertMid(head, 3, 5)
head = value
printList(head)
