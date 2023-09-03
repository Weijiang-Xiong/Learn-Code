from lcutils.structures import ListNode, make_linked_list

class Solution(object):
    
    def removeDuplicateNodes(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set() # faster than list 
        node = head
        prev = None
        
        while node is not None:

            if node.val in seen:
                prev.next = node.next 
                node = node.next
            else:
                seen.add(node.val)
                prev = node
                node = node.next 

        return head
    
head = make_linked_list([1, 2, 3, 3, 2, 1])

head = Solution().removeDuplicateNodes(head)

        
        
    