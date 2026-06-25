class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        
        while left < right:
            # 1. Inline calculation avoids function call overhead
            h_left = height[left]
            h_right = height[right]
            
            # 2. Use built-in functions; they are optimized in C
            area = (right - left) * min(h_left, h_right)
            
            if area > maxarea:
                maxarea = area
                
            # 3. Fast pointer movement
            if h_left < h_right:
                left += 1
            else:
                right -= 1
                
        return maxarea