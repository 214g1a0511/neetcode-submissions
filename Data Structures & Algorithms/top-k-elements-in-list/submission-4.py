import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp={}
        for num in nums:
            hp[num]=1+hp.get(num,0)
        heap=[]
        for num,count in hp.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count,num in heap]