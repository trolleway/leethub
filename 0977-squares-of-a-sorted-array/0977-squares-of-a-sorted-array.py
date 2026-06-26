class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # trivial
        res=list()
        for n in nums:
            res.append(n**2)
        res.sort()
        return res