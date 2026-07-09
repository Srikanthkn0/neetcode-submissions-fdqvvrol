class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                res=max(res, (min(height[i],height[j]) * (j-i)))
        return res        