class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        mp={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in mp:
                return [mp[diff],i]
            mp[num]=i
