class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Шаг 1: Инициализируем указатели на стартовой позиции (индекс 0)
        slow = nums[0]
        fast = nums[0]
        
        # Находим точку первой встречи внутри цикла
        # Сначала делаем первый шаг, чтобы запустить цикл while
        slow = nums[slow]          # 1 шаг
        fast = nums[nums[fast]]    # 2 шага
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        # Шаг 2: Переносим slow в начало (индекс 0)
        slow = nums[0]
        
        # Двигаем оба указателя с одинаковой скоростью, пока они не встретятся
        while slow != fast:
            slow = nums[slow]      # 1 шаг
            fast = nums[fast]      # 1 шаг
            
        # Точка их встречи — это и есть дубликат (вход в цикл)
        return slow