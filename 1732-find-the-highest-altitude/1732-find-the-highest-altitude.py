class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        al=list()
        
        current_al=0
        al.append(current_al)
        for value in gain:
            current_al=current_al+value
            al.append(current_al)
        return max(al)
