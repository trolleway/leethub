class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Используем set (множество) вместо списка для финального ответа.
        # Множество хранит только УНИКАЛЬНЫЕ элементы. Повторы сами удалятся!
        unique_triplets = set()
        
        # Обязательно сортируем, чтобы работал метод двух указателей
        nums.sort() 
        
        # Перебираем первое число 'a'
        for i in range(len(nums)):
            a = nums[i]
            
            # Оптимизация: если первое число больше нуля, то сумму 0 мы уже не соберем
            if a > 0:
                break
            
            # Создаем два указателя для поиска 'b' и 'c'
            left = i + 1
            right = len(nums) - 1
            
            # Двигаем указатели навстречу друг другу
            while left < right:
                b = nums[left]
                c = nums[right]
                current_sum = a + b + c
                
                if current_sum == 0:
                    # Мы нашли тройку! 
                    # Превращаем её в tuple (кортеж), так как обычный список [a, b, c] 
                    # нельзя положить в set.
                    unique_triplets.add((a, b, c))
                    
                    # Просто сдвигаем оба указателя на один шаг внутрь.
                    # Если там окажутся дубликаты — не страшно, set их проигнорирует!
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Сумма маловата, нужно число побольше (сдвигаем левый указатель)
                    left += 1
                else:
                    # Сумма великовата, нужно число поменьше (сдвигаем правый указатель)
                    right -= 1
                    
        # Переводим наше множество кортежей обратно в список списков, как просит LeetCode
        result = []
        for triplet in unique_triplets:
            result.append(list(triplet))
            
        return result