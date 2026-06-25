class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        
        # Поочередно добавляем буквы, пока обе строки не закончатся
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
            
        # Добавляем остаток из word1 (если она была длиннее)
        if i < len(word1):
            result.append(word1[i:])
            
        # Добавляем остаток из word2 (если она была длиннее)
        if j < len(word2):
            result.append(word2[j:])
            
        # Объединяем список букв в одну строку и возвращаем ее
        text =  "".join(result)
        return text