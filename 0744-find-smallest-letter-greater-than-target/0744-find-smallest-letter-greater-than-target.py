class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        бинарный поиск
        фцнкция номер среднего: (номмин+номмах)//2
        маркеры обозначают номера элементов
        маркеры на крайние элементы
        цикл пока левый <= правый #трюк
            расчёт индекса среднего элемента 
            если значение сред элемента <= букве: нужный правее, левый=средний+1
            если значение срэлемента>цели: прав=сред-1
        после цикла левый указывает на первый элемент который больше цели #трюк
        проверить, вышел ли левый за пределы массива, если да то вернуть первый элемент

        '''
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        left=0
        right=len(letters)-1
        while left <= right:
            mid = (left+right)//2
            if letters[mid]<=target:
                left=mid+1
            elif letters[mid]>target:
                right=mid-1
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]

'''
0 1 2  c
c f j

'''