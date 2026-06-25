class Solution:
    def is_number_top(self,num:int,candies:list)->bool:
        if num >=max(candies):
            return True
        return False
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = list()
        for index, item in enumerate(candies):
            if self.is_number_top(item+extraCandies,candies):
                res.append(True)
            else:
                res.append(False)
        return res

'''
23513
!

2+extra is top? check
'''