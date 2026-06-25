class Solution:
    def reverseWords(self, s: str) -> str:
        mode='out'
        prev_char=' '
        words=list()
        for index,char in enumerate(s):
            if char==' ' and mode=='out':
                prev_char=char 
                continue
            if (char==' ' and mode=='in') or ():
                prev_char=char
                #end of word
                mode='out'
                words.append(word)
            if char != ' ':
                mode='in'
                if prev_char==' ':
                    word=list()
                word.append(char)
                prev_char=char
                if mode=='in' and index==len(s)-1:
                    #end of word
                    mode='out'
                    words.append(word)                    
        
        out=''
        res=''
        for index, word in enumerate(words[::-1]):
            out = ''.join(word)
            if index != len(words): out=out+' '
            res = res + out
            
        res = res.strip()
        return res