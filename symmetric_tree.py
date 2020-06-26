# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        
        return self.recursion(root.left, root.right)
    
    
    def recursion(self, node1, node2):
        if not node1 or not node2: 
            return node1 == node2
        if node1.val != node2.val:
            return False
        return self.recursion(node1.left, node2.right) and self.recursion(node1.right, node2.left)
    
    
    def recursion2(self, node1, node2):
        if not node1 and  not node2: 
            return True
        elif not node1 or not node2:
            print(node1, node2)
            return False
        if node1 and node2:
            if not self.recursion(node1.left, node2.right)  or not self.recursion(node1.right, node2.left):
                return False
            if node1.val != node2.val:
                return False
            
        return True
        
            
    
    
    def _isSymmetric(self, root: TreeNode) -> bool:
        if not root: return  True
        
        stack = [(root.left, root.right)]
        
        while len(stack)>0:
            # Node to be compared
            node1, node2= stack.pop()
            
            
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val == node2.val:
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
            else:
                return False
            
        return True
