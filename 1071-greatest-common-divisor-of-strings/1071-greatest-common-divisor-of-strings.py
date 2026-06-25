class Solution:
    def testcd(self, str1: str, candidate: str) -> bool:
        if not candidate: 
            return False
        # QUICK CHECK: If candidate length doesn't divide str1 length perfectly, skip it
        if len(str1) % len(candidate) != 0: 
            return False
        
        # Calculate exactly how many times it must repeat
        repeat_count = len(str1) // len(candidate)
        return candidate * repeat_count == str1

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2: 
            return str1
        
        # Loop BACKWARD from the maximum possible length to 1
        # This guarantees the first match we find is the GREATEST common divisor
        max_possible_len = min(len(str1), len(str2))
        
        for i in range(max_possible_len, 0, -1):
            candidate = str1[0:i]
            if self.testcd(str1, candidate) and self.testcd(str2, candidate):
                return candidate
                
        return ""