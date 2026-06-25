class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, item1 in enumerate(nums):
            skipped_n2 = index1
            index2 = len(nums)-1
            for index2 in range(len(nums) - 1, -1, -1):
                if index2 == skipped_n2:
                    continue
                if item1+nums[index2]==target:
                    return [index1,index2]