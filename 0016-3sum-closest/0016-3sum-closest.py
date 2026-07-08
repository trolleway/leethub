class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''      
        отсортировать массив
        closest_sum инициализируется первыми 3 числами
        цикл по всем элементам, элемент - это первое число
        
        левый указатель на следующее за а
        правый указатель на последнее
        в цикле while left < right двиигаем указатели настречу друг другу
        b = nums[left]
        c = nums[right]
        current_sum = a + b + c
        если current_sum искомая, то 
            return current_sum
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
            
        current_sum меньше искомой, то левый указатель сдвинуть к центру
        current_sum больше искомой, то правый указатель сдвинуть к центру

        '''

        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n):
            # Пропускаем дубликаты для первого числа, чтобы не делать лишнюю работу
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Если нашли идеальное совпадение, сразу возвращаем его
                if current_sum == target:
                    return current_sum
                
                # Если текущая сумма БЛИЖЕ к target, чем сохраненная ранее
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Двигаем указатели в зависимости от того, не дотянули мы или перелетели
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum