class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #stack
        r1=list()
        r2=list()

        for char in s:
            if char == '#':
                if len(r1) > 0:
                    r1.pop()
            else:
                r1.append(char)

        for char in t:
            if char == '#':
                if len(r2) > 0:
                    r2.pop()
            else:
                r2.append(char)
        return r1 == r2


"""
занесение символов в стек

 |
ab#c
ad#c
 |
"""

