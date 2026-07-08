class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        завести множество для триплетов
        отсортировать массив
        цикл по всем элементам, элемент - это первое число
        поскольку массив отсортирован, то если первое число больше нуля, то следующие будут ещё больше нуля, и результат не выйдет
        левый указатель на следующее за а
        правый указатель на последнее
        в цикле while left < right двиигаем указатели настречу друг другу
        b = nums[left]
        c = nums[right]
        current_sum = a + b + c
        если current_sum искомая, то 
            конвертируем её в tuple, заносим tuple в set
            сдвиг обеих указателей внутр
        current_sum меньше искомой, то левый указатель сдвинуть к центру
        current_sum больше искомой, то правый указатель сдвинуть к центру

         '''
        triplets = set()
        nums.sort()
        target=0
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                current_sum = a + b + c
                if current_sum==target:
                    triplets.add((a, b, c))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        result = []
        for triplet in triplets:
            result.append(list(triplet))
            
        return result