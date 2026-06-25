class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
        """
        сортировать массив
        пройти по всем элементам с 1
        если элемент == элемент[-1] return true


        """
        