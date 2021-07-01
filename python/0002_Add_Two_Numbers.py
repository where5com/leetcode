# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=ListNode()
        curr=result
        temp=0
        while l1 or l2 or temp:
            if l1!=None:
                temp+=l1.val
                l1=l1.next
            if l2!=None:
                temp+=l2.val
                l2=l2.next
            curr.next=ListNode(temp%10)
            temp//=10
            curr=curr.next
        return result.next