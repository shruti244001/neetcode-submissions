# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode=ListNode(-1)
        ans=dummynode

        t1 = l1
        t2 = l2
        carry=0

        while t1 != None or t2 != None:
            Sum=carry
            if (t1): Sum += t1.val
            if (t2): Sum += t2.val
            newnode = ListNode(Sum%10)
            carry=Sum // 10

            ans.next=newnode
            ans=ans.next

            if (t1): t1=t1.next
            if (t2): t2=t2.next
        
        if (carry):
            newnode=ListNode(carry)
            ans.next=newnode
        return dummynode.next

        
