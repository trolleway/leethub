class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        val=sum(nums[0:k])
        maxval = val/k
        for r in range(k,len(nums)):
            val = val + nums[r] - nums[r-k]
            nv=val/k
            if nv>maxval:
                maxval=nv

        return maxval

"""
sliding window
add right element, remove left element

подсчёт среднего для начальной группы


1 12 -5 -6 50 3
! !  !   !
window:0-3

"""