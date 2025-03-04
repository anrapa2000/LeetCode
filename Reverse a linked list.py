class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while(current.next !=None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
value = Solution()
print(value.reverseList([1,2,3,4,5]))