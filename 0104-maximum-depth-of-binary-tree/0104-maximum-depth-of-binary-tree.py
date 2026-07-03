# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def DepthCalc(root):
            if root is None: return 0
            if not root.left and not root.right:
                return 1
            return max(DepthCalc(root.left),DepthCalc(root.right))+1
        '''
        рекурсивный алгоритм

        если левого и правого нет, то вернуть 1
        иначе вернуть макс(глубина левого, глубина правого)+1
        '''
        return DepthCalc(root)