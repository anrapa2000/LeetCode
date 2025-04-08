# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # nodesSeen = set()
        # current = head
        # while current:
        #     if current in nodesSeen:
        #         return True
        #     nodesSeen.add(current)
        #     current = current.next
        # return False

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
