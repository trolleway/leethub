class Solution:
    def norm(self,s):
        text = s.lower().replace(' ','')
        out = "".join([char for char in text if char.isalnum()])
        return out
        
    def isPalindrome(self, s: str) -> bool:
        s=self.norm(s)
        pntl=0
        pntr=len(s)-1
        exit=False
        while exit == False:
            if pntl>=pntr: return True
            if s[pntl]!=s[pntr]:
                return False
            else:
                pntl=pntl+1
                pntr = pntr - 1