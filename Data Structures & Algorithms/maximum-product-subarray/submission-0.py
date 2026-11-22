class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        min_prod=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            new_max=max(n,n*max_prod,n*min_prod)
            new_min=min(n,n*max_prod,n*min_prod)
            max_prod=new_max
            min_prod=new_min
            result=max(result,max_prod)
        return result
