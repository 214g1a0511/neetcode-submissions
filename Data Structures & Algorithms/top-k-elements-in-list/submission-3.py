class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp={}
        for num in nums:
            hp[num]=1+hp.get(num,0)
        arr=[]
        for num,count in hp.items():
            arr.append([count,num])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
