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
            h.heappush(heap,(value, key)) # build min heap until k elements
            if len(heap) > k: # by popping the smallest one (root), we will only hold k largest
                h.heappop(heap)

        return [key for value, key in heap] # since we are using tuples
