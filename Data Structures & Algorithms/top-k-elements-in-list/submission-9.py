class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp={}
        for num in nums:
            hp[num]=1+hp.get(num,0)
        bucket=[[] for _ in range(len(nums)+1)]
        for num,count in hp.items():
            bucket[count].append(num)
        arr=[]
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                arr.append(num)
            if len(arr)==k:
                return arr


        