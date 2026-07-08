import math
class Solution:
    '''
    расчёт для элемента 
1   2 3 4
24 12 8 6

математическое решение
новый массив заполняется произведениями слева
затем этот же новый массив проходится в обратном порядке, и заполняется произведениями справа
это трюк
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n #заполнение массива единицами
        
        # Шаг 1: Префиксные произведения (слева направо)
        left_prod = 1
        for i in range(n):
            answer[i] = left_prod
            left_prod = left_prod * nums[i]
            
        # Шаг 2: Суффиксные произведения (справа налево)
        right_prod = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right_prod
            right_prod = right_prod * nums[i]
            
        return answer

        '''




bruteforce. Так не принимается, потому что slice дорогие
        answer=list()
        for i in range(len(nums)):
            answer.append(math.prod(nums[0:i])*math.prod(nums[i+1:len(nums)]))

        return answer

0:0*1:4
0:1*2:4
0:2*3:4
0:3*4:4

для 0: math.prod(nums[0:0])*math.prod(nums[1:4])
для 1: math.prod(nums[0:1])*math.prod(nums[2:4])
для 2: math.prod(nums[0:2])*math.prod(nums[3:4])
для 3: math.prod(nums[0:3])*math.prod(nums[4:4])
        '''
