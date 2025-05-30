class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i in range(len(nums)):
            res = target - nums[i]
            if res not in map:
                map[nums[i]] = i
            else:
                return(i, map[res])