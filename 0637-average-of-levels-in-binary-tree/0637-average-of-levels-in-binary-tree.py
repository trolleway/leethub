# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        '''
        алгоритм обхода дерева в ширину
        
        '''


        from collections import deque

        queue = deque([root])
        level_avgs=list()
        while queue:
            # в этот момент в queue весь уровень
            level_size = len(queue) 
            values_on_level = list()
            for _ in range(level_size):
                #эта конструкция проходит только по узлам одного уровня, в товремякак в очередь добавляются новые узлы
                node = queue.popleft()
                values_on_level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            level_avgs.append(sum(values_on_level) / len(values_on_level))
        return level_avgs