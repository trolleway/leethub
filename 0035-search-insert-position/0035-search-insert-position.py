class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l=0
        r=len(nums)-1
        while l <= r:
            if target==nums[l]: return l
            if target==nums[r]: return r
            if target < nums[l]: return l
            if target > nums[r]: return r+1
            if r==l+1 and nums[l] < target < nums[r]: return l+1
            l=l+1
            r=r-1 

        return 0      







'''
1356   2
!  !

5678   2

'''