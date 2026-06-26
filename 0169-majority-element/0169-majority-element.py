class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate=None
        count=0    

        for num in nums:
            if count==0:
                candidate=num
                count = 1
            elif candidate == num:   
                count += 1
            else:
                count -= 1

        return candidate
        
        """Boyer-Moore Voting Algorithm
        
        candidate=None
        count=0

        проход по списку
        если count встал в 0, то кандидат =текущий элемент и count+=1
        инесли кандидат==текущий элемент count+=1
        иначе кандидат не равен текущему count-=1

        опционально пройти 2 раз, подсчитать что кандидат действительно есть, если его может не былть
        
        """
