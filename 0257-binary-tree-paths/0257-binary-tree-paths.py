# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Базовый случай 1: Если узел пустой, возвращаем пустой список
        if not root:
            return []
            
        # Базовый случай 2: Если дошли до листа, возвращаем его значение как единственный путь
        if not root.left and not root.right:
            return [str(root.val)]
            
        # Локальный список для путей текущего поддерева
        paths = []
        
        # Шаг 1: Собираем все пути из левого поддерева
        if root.left:
            left_paths = self.binaryTreePaths(root.left)
            for path in left_paths:
                # К каждому найденному пути снизу прибавляем текущий корень сверху
                paths.append(str(root.val) + "->" + path)
                
        # Шаг 2: Собираем все пути из правого поддерева
        if root.right:
            right_paths = self.binaryTreePaths(root.right)
            for path in right_paths:
                # Точно так же склеиваем текущий корень с правыми путями
                paths.append(str(root.val) + "->" + path)
                
        # Возвращаем собранные пути на уровень выше
        return paths
        
        '''
        вернуть список строк
        рекурсивная функция



        '''