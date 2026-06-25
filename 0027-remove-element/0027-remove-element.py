class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow=0
        fast=0
        cnt=0
        for fast in range(len(nums)):
            if nums[slow]==val and nums[fast]!=val:
                nums[slow],nums[fast]=nums[fast],nums[slow]
            if nums[slow]!=val:
                slow=slow+1
        for i in range(len(nums)):
            if nums[i]!=val:
                cnt+=1 
        return cnt

