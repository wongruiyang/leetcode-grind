class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r,area = 0, len(height) - 1, 0
        
        while (l<r):
            area = max(area, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return area
        