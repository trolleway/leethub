# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        разворот дерева - это отражение по горизонтали, не по вертикали
        рекурсивный алгоритм
        если not root: none
        поменять местами левый-правый
        левое=вызов себя для левого #технически присваивание тут избыточно, в предудущем операторе уже меняется значение. Но мне так сложнее понимать
        правое=вызов себя для правого 
        вернуть root
        '''

        if not root: return None
        root.left,root.right=root.right,root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root