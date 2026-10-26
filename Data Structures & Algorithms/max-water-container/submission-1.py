class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # res=0
        # for l in range(len(heights)):
        #     for r in range(l+1,len(heights)):
        #         ans=(r-l)*min(heights[l],heights[r])
        #         res=max(ans,res)
        # return res
        res=0
        l,r=0,len(heights)-1
        while l<r:
            ans=(r-l)*min(heights[l],heights[r])
            res=max(ans,res)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return res
        

        