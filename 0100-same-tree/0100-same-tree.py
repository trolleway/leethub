# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        рекурсивный алгоритм
        если не п и не q: да
        теперь может быть пустым только один потомок из двух
        если не п или не q: нет.  это значит что в одном дереве тут есть узел, в другом нет
        если p.val != q.val: нет
        вернуть результат проверки обеих левых и обеих правых

        '''
        if not p and not q: return True
        if not p or not q: return False #это значит что в одном дереве тут есть узел, в другом нет
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)