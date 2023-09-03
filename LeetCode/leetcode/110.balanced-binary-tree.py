from lcutils import make_tree_node

class Solution:
    def isBalanced(self, root) -> bool:
        
        def height_check(root):
            """ return the height of the tree if it's balanced
                return -1 if unbalanced
            """
            if root == None:
                return 0
            
            left = height_check(root.left)
            right = height_check(root.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1 # the tree is unbalanced 

            return 1 + max(left, right)
        
        return height_check(root) != -1
    
root = make_tree_node([1,2,2,3,3,None,None,4,4])
print(Solution().isBalanced(root))