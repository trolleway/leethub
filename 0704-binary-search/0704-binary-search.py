class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        бинарный поиск
        два маркера - номера крайних элементов
        цикл пока левый <= правый #трюк
            индекс среднего элемента = левый+(правый-левый)//2 #трюк
            если значение сред элемента = цель:вернуть индекс
            если значение срэлемента<цели: лев=сред+1
            если значение срэлемента>цели: прав=сред-1
        '''
        left=0
        right=len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else: right = mid-1
        return -1

        '''
0  1 2 3 4 5        
       .
-1 0 3 5 9 12
           .
        '''