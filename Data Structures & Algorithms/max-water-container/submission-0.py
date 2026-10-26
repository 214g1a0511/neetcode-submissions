class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        for l in range(len(heights)):
            for r in range(l+1,len(heights)):
                ans=(r-l)*min(heights[l],heights[r])
                res=max(ans,res)
        return res

        