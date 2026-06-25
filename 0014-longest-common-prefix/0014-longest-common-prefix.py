class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out=list()
        if strs[0]=='':return ''
        for i in range(len(strs[0])):
            char1=strs[0][i]
            for word in strs:
                if word=="":
                    return ""
                if i > len(word)-1:
                    return "".join(out)
                charn=word[i]
                if i>len(word) or charn != char1:
                    return "".join(out)
            out.append(char1)
        return "".join(out)


'''
flower
flow
flight
!!!!
out of any word or char not same
'''