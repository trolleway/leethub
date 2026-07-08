class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        '''
        алгоритм со слайсами. 
        проверка что задача выполнима
        if m*n!=len(original):
            return []
        
        for i in range(0,len(original),n):

        Так же можно создать пустой массив, итерировать входной, и расчитывать адреса математическими выражениями
        на других языках типа java это может быть быстрее за счёт оптимизаций в компиляторе
        

        1234
        12
        '''
        out=list()
        #проверка что входные параметры валидны
        if m*n!=len(original):
            return []
        for i in range(0,len(original),n):
            out.append(original[i:i+n])

        return out
