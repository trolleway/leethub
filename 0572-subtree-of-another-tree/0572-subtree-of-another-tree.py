# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if self.isSameTree(root, subRoot):return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        '''
        рекурсивная функция: проверка одинаковости 2 деревьев
            если не л и не п: да (это leaf)
            теперь может быть пустым только один потомок из двух
            если не п или не q: нет.  это значит что в одном дереве тут есть узел, в другом нет
            если p.val != q.val: нет
            если л.вал!=п.вал:нет
            вернуть результат проверки обеих левых и обеих правых
        рекурсивная функция: проверка поддерева
            если не рут: нет #в пустом дереве нет поддерева
            если self.isSameTree(root, subRoot): да
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        '''
        