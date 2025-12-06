class Solution:
    def maxArea(self, height: List[int]):
        max_area = 0
        left = 0
        right = len(height)-1
        while right>left:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            if area > max_area:
                max_area = area
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return max_area