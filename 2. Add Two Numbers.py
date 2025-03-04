from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            result = value1 + value2 + carry

            carry = result // 10
            result = result % 10
            newNode = ListNode(result)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry != 0:
            newNode = ListNode(carry)
            curr.next = newNode
        return dummy.next


root1 = ListNode(2)
root1.next = ListNode(4)
root1.next.next = ListNode(3)

root2 = ListNode(5)
root2.next = ListNode(6)
root2.next.next = ListNode(4)

print(Solution().addTwoNumbers(root1, root2))
