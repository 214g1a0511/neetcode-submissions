class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=len(nums)-1
        l=0
        mid=(l+r)//2
        while l<=r:
            if nums[l]==target:
                return l
            elif nums[l]<target:
                l+=1
            else:
                r-=1
        return -1
        