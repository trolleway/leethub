class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        for fast in range(len(nums)):
            if nums[slow]==0 and nums[fast]!= 0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
            if nums[slow]!=0:
                slow = slow+1



"""
0 1 0 3 12
  !        
!
1 0 0 3 12
      !
  !

1 3 0 0 12 
        !
    !
1 3 12 0 0
         !
    !
"""