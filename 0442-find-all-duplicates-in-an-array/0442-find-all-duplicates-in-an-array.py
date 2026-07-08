class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        '''
[4,3,2,7,8,2,3,1]
2 3
алгоритм простой, но не укладывается в constant auxiliary space
        visited=set()
        doubles=list()
        for i in range(len(nums)):
            if nums[i] in visited:
                doubles.append(nums[i])
            visited.add(nums[i])
        return doubles

поскольку каждое число может встретится максимум 2 раза, то просмотренные числа делаются отрицательными. Флагом становится отрицательность числа
проход по циклу


        '''
        doubles = list()
        
        for i in range(len(nums)):
            val = abs(nums[i])
            target_index = val - 1 
            if nums[target_index] < 0:
                doubles.append(val)
            else:
                nums[target_index] = nums[target_index] * -1
        return doubles