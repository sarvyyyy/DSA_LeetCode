class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        water = 0
        k = len(height)
        for i in range(k):
            while st and height[i]>height[st[-1]]:
                floor = st.pop()
                if not st:
                    break

                right = i
                left = st[-1]
                width = i - st[-1] - 1
                min_boundary = min(height[i],height[st[-1]]) - height[floor]
                water+= min_boundary*width
            st.append(i)
            
        return water


