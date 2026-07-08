# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: # трюк
            return root2
        if not root2:
            return root1

        new_node = TreeNode(root1.val + root2.val)
        new_node.left = self.mergeTrees(root1.left, root2.left)
        new_node.right = self.mergeTrees(root1.right, root2.right)



        return new_node


        
        '''
        рекурсивный алгоритм

            new_node = TreeNode(root1.val + root2.val)
            if root1.left is None and root2.left is not None:
                new_node.left = root2.left
            if root1.left is not None and root2.left is None:
                new_node.left = root1.left
            if root1.right is None and root2.right is not None:
                new_node.left = root2.left
            if root1.right is not None and root2.right is None:
                new_node.right = root1.right
            
                    
            new_node.left = mergeTrees(root1.left, root2.left)
            new_node.right = mergeTrees(root1.right, root2.right)
            return new_node

        

        '''