# https://leetcode.com/problems/add-two-numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from lcutils import *

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        previous = ListNode() 
        head = previous
        while l1 or l2 or carry!=0:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, remainder = divmod(val1 + val2 + carry, 10)
            new_node = ListNode(remainder)
            
            previous.next = new_node
            previous = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head.next 
    

l1 = make_linked_list([1,2,3])
l2 = make_linked_list([4,8,6])
head = Solution().addTwoNumbers(l1, l2)
print(head)
