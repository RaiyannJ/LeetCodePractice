class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mySet = set(nums)

        for e in nums:
            if (e - 1) in nums: # check if it is the start of a sequence or not
                continue
            else:
                length = 1 # if it is, begin counting the consecutive numbers
                while (e +length) in mySet:
                    length+=1
                res = max(length, res)

        return res

