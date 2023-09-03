from typing import List

class ListNode:
    
    def __init__(self, x=0):
        self.val = x
        self.next = None
    
    def __str__(self) -> str:
        ret = repr(self.val)
        if isinstance(self.next, ListNode):
            ret += " => " + self.next.__str__()
        return ret

def make_linked_list(array:List[int]):
    linked_list = [ListNode(array[0])]
    for num in array[1:]:
        new_node = ListNode(num)
        linked_list[-1].next = new_node
        linked_list.append(new_node)
    return linked_list[0]

class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self, level=0):
        # modified from https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
        ret = "   "*(level-1) + "|__" +repr(self.val)+"\n" if level >= 1 else "   "*level +repr(self.val)+"\n"
        for node in [self.left, self.right]:
            if isinstance(node, TreeNode):
                ret += node.__str__(level+1)
        return ret
    
def make_tree_node(array:List[int]):
    
    all_nodes = [TreeNode(val=val) if val is not None else None
                 for val in array]
    
    for idx, node in enumerate(all_nodes):
        try:
            node.left = all_nodes[2*idx + 1]
        except:
            node.left = None
        
        try:
            node.right = all_nodes[2*idx+2]
        except:
            node.right = None
            
    return all_nodes[0]


if __name__ == "__main__":
    head = make_linked_list([1,2,3,4,5,6,7])
    print(head)
    head = make_tree_node([1,2,3,4,5,6,7, 8])
    print(head)
    