# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val= val
#         self.next = next

class Solution:
    def middleNode(self, head):
        slow,fast= head, head

        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next

        return slow


head=[23,45,67,23,45,67,4,32,5]

answer=Solution()
ans=answer.middleNode(head)
print(ans)