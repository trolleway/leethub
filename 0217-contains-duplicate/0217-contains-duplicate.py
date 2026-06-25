class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2=sorted(nums)
        for i in range(1,len(nums2)):
            if nums2[i]==nums2[i-1]:
                return True
        return False
        """
        сортировать массив
        пройти по всем элементам с 1
        если элемент == элемент[-1] return true


        """
        