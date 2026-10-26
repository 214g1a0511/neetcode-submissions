import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        bucket=[[] for _ in range(len(nums)+1)]

        for num, count in freq.items():
            bucket[count].append(num)
        answer=[]
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                answer.append(num)
            if len(answer)==k:
                return answer