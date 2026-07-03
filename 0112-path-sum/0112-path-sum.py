# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        рекурсивный алгоритм. Возвращает логическое значение
        если not root: нет # это проверка на пустой запрос
        если нет левого, и нет правого: 
            если цель==значение:да
            если цель != значение: нет
        новцель=цель-значение текущего узла
        вернуть себя(левый, новцель) или себя(правый,новцель)
        '''
        if not root: return False
        if not root.left and not root.right:
            if targetSum==root.val: return True
            if targetSum!=root.val: return False
        nextTargetSum = targetSum - root.val
        return self.hasPathSum(root.left,nextTargetSum) or self.hasPathSum(root.right,nextTargetSum)