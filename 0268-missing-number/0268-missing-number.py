class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=set(nums)
        for i in range(len(nums)+1):
            if i not in s: return i
"""
3 0 1
sort
0 1 3
просмотр пар, определение что число не отстоит на единицу


"""
        