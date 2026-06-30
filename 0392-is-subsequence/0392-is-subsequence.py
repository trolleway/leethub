class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m1=0
        m2=0
        if s=='':  return True
        if t=='': return False
        while m2<len(t) and m1<len(s):
            if s[m1]==t[m2]:
                m1=m1+1
            m2=m2+1
        if m1==len(s):
            return True
        else:
            return False
        
        
        
        
        
        
        '''
м1
м2
цикл
сравнить символы под маркерами
если одинаковые то сдвинуть м1
сдвинуть м2

если м2 на последнем то конец цикла
если м1 на последнем, то да
        '''
        