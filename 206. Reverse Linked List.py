class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        # prev = None
        # current = head
        # while current.next is not None:
        #     temp = current.next
        #     current.next = prev
        #     prev = current
        #     current = temp
        # return prev

        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
        
            
        


value = Solution()
print(value.reverseList([1, 2, 3, 4, 5]))
