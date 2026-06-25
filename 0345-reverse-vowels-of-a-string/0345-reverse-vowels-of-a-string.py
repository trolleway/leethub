class Solution:
    def testpayload(self,char) -> bool:
        assert len(char)==1
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            return True
        else:
            return False
    def reverseVowels(self, s: str) -> str:
        vovels_positions = list()
        for index,char in enumerate(s):
            if self.testpayload(char):
                vovels_positions.append(index)
        if len(vovels_positions) < 2:
            return s
        out=list(s)

        for i,pos in enumerate(vovels_positions):

            reverse_pos = vovels_positions[-i-1]
            out[pos]=s[reverse_pos]
            
        return ''.join(out)