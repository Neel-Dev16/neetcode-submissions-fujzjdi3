# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [],[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        carry=0
        head=None
        while stack1 or stack2 or carry:
            v1=stack1.pop() if stack1 else 0
            v2=stack2.pop() if stack2 else 0
            value=v1+v2+carry
            digit=value%10
            carry=value//10
            node=ListNode(digit)
            node.next=head
            head=node
        return head
