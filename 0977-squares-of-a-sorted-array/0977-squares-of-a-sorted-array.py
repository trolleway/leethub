class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointers
        out=[None] * len(nums)
        m1=0
        m2=len(nums)-1
        counter=len(nums)-1
        while m1 <= m2:
            
            if abs(nums[m1])>=abs(nums[m2]):
                out[counter]=nums[m1]**2
                m1+=1
                counter = counter-1
            else:
                out[counter]=nums[m2]**2
                m2-=1
                counter = counter-1

            if m1==m2:
                stop=True
                out[counter]=nums[m1]**2
            
        return out

        """
-4,-1,0,3,10
^         ^

отрицательное и положительное число после операции одинаковы
маркер1 на первый элемент
маркер2 на последний элемент
цикл
обработка большего значения под маркерами, результат поместить в конец
сдвинуть маркер с большим значением

        """