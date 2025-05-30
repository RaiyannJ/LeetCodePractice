import heapq as h

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        freq = {}

        for e in nums:
            freq[e] = 1 + freq.get(e, 0)
        
        heap = []
        for key, value in freq.items():
            h.heappush(heap,(value, key))
            if len(heap) > k:
                h.heappop(heap)

        return [key for value, key in heap] # string 
